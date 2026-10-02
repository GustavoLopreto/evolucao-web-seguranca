"""Monta o PDF único de entrega: caderno + evidências E01–E06 + ficha exportada.

Uso (na raiz do projeto):  python scripts/gerar_pdf.py
Saída: Entrega/Entrega_WEB.pdf
"""
import html
import re
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CADERNO = RAIZ / "Respostas_WEB_SuaIdentificacao.txt"
EVIDENCIAS = RAIZ / "Evidencias"
FICHA = RAIZ / "Ficha"
SAIDA = RAIZ / "Entrega"
NAVEGADORES = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
]

CSS = """
@page { size: A4; margin: 18mm 16mm; }
body { font-family: 'Segoe UI', Arial, sans-serif; font-size: 10.5pt; line-height: 1.45; color: #111; }
h1 { font-size: 17pt; margin: 0 0 8pt; }
h2 { font-size: 13pt; margin: 18pt 0 4pt; padding-top: 6pt; border-top: 1px solid #999; break-after: avoid; }
h3 { font-size: 11pt; margin: 12pt 0 4pt; break-after: avoid; }
p { margin: 0 0 6pt; text-align: justify; }
.pergunta { background: #eef3fa; border-left: 3px solid #36c; padding: 5pt 8pt; font-style: italic; }
.secao { break-before: page; }
figure { margin: 8pt 0 12pt; break-inside: avoid; text-align: center; }
figure img { max-width: 100%; max-height: 150mm; border: 1px solid #888; }
figcaption { font-size: 9pt; color: #444; }
.falta { color: #b00; font-weight: bold; }
ul { margin: 0 0 6pt 16pt; padding: 0; }
code { font-family: Consolas, monospace; font-size: 9.5pt; }
"""


def inline(texto):
    t = html.escape(texto)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    return re.sub(r"`(.+?)`", r"<code>\1</code>", t)


def imagem_da_evidencia(codigo):
    for arq in sorted(EVIDENCIAS.glob(codigo + "*")):
        if arq.suffix.lower() in (".png", ".jpg", ".jpeg"):
            return arq
    return None


def caderno_para_html(texto, faltando):
    partes = []
    linhas = texto.splitlines()
    partes.append(f"<h1>{inline(linhas[0])}</h1>")
    for linha in linhas[1:]:
        s = linha.strip()
        if not s:
            continue
        if re.match(r"^Q\d\d — ", s):
            partes.append(f"<h2>{inline(s)}</h2>")
        elif s.startswith("Pergunta:"):
            partes.append(f'<p class="pergunta">{inline(s)}</p>')
        elif s == "Resposta:":
            continue
        elif s.isupper() and len(s) > 8:
            partes.append(f'<h2 class="secao">{inline(s)}</h2>')
        else:
            m = re.match(r"^(E0[1-6]) — ", s)
            if m:
                partes.append(f"<h3>{inline(s)}</h3>")
                img = imagem_da_evidencia(m.group(1))
                if img:
                    partes.append(f'<figure><img src="{img.as_uri()}"><figcaption>{m.group(1)} — {html.escape(img.name)}</figcaption></figure>')
                else:
                    faltando.append(f"captura {m.group(1)} em Evidencias/")
                    partes.append(f'<p class="falta">[captura {m.group(1)} ainda não salva em Evidencias/]</p>')
            else:
                partes.append(f"<p>{inline(s)}</p>")
    return "\n".join(partes)


def markdown_para_html(texto):
    partes, lista = [], False
    for linha in texto.splitlines():
        s = linha.strip()
        if s.startswith("- "):
            if not lista:
                partes.append("<ul>")
                lista = True
            partes.append(f"<li>{inline(s[2:])}</li>")
            continue
        if lista:
            partes.append("</ul>")
            lista = False
        if not s or s == "---":
            continue
        m = re.match(r"^(#{1,3}) (.+)", s)
        if m:
            nivel = len(m.group(1))
            classe = ' class="secao"' if nivel == 1 else ""
            partes.append(f"<h{nivel + 1}{classe}>{inline(m.group(2))}</h{nivel + 1}>")
        else:
            partes.append(f"<p>{inline(s)}</p>")
    if lista:
        partes.append("</ul>")
    return "\n".join(partes)


def main():
    faltando = []
    texto = CADERNO.read_text(encoding="utf-8")
    for marca in ("[PREENCHER", "[AJUSTAR", "[Se "):
        n = texto.count(marca)
        if n:
            faltando.append(f"{n} trecho(s) '{marca}...]' no caderno")
    corpo = caderno_para_html(texto, faltando)

    fichas = sorted(FICHA.glob("*.md"))
    fichas = [f for f in fichas if f.name.lower() != "readme.md"]
    if fichas:
        corpo += '\n<h2 class="secao">ANEXO — FICHA EXPORTADA PELA FERRAMENTA</h2>\n'
        corpo += markdown_para_html(fichas[-1].read_text(encoding="utf-8"))
    else:
        faltando.append("ficha exportada (.md) em Ficha/")

    SAIDA.mkdir(exist_ok=True)
    pagina = SAIDA / "Entrega_WEB.html"
    pdf = SAIDA / "Entrega_WEB.pdf"
    pagina.write_text(f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Entrega WEB</title><style>{CSS}</style></head><body>{corpo}</body></html>', encoding="utf-8")

    navegador = next((n for n in NAVEGADORES if Path(n).exists()), None)
    if not navegador:
        sys.exit(f"Edge/Chrome não encontrado. Abra {pagina} e use Ctrl+P → Salvar como PDF.")
    subprocess.run([navegador, "--headless", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={pdf}", pagina.as_uri()], check=True, capture_output=True)
    print(f"PDF gerado: {pdf}")
    if faltando:
        print("\nATENÇÃO — ainda falta antes de entregar:")
        for item in faltando:
            print(" -", item)
    else:
        print("Nada pendente: pronto para enviar no Moodle.")


if __name__ == "__main__":
    main()

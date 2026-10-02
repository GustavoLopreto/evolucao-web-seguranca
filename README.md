# Aula 2 — Evolução da Web e segurança cibernética

Atividade individual do curso (SENAI): percorrer 16 marcos da história da Web em um laboratório local, investigar três incidentes simulados em um portal fictício de biblioteca e entregar um PDF único.

## O que é entregue

| Entregável | Onde está |
|---|---|
| Caderno com 32 respostas (Q01–Q32) | `Respostas_WEB_SuaIdentificacao.txt` |
| 6 evidências (E01–E06) | `Evidencias/` |
| Ficha das 3 investigações exportada pelo laboratório | `Ficha/` |
| PDF único para o Moodle | `Entrega/Entrega_WEB.pdf` (gerado pelo script) |

## Estrutura

```
Atividade_WEB/
├── README.md                               este arquivo
├── GUIA_PASSO_A_PASSO.md                   roteiro com caixas de marcação
├── Respostas_WEB_SuaIdentificacao.txt      caderno de respostas
├── Linha_do_Tempo_WEB_Laboratorio_v2.html  laboratório (material do professor)
├── Evidencias/                             capturas E01–E06
├── Ficha/                                  ficha .md exportada pela ferramenta
├── Entrega/                                PDF final
└── scripts/gerar_pdf.py                    monta caderno + evidências + ficha em um PDF
```

## Como refazer

1. Siga `GUIA_PASSO_A_PASSO.md`.
2. Rode `python scripts/gerar_pdf.py` (usa só a biblioteca padrão do Python e o Edge ou Chrome instalado).

## Resumo do que a atividade ensina

As três investigações parecem iguais (algo inesperado apareceu na tela), mas falham em lugares diferentes e pedem controles diferentes:

| | INV-01 Formulários | INV-02 Cookies | INV-03 DOM |
|---|---|---|---|
| Benefício | buscar no catálogo | manter sessão e reservas | comentar sem recarregar |
| O que aconteceu | busca devolveu cadastros de leitores | local de retirada mudou sozinho | comentário virou "aviso" da página |
| Nome do problema | injeção de SQL | CSRF | injeção de HTML via DOM (base do XSS) |
| Onde falha | servidor monta o SQL colando a entrada | servidor aceita a operação só pela sessão | cliente insere a entrada com `innerHTML` |
| Limite de confiança | dado do cliente → comando do banco | sessão válida → pedido intencional | dado não confiável → API que interpreta HTML |
| Controle que resolve | consulta parametrizada | token anti-CSRF validado no servidor | `textContent` |
| Controles que não resolvem | HTTPS, limite de caracteres | HttpOnly, trocar GET por POST | limite de caracteres, HTTPS |

Ideias que se repetem nas 32 questões:

- **Cada controle age em uma camada.** HTTPS protege o trajeto; não corrige o que o servidor ou o cliente fazem com o dado.
- **A interface não é barreira.** Esconder um botão com CSS, limitar um campo ou calcular no navegador não impede uma requisição feita diretamente.
- **Autenticar, autorizar e verificar a intenção são coisas distintas.** Saber quem é o usuário não diz o que ele pode fazer nem se foi ele quem pediu.
- **Desligar a função não é solução.** Um bom controle contém o efeito indevido e preserva o benefício.
- **A data do marco não é a data da vulnerabilidade.** 1993 é quando surgiram os formulários, não quando a injeção de SQL foi descrita.
- **Simulação não é prova.** O laboratório não executa SQL, não cria cookies reais e não roda código digitado.

## Sobre a autoria

As respostas do caderno foram redigidas com apoio de IA (Claude) a partir do roteiro e do laboratório, e depois conferidas e ajustadas na execução. As evidências são capturas das telas obtidas ao executar o laboratório.

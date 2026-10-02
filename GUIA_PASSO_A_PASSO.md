# Guia passo a passo — do laboratório ao PDF

Tempo estimado: 40 a 60 minutos. Faça na ordem. Marque cada caixa ao concluir.

## Regras que valem para tudo

- **Não feche nem recarregue a aba do laboratório** até exportar a ficha (Parte 5). Os registros internos se perdem.
- Captura de tela: **Win + Shift + S**, selecione a área, clique na notificação e salve em `Evidencias/` com o nome indicado.
- Nos três marcos com investigação, use **Dinâmica → Disparar agora** em vez de esperar 2 minutos.
- Depois do incidente, **não clique em Restaurar** antes de capturar.
- Leia a resposta correspondente no caderno enquanto executa. Se a sua tela mostrar algo diferente, corrija o caderno: vale o que você observou.

## Parte 0 · Preparação (5 min)

- [ ] Abra `Linha_do_Tempo_WEB_Laboratorio_v2.html` no Edge ou Chrome (botão direito → Abrir com).
- [ ] Confirme os botões **1 · Benefícios**, **2 · Segurança**, **Mapa geral** e **Dinâmica**.
- [ ] Abra `Respostas_WEB_SuaIdentificacao.txt` e preencha nome, turma e navegador.

## Parte 1 · INV-01 Formulários (Q03–Q07, E01, E02)

Ideia central: o texto digitado na busca foi colado dentro do comando SQL no servidor.

- [ ] **Mapa geral → 1993 — Imagens e formulários**, modo **Benefícios**.
- [ ] Veja **Sem o recurso**; depois ligue **Com o recurso**.
- [ ] Busque `redes`, `web` e `http`. Confira com a Q03.
- [ ] **Dinâmica → Disparar agora**. Espere uns 5 segundos sem trocar de aba.
- [ ] Com os três cadastros (Ana, Bruno, Carla) na tela, capture: `E01_Formularios_incidente.png`.
- [ ] **Investigar o que aconteceu** → aba **1 · Observar** → preencha "O que você observou?".
- [ ] Aba **2 · Hipótese** → preencha os dois campos (base: Q04).
- [ ] Aba **3 · Rastrear** → **Reproduzir percurso** → leia o pseudocódigo → **Comparar processamento protegido**.
- [ ] Aba **4 · Proteger**. Para cada alternativa, nesta ordem — A, B, D e por último C:
  1. selecione e escreva a previsão no campo;
  2. **Aplicar ao modelo e testar os dois usos**;
  3. leia os dois cartões (efeito indevido / uso legítimo) e compare com a Q06;
  4. **Ver o resultado e usar a aplicação → Testar uso legítimo**;
  5. volte em **Investigar este marco → Proteger**.

| Letra | Intervenção | Contém o efeito? | Mantém a busca? |
|---|---|---|---|
| A | Adicionar HTTPS | Não | Sim |
| B | Limitar o campo a 20 caracteres | Não | Sim |
| D | Desativar o serviço de busca | Sim | **Não** |
| C | Parametrizar a consulta no servidor | **Sim** | **Sim** |

- [ ] Com **C** aplicada e o uso legítimo testado, capture: `E02_Formularios_reteste.png`.
- [ ] Aba **6 · Registrar** → preencha conclusão, limitações e outro caso (base: Q07) → situação **Concluída pelo grupo**.

## Parte 2 · INV-02 Cookies (Q08–Q12, E03, E04)

Ideia central: o servidor reconheceu a sessão, mas não conferiu se o pedido partiu de você.

- [ ] **1994 — Cookies**, modo **Benefícios**.
- [ ] **Sem o recurso**: **Reservar um material → Ir a outra página** (a reserva se perde).
- [ ] **Com o recurso**: repita (a reserva continua). Confira com a Q08.
- [ ] **Dinâmica → Disparar agora** e espere terminar.
- [ ] Com "Balcão externo" e "Alteração inesperada" na tela, capture: `E03_Cookies_incidente.png`.
- [ ] **Observar → Hipótese → Rastrear**, como na Parte 1 (base: Q09 e Q10).
- [ ] **Proteger**, na ordem A, B, C e por último D:

| Letra | Intervenção | Contém o efeito? | Mantém a função? |
|---|---|---|---|
| A | Usar apenas HttpOnly no cookie | Não | Sim |
| B | Trocar GET por POST, sem outro controle | Não | Sim |
| C | Desativar alterações de reservas | Sim | **Não** |
| D | Validar token anti-CSRF no servidor | **Sim** | **Sim** |

- [ ] Com **D** aplicada e **Testar uso legítimo** clicado, capture: `E04_Cookies_reteste.png`.
- [ ] **Registrar** (base: Q12) → **Concluída pelo grupo**.

## Parte 3 · INV-03 DOM (Q18–Q22, E05, E06)

Ideia central: o comentário foi inserido como HTML, então virou parte da página em vez de texto.

- [ ] **1998 — DOM e documentos dinâmicos**, **Benefícios**, **Com o recurso**.
- [ ] Publique dois comentários (as frases da Q18, ou troque lá pelas suas).
- [ ] **Dinâmica → Disparar agora** e espere terminar.
- [ ] Com a faixa "ESTE AVISO NÃO VEIO DA BIBLIOTECA" na tela, capture: `E05_DOM_incidente.png`.
- [ ] **Observar → Hipótese → Rastrear** (base: Q19 e Q20).
- [ ] A extensão "Simular um possível efeito de XSS" é opcional. Decida e ajuste o trecho entre colchetes na Q19 e em Limitações.
- [ ] **Proteger**, na ordem A, C, D e por último B:

| Letra | Intervenção | Contém o efeito? | Mantém os comentários? |
|---|---|---|---|
| A | Limitar comentários a 200 caracteres | Não | Sim |
| C | Adicionar somente HTTPS | Não | Sim |
| D | Desativar comentários por completo | Sim | **Não** |
| B | Inserir o comentário com textContent | **Sim** | **Sim** |

- [ ] Com **B** aplicada: **Ver o resultado e usar a aplicação** → publique um comentário novo (o da Q22).
- [ ] Capture mostrando a marcação literal e o seu comentário: `E06_DOM_reteste.png`.
- [ ] **Registrar** (base: Q22) → **Concluída pelo grupo**.

## Parte 4 · Os outros 13 marcos (sem incidente, só comparar)

Em cada um: modo **Benefícios**, compare **Sem o recurso** e **Com o recurso**, depois leia **2 · Segurança** e confira a resposta no caderno.

| Marco | O que clicar | O que deve aparecer | Questão |
|---|---|---|---|
| 1990 HTML e links | o link "Leia também…" e voltar | passa do Documento A ao B | Q01, Q02 |
| 1995 HTTPS | **Enviar pedido** nos dois modos | sem: `GET /pedido?id=42`; com: registros cifrados | Q13 |
| 1995 Java | iniciar e pausar o simulador | sem o ambiente Java o applet não executa | Q14 |
| 1995 JavaScript | quantidade 3 → **Calcular subtotal** | R$ 75,00 calculado no navegador | Q14, Q15 |
| 1996 CSS | **Trocar a folha de estilo** | muda a aparência, o conteúdo fica | Q16 |
| 1996 Flash | reproduzir a animação | sem: "Player adicional não disponível" | Q17 |
| 1999 XHR / AJAX | buscar um assunto nos dois modos | com: "Somente este resultado mudou" | Q23 |
| 2011 WebSocket | **Gerar evento no servidor** / **Consultar novamente** | com: o servidor envia sem novo pedido | Q24 |
| 2014 HTML5 | **Desenhar no canvas** | desenho feito pelo navegador, sem plug-in | Q25 |
| 2015 Service Workers | **Simular ficar offline** nos dois modos | com: cópia do cache; sem: indisponível | Q26 |
| 2017 WebAssembly | 19 + 23 nos dois modos | 42 nos dois; muda quem calculou | Q27 |
| 2019 WebAuthn | **Simular autenticação** nos dois modos | com: a chave privada não vai ao servidor | Q28 |
| 2020 Evoluir é remover | **Reproduzir a mesma função** | player legado sai, a função continua | Q29 |

- [ ] Por fim, **Mapa geral → Síntese conceitual** e releia Q30, Q31 e Q32. Reescreva a Q32 com suas palavras, mantendo entre 200 e 300.

## Parte 5 · Exportar a ficha

- [ ] **Dinâmica → Caderno de evidências**.
- [ ] Confira: as três investigações com **4 reteste(s)** ou mais e "concluída pelo grupo".
- [ ] **Exportar ficha legível (.md)**.
- [ ] Mova o arquivo baixado (`Ficha_Evolucao_WEB_AAAA-MM-DD.md`) para a pasta `Ficha/`.
- [ ] Abra-o e confirme que hipóteses, conclusões e retestes estão preenchidos (nada de "Não registrado").

## Parte 6 · Fechar o caderno

- [ ] Substitua todos os `[PREENCHER]` e `[AJUSTAR]` e apague os trechos `[Se …]` que não se aplicam.
- [ ] No fim do arquivo, troque `[ ]` por `[x]` na Conferência Final.

## Parte 7 · Gerar o PDF único

Na pasta do projeto:

```
python scripts/gerar_pdf.py
```

- [ ] O script avisa o que ainda falta. Repita até aparecer "Nada pendente".
- [ ] Abra `Entrega/Entrega_WEB.pdf` e confira as 32 respostas, as 6 imagens e a ficha em anexo.
- [ ] Envie esse PDF no Moodle.

## Conferência do que o professor pede

- [ ] PDF único
- [ ] Caderno completo: 32 respostas
- [ ] 3 investigações, com 4 intervenções em cada
- [ ] Evidências E01–E06
- [ ] Ficha exportada, aberta e conferida

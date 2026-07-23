# COD-IV — Briefing do Projeto

## 1. O que é

Site de estudo para exame de condução, desenvolvido para a Escola de Condução
Auto-Marmindo. Serve para revisão rápida de conteúdo — código da estrada e
mecânica — no estilo "simulador de exame", pensado para quem quer estudar em
pouco tempo (scroll e responde, sem precisar de ler tudo).

Nome: **COD-IV** (Código + Ivandro).

## 2. Stack técnico

| Camada | Tecnologia |
|---|---|
| Frontend | HTML / CSS / JS puro |
| Backend | Python (FastAPI), como funções serverless |
| Base de dados | PostgreSQL centralizada (via Vercel / Neon) |
| Hospedagem | Tudo no Vercel (frontend + backend + BD) |
| Referência de estilo visual | https://unc-two.vercel.app/ — layout limpo, toggle de tema claro/escuro, seleção por dropdowns, foco na função |

**Decisão importante:** Java foi descartado do stack porque o Vercel não tem
runtime nativo para Java (só Node.js, Python, Go e afins). Fica tudo em
Python + HTML/CSS/JS.

## 3. Fluxo do utilizador

1. **Cadastro** — primeiro nome + último nome + password (sem email). O
   sistema gera automaticamente um *username* interno único (não visível ao
   utilizador) para servir de chave na base de dados, já que nomes podem
   repetir-se.
2. **Login** — nome completo + password.
3. **Escolha de matéria** — Código (sinalização) ou Mecânica.
4. **Escolha do número de perguntas** — 10, 15, 20 ou 50.
5. **Temporizador** — 1,5 minutos (90 segundos) por pergunta, multiplicado
   pelo número de perguntas escolhido.

   | Nº perguntas | Tempo total |
   |---|---|
   | 10 | 15 min |
   | 15 | 22,5 min |
   | 20 | 30 min |
   | 50 | 75 min |

6. **Respostas** — o utilizador responde pergunta a pergunta; pode saltar
   (skip) uma pergunta e voltar a ela mais tarde. Se chegar ao fim sem voltar
   a uma pergunta saltada, essa pergunta conta como errada.
7. **Finalizar** — botão para terminar o quiz.
8. **Resultados** — ecrã mostra cada pergunta: se acertou ou errou; se
   errou, mostra qual era a opção certa.

## 4. Tipos de pergunta

| Tipo | Aplica-se a | Formato | Interação |
|---|---|---|---|
| **C — Reconhecimento** | Código | Imagem do sinal + 4 nomes possíveis | Clica no nome certo (escolha única) |
| **A — Afirmações com imagem** | Só Mecânica | Imagem da peça + 4 afirmações (3 certas, 1 errada) | Clica nas afirmações certas (multi-seleção, 3 de 4) |
| **B — Afirmações sem imagem** | Código e Mecânica | 3 afirmações (2 certas, 1 errada) | Clica nas afirmações certas (multi-seleção, 2 de 3) |

Regra de pontuação (a confirmar): pergunta só conta como certa se todas as
opções certas forem marcadas e nenhuma errada for selecionada.

## 5. Schema da base de dados

**`utilizadores`**
- id (PK), primeiro_nome, ultimo_nome, username (único, gerado), password_hash, criado_em

**`sinais`** (conteúdo de Código)
- id (PK), codigo, nome, categoria, subcategoria, imagem_url, descricao

**`perguntas_mecanica`**
- id (PK), pergunta, resposta_correta, categoria, imagem_url

**`quiz_perguntas`** (perguntas efetivamente usadas num quiz, geradas a partir de sinais/perguntas_mecanica)
- id (PK), tipo ("reconhecimento" / "afirmacoes_imagem" / "afirmacoes"), materia ("codigo" / "mecanica"), categoria, imagem_url, referencia_id (FK)

**`quiz_opcoes`**
- id (PK), pergunta_id (FK), texto, correta (boolean), ordem

**`quiz_sessions`**
- id (PK), utilizador_id (FK), materia, num_perguntas, tempo_total_segundos, iniciado_em, finalizado_em, status

**`quiz_respostas`**
- id (PK), quiz_session_id (FK), pergunta_id (FK), ordem, opcao_escolhida_id(s), correta, saltada

## 6. Conteúdo extraído até agora

Fonte: manuais próprios do Danilo (Guia de Sinalização Rodoviária + Manual de
Mecânica da Escola Auto-Marmindo).

- **`sinais.json`** — 464 sinais extraídos, em 23 categorias: sinais de
  perigo, cedência de passagem, proibição, obrigação, seleção/afetação de
  vias, zona, informação, pré-sinalização, direção, confirmação,
  identificação de localidades, complementares, sinalização
  turístico-cultural, marcas rodoviárias, sinalização temporária, e símbolos
  (apoio ao utente, turísticos, geográficos/ecológicos, culturais,
  desportivos, industriais).

- **`mecanica.json`** — 202 perguntas e respostas extraídas, em 14
  categorias: partes do veículo, tipos de chassi, painel/iluminação, motor,
  sistema de distribuição, sistema de travagem, sistema de arrefecimento,
  sistema de lubrificação, sistema de transmissão, suspensão, direção,
  alimentação, alimentação diesel, sistema elétrico.

## 7. Estado atual do desenvolvimento

**Concluído:**
- Extração de conteúdo dos manuais (sinais + mecânica) — 464 sinais, 202 perguntas de mecânica
- Schema da base de dados definido e implementado (SQLAlchemy + SQL)
- Backend completo: cadastro, login, iniciar quiz, responder, finalizar, resultados
- Frontend completo: autenticação, seleção de matéria/nº perguntas, quiz com temporizador e navegação (incluindo saltar pergunta), ecrã de resultados
- Perguntas Tipo C (reconhecimento de sinais) — 464 perguntas
- Perguntas Tipo B (afirmações, código e mecânica) — 464 (código) + 202 (mecânica) = 666 perguntas
- Fluxo completo testado de ponta a ponta (cadastro → login → quiz misto → responder → finalizar → resultados)

**Pendente:**
- Perguntas Tipo A (mecânica com imagem) — código pronto, mas bloqueado até haver imagens em `mecanica.json`
- Imagens dos sinais e das peças de mecânica (a fornecer pelo Danilo)
- Definir `COD_IV_ALLOWED_ORIGINS` e `COD_IV_SECRET_KEY` no Vercel antes de produção
- Deploy real no Vercel com Postgres/Neon ligado (usar connection string "pooled")

## 8. Correções aplicadas na revisão de código

- **Pool de ligações à BD em serverless** — `QueuePool` esgotava ligações do Neon entre invocações; trocado por `NullPool` + recomendação de usar a connection string "pooled" (com `-pooler` no host).
- **API deprecated do SQLAlchemy 2.0** — `Query.get()` substituído por `Session.get()`.
- **N+1 no ecrã de resultados** — 1 query por pergunta (até 50 numa sessão) substituído por 1 query única com `IN`.
- **CORS aberto (`*`)** — agora configurável via `COD_IV_ALLOWED_ORIGINS`.
- **`SECRET_KEY` insegura por omissão** — backend recusa arrancar em produção sem `COD_IV_SECRET_KEY` definida.
- **Perguntas Tipo B implementadas** — geração automática de afirmações (código: categoria do sinal; mecânica: pares pergunta/resposta reais do manual, com resposta errada trocada por outra da mesma categoria).
- **Tipo A pronto mas não corrido** — corre automaticamente assim que `mecanica.json` tiver `imagem_url` preenchido.

---
*Documento gerado como registo do estado do projeto COD-IV, para reutilização
noutras conversas ou partilha com outros colaboradores.*

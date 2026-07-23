# COD-IV

Plataforma de estudo para exame de condução (Escola de Condução Auto-Marmindo) —
código da estrada e mecânica, em formato de simulador de exame.

## Estrutura do projeto

```
cod-iv/
├── api/                     Backend Python (FastAPI)
│   ├── index.py             App principal + rotas da API
│   ├── database.py          Ligação à base de dados (Postgres/SQLite)
│   ├── models.py             Modelos SQLAlchemy
│   ├── schemas.py            Schemas Pydantic (validação)
│   ├── auth.py                Password hashing, tokens JWT, username interno
│   ├── quiz_logic.py          Seleção de perguntas e avaliação de respostas
│   ├── seed_db.py             Popula a BD a partir de data/*.json
│   └── requirements.txt
├── public/                  Frontend estático
│   ├── index.html
│   ├── css/style.css
│   └── js/app.js
├── data/                    Conteúdo extraído dos manuais
│   ├── sinais.json           464 sinais de trânsito
│   ├── mecanica.json         202 perguntas de mecânica
│   ├── build_sinais.py       Script que gerou sinais.json
│   └── build_mecanica.py     Script que gerou mecanica.json
├── sql/
│   └── schema.sql            Schema SQL de referência (Postgres)
├── docs/
│   └── COD-IV_briefing.md    Registo do estado do projeto
└── vercel.json               Configuração de deploy no Vercel
```

## Deploy no Vercel (sem instalar nada no teu computador)

Não precisas de Python nem de Node instalados no teu PC para isto — tudo
pelo browser:

1. **Cria uma conta no GitHub** (github.com) se ainda não tiveres, e cria um
   repositório novo (botão "New repository"). Podes arrastar a pasta
   `cod-iv/` inteira para dentro do repositório pela interface web do GitHub
   (upload de ficheiros).
2. **Cria uma conta no Vercel** (vercel.com) — usa "Continue with GitHub" para
   ligar automaticamente.
3. No Vercel, "Add New... → Project", escolhe o repositório que criaste.
   Deploy automático (o `vercel.json` já configura tudo).
4. No painel do projeto no Vercel, vai a **Storage → Create Database →
   Postgres (Neon)**. Isto cria a base de dados e já liga a variável
   `DATABASE_URL` automaticamente ao projeto.
5. Em **Settings → Environment Variables**, adiciona também:
   - `COD_IV_SECRET_KEY` → uma frase longa qualquer, só tu sabes (usada para
     assinar os logins)
   - `COD_IV_ADMIN_SEED_KEY` → outra password à tua escolha (só para o passo
     6, podes remover depois)
6. Depois do deploy terminar, abre no browser (uma única vez):
   ```
   https://o-teu-site.vercel.app/api/admin/seed?key=A_TUA_COD_IV_ADMIN_SEED_KEY
   ```
   com pedido **POST** — mais fácil de abrir com um "POST tester" simples ou
   com a extensão do browser que preferires; ou pede-me e explico como fazer
   com uma ferramenta gratuita. Isto popula sinais + mecânica + perguntas.
7. Pronto — o site já está no ar com a BD populada.

## Como correr localmente (opcional — só se quiseres testar no teu PC)

Precisas de Python 3.10+ instalado.

```bash
cd api
pip install -r requirements.txt

# Sem DATABASE_URL definida, usa SQLite local automaticamente
python seed_db.py          # cria a BD e popula sinais, mecânica e perguntas

uvicorn index:app --reload --port 8000
```

Agora abre **http://localhost:8000/** no browser — este único servidor serve
o site (HTML/CSS/JS) e a API ao mesmo tempo, por isso tudo funciona sem mais
configuração (login, quiz, resultados). Fica a correr no terminal; para
parar, `Ctrl+C`.

> ⚠️ Não abras `public/index.html` diretamente com duplo-clique — os pedidos
> à API (`/api/...`) não têm um servidor a responder e o login/quiz não
> funcionam. Usa sempre `http://localhost:8000/` com o `uvicorn` a correr.

## Estado atual / próximos passos

- ✅ Extração de conteúdo dos manuais (sinais + mecânica)
- ✅ Schema da base de dados
- ✅ Backend completo: cadastro, login, iniciar quiz, responder, finalizar, resultados
- ✅ Frontend completo: autenticação, seleção de matéria/nº perguntas, quiz com
  temporizador e navegação (incluindo saltar pergunta), ecrã de resultados
- ✅ Perguntas **Tipo C** (reconhecimento) — 464, geradas pelo `seed_db.py`
- ✅ Perguntas **Tipo B** (afirmações, código + mecânica) — 666, geradas pelo `seed_db.py`
- ✅ Um só comando (`uvicorn index:app`) serve frontend + backend juntos em `localhost:8000`
- ⏳ Perguntas **Tipo A** (mecânica, imagem + 4 afirmações) — código pronto em
  `seed_db.py`, mas bloqueado: nenhuma entrada de `data/mecanica.json` tem
  `imagem_url` ainda
- ⏳ Imagens dos sinais e das peças de mecânica — a fornecer, ficam em
  `public/static/sinais/` e `public/static/mecanica/` (caminhos já
  referenciados em `data/sinais.json`)
- ⏳ Definir `COD_IV_ALLOWED_ORIGINS` e `COD_IV_SECRET_KEY` no Vercel antes de produção

## Notas técnicas

- Login feito por **primeiro nome + último nome + password** (sem email).
  Como nomes podem repetir-se, o sistema gera internamente um `username`
  único (nunca mostrado ao utilizador) e, no login, testa a password contra
  todos os utilizadores com esse nome.
- Temporizador: 90 segundos (1,5 min) por pergunta × número de perguntas
  escolhido. Constante em `api/quiz_logic.py` (`TEMPO_POR_PERGUNTA_SEGUNDOS`)
  e replicada em `public/js/app.js` (`TEMPO_POR_PERGUNTA`) para o contador
  visual — mantém os dois sincronizados se alterares o valor.
- Pontuação de perguntas Tipo A/B (multi-seleção): só conta como certa se o
  conjunto de opções escolhidas for exatamente igual ao conjunto de opções
  certas (tudo ou nada).

# -*- coding: utf-8 -*-
"""
COD-IV — Gera COD-IV_briefing.pdf a partir do conteúdo do projeto.
Usa reportlab diretamente (sem depender de conversão automática de markdown)
para ter controlo total sobre a formatação.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, ListFlowable, ListItem
)
from reportlab.lib.enums import TA_LEFT

styles = getSampleStyleSheet()

titulo = ParagraphStyle("TituloCapa", parent=styles["Title"], fontSize=26, spaceAfter=6)
subtitulo = ParagraphStyle("Subtitulo", parent=styles["Normal"], fontSize=12, textColor=colors.HexColor("#555555"))
h1 = ParagraphStyle("H1", parent=styles["Heading1"], fontSize=16, spaceBefore=18, spaceAfter=8, textColor=colors.HexColor("#1a1d23"))
h2 = ParagraphStyle("H2", parent=styles["Heading2"], fontSize=13, spaceBefore=12, spaceAfter=6, textColor=colors.HexColor("#2563eb"))
corpo = ParagraphStyle("Corpo", parent=styles["Normal"], fontSize=10.3, leading=15, alignment=TA_LEFT, spaceAfter=6)
nota = ParagraphStyle("Nota", parent=styles["Normal"], fontSize=9.3, leading=13, textColor=colors.HexColor("#555555"), spaceAfter=6)

story = []

# ---------- Capa ----------
story.append(Spacer(1, 5 * cm))
story.append(Paragraph("COD-IV", titulo))
story.append(Paragraph("Briefing do Projeto — Plataforma de estudo para exame de condução", subtitulo))
story.append(Spacer(1, 0.5 * cm))
story.append(Paragraph("Escola de Condução Auto-Marmindo", subtitulo))
story.append(PageBreak())

# ---------- 1. O que é ----------
story.append(Paragraph("1. O que é", h1))
story.append(Paragraph(
    "Site de estudo para exame de condução, desenvolvido para a Escola de Condução "
    "Auto-Marmindo. Serve para revisão rápida de conteúdo — código da estrada e "
    "mecânica — no estilo \"simulador de exame\", pensado para quem quer estudar em "
    "pouco tempo (scroll e responde, sem precisar de ler tudo).", corpo))
story.append(Paragraph("Nome: <b>COD-IV</b> (Código + Ivandro).", corpo))

# ---------- 2. Stack técnico ----------
story.append(Paragraph("2. Stack técnico", h1))
stack_data = [
    ["Camada", "Tecnologia"],
    ["Frontend", "HTML / CSS / JS puro"],
    ["Backend", "Python (FastAPI), funções serverless"],
    ["Base de dados", "PostgreSQL centralizada (Vercel / Neon)"],
    ["Hospedagem", "Tudo no Vercel"],
]
t = Table(stack_data, colWidths=[4.5 * cm, 11 * cm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2563eb")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 9.5),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#dddddd")),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f5f6f8")]),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("TOPPADDING", (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ("LEFTPADDING", (0, 0), (-1, -1), 8),
]))
story.append(t)
story.append(Spacer(1, 8))
story.append(Paragraph(
    "<b>Decisão importante:</b> Java foi descartado do stack porque o Vercel não "
    "tem runtime nativo para Java (só Node.js, Python, Go e afins). Fica tudo em "
    "Python + HTML/CSS/JS.", nota))
story.append(Paragraph(
    "Referência de estilo visual: https://unc-two.vercel.app/ — layout limpo, "
    "toggle de tema claro/escuro, seleção por dropdowns, foco na função.", nota))

# ---------- 3. Fluxo do utilizador ----------
story.append(Paragraph("3. Fluxo do utilizador", h1))
fluxo_items = [
    "Cadastro — primeiro nome + último nome + password (sem email). Username interno gerado automaticamente, não visível ao utilizador.",
    "Login — nome completo + password.",
    "Escolha de matéria — Código (sinalização) ou Mecânica.",
    "Escolha do número de perguntas — 10, 15, 20 ou 50.",
    "Temporizador — 1,5 minutos (90 segundos) por pergunta × número de perguntas escolhido.",
    "Respostas — pergunta a pergunta, com opção de saltar e voltar depois. Pergunta saltada e não respondida no fim conta como errada.",
    "Finalizar — botão para terminar o quiz.",
    "Resultados — cada pergunta mostra se acertou/errou; se errou, mostra a opção certa.",
]
story.append(ListFlowable(
    [ListItem(Paragraph(item, corpo)) for item in fluxo_items],
    bulletType="1", start=1
))

tempo_data = [
    ["Nº perguntas", "Tempo total"],
    ["10", "15 min"],
    ["15", "22,5 min"],
    ["20", "30 min"],
    ["50", "75 min"],
]
t2 = Table(tempo_data, colWidths=[6 * cm, 6 * cm])
t2.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2563eb")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 9.5),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#dddddd")),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f5f6f8")]),
    ("TOPPADDING", (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
]))
story.append(Spacer(1, 6))
story.append(t2)

# ---------- 4. Tipos de pergunta ----------
story.append(Paragraph("4. Tipos de pergunta", h1))
tipos_data = [
    ["Tipo", "Aplica-se a", "Formato", "Interação"],
    ["C — Reconhecimento", "Código", "Imagem do sinal + 4 nomes possíveis", "Clica no nome certo (escolha única)"],
    ["A — Afirmações c/ imagem", "Só Mecânica", "Imagem da peça + 4 afirmações (3 certas, 1 errada)", "Clica nas afirmações certas (3 de 4)"],
    ["B — Afirmações s/ imagem", "Código e Mecânica", "3 afirmações (2 certas, 1 errada)", "Clica nas afirmações certas (2 de 3)"],
]
t3 = Table(tipos_data, colWidths=[3.6 * cm, 3 * cm, 5.5 * cm, 3.4 * cm])
t3.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2563eb")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 8.5),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#dddddd")),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f5f6f8")]),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("TOPPADDING", (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
]))
story.append(t3)
story.append(Spacer(1, 8))
story.append(Paragraph(
    "Regra de pontuação: pergunta só conta como certa se todas as opções certas "
    "forem marcadas e nenhuma errada for selecionada (tudo ou nada).", nota))

story.append(PageBreak())

# ---------- 5. Schema da base de dados ----------
story.append(Paragraph("5. Schema da base de dados", h1))
tabelas = [
    ("utilizadores", "id (PK), primeiro_nome, ultimo_nome, username (único, gerado), password_hash, criado_em"),
    ("sinais", "id (PK), codigo, nome, categoria, subcategoria, imagem_url, descricao"),
    ("perguntas_mecanica", "id (PK), pergunta, resposta_correta, categoria, imagem_url"),
    ("quiz_perguntas", "id (PK), tipo, materia, categoria, enunciado, imagem_url, referencia_id (FK)"),
    ("quiz_opcoes", "id (PK), pergunta_id (FK), texto, correta (boolean), ordem"),
    ("quiz_sessions", "id (PK), utilizador_id (FK), materia, num_perguntas, tempo_total_segundos, iniciado_em, finalizado_em, status"),
    ("quiz_respostas", "id (PK), quiz_session_id (FK), pergunta_id (FK), ordem, opcoes_escolhidas, correta, saltada"),
]
for nome_tabela, campos in tabelas:
    story.append(Paragraph(nome_tabela, h2))
    story.append(Paragraph(campos, corpo))

# ---------- 6. Conteúdo extraído ----------
story.append(Paragraph("6. Conteúdo extraído", h1))
story.append(Paragraph(
    "Fonte: manuais próprios do Danilo (Guia de Sinalização Rodoviária + Manual "
    "de Mecânica da Escola Auto-Marmindo).", corpo))
story.append(Paragraph(
    "<b>sinais.json</b> — 464 sinais extraídos, em 23 categorias: sinais de "
    "perigo, cedência de passagem, proibição, obrigação, seleção/afetação de "
    "vias, zona, informação, pré-sinalização, direção, confirmação, "
    "identificação de localidades, complementares, sinalização "
    "turístico-cultural, marcas rodoviárias, sinalização temporária, e símbolos "
    "(apoio ao utente, turísticos, geográficos/ecológicos, culturais, "
    "desportivos, industriais).", corpo))
story.append(Paragraph(
    "<b>mecanica.json</b> — 202 perguntas e respostas extraídas, em 14 "
    "categorias: partes do veículo, tipos de chassi, painel/iluminação, motor, "
    "sistema de distribuição, sistema de travagem, sistema de arrefecimento, "
    "sistema de lubrificação, sistema de transmissão, suspensão, direção, "
    "alimentação, alimentação diesel, sistema elétrico.", corpo))

# ---------- 7. Estado atual ----------
story.append(Paragraph("7. Estado atual do desenvolvimento", h1))
feito = [
    "Extração de conteúdo dos manuais (sinais + mecânica) — 464 sinais, 202 perguntas de mecânica",
    "Schema da base de dados definido e implementado (SQLAlchemy + SQL)",
    "Backend completo: cadastro, login, iniciar quiz, responder, finalizar, resultados",
    "Frontend completo: autenticação, seleção de matéria/nº perguntas, quiz com temporizador e navegação (incluindo saltar pergunta), ecrã de resultados",
    "Perguntas Tipo C (reconhecimento de sinais) geradas automaticamente — 464 perguntas",
    "Perguntas Tipo B (afirmações, código e mecânica) geradas automaticamente — 464 (código) + 202 (mecânica) = 666 perguntas",
    "Fluxo completo testado de ponta a ponta (cadastro → login → quiz misto código/mecânica → responder → finalizar → resultados) com sucesso",
]
story.append(Paragraph("Concluído:", h2))
story.append(ListFlowable(
    [ListItem(Paragraph(item, corpo)) for item in feito],
    bulletType="bullet"
))

pendente = [
    "Perguntas Tipo A (mecânica com imagem) — código já pronto, mas bloqueado: nenhuma das 202 entradas de mecanica.json tem imagem ainda",
    "Imagens dos sinais e das peças de mecânica — a fornecer pelo Danilo",
    "Definir COD_IV_ALLOWED_ORIGINS e COD_IV_SECRET_KEY nas env vars do Vercel antes de produção (ver secção 8)",
    "Deploy real no Vercel com Postgres/Neon ligado (usar connection string 'pooled', com -pooler no host)",
]
story.append(Paragraph("Pendente:", h2))
story.append(ListFlowable(
    [ListItem(Paragraph(item, corpo)) for item in pendente],
    bulletType="bullet"
))

# ---------- 8. Correções aplicadas na revisão de código ----------
story.append(PageBreak())
story.append(Paragraph("8. Correções aplicadas na revisão de código", h1))
story.append(Paragraph(
    "Revisão completa do projeto (backend, frontend, schema e dados) com as "
    "seguintes correções aplicadas e testadas:", corpo))
correcoes = [
    "<b>Pool de ligações à BD em serverless</b> — o engine SQLAlchemy usava pool "
    "normal (QueuePool), que em funções serverless da Vercel esgota rapidamente "
    "o limite de ligações do Neon. Corrigido para NullPool + recomendação de "
    "usar a connection string \"pooled\" do Neon (com -pooler no host).",
    "<b>API deprecated do SQLAlchemy 2.0</b> — vários pontos usavam "
    "Query.get(), que está descontinuado. Substituído por Session.get().",
    "<b>Problema N+1 no ecrã de resultados</b> — o cálculo de resultados fazia "
    "uma query à BD por cada pergunta respondida (até 50 queries para um quiz "
    "de 50 perguntas). Corrigido para uma única query com IN.",
    "<b>CORS aberto a qualquer domínio</b> — passou a ser configurável via env "
    "var COD_IV_ALLOWED_ORIGINS, em vez de \"*\" fixo no código.",
    "<b>Chave secreta (JWT) por omissão</b> — o backend recusa arrancar em "
    "produção (VERCEL_ENV=production) se a env var COD_IV_SECRET_KEY não for "
    "definida, evitando assinar tokens com uma chave previsível.",
    "<b>Perguntas Tipo B implementadas</b> — geração automática de afirmações "
    "para código (categoria do sinal, certa/errada) e mecânica (par "
    "pergunta/resposta do manual, com a resposta errada vinda de outra "
    "pergunta da mesma categoria — distrator plausível sem inventar conteúdo).",
    "<b>Tipo A deixado pronto mas não corrido</b> — a função existe e corre "
    "automaticamente assim que mecanica.json tiver imagem_url preenchido; "
    "por agora está a 0/202 imagens, por isso não gera nada ainda.",
]
story.append(ListFlowable(
    [ListItem(Paragraph(item, corpo)) for item in correcoes],
    bulletType="bullet"
))

story.append(Spacer(1, 20))
story.append(Paragraph(
    "Documento gerado como registo do estado do projeto COD-IV, para reutilização "
    "noutras conversas ou partilha com outros colaboradores.", nota))

doc = SimpleDocTemplate(
    "/home/claude/cod-iv/docs/COD-IV_briefing.pdf",
    pagesize=A4,
    topMargin=2 * cm, bottomMargin=2 * cm, leftMargin=2 * cm, rightMargin=2 * cm,
)
doc.build(story)
print("PDF gerado com sucesso.")

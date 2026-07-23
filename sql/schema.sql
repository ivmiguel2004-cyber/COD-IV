-- COD-IV — Schema da base de dados (PostgreSQL)

CREATE TABLE IF NOT EXISTS utilizadores (
    id SERIAL PRIMARY KEY,
    primeiro_nome VARCHAR(80) NOT NULL,
    ultimo_nome VARCHAR(80) NOT NULL,
    username VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    criado_em TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS sinais (
    id SERIAL PRIMARY KEY,
    codigo VARCHAR(20) NOT NULL,
    nome VARCHAR(200) NOT NULL,
    categoria VARCHAR(80) NOT NULL,
    subcategoria VARCHAR(80),
    imagem_url VARCHAR(255),
    descricao TEXT
);

CREATE TABLE IF NOT EXISTS perguntas_mecanica (
    id SERIAL PRIMARY KEY,
    pergunta TEXT NOT NULL,
    resposta_correta TEXT NOT NULL,
    categoria VARCHAR(80) NOT NULL,
    imagem_url VARCHAR(255)
);

-- Perguntas efetivamente geradas para uso em quizzes
CREATE TABLE IF NOT EXISTS quiz_perguntas (
    id SERIAL PRIMARY KEY,
    tipo VARCHAR(30) NOT NULL CHECK (tipo IN ('reconhecimento', 'afirmacoes_imagem', 'afirmacoes')),
    materia VARCHAR(20) NOT NULL CHECK (materia IN ('codigo', 'mecanica')),
    categoria VARCHAR(80),
    enunciado TEXT,
    imagem_url VARCHAR(255),
    referencia_id INTEGER
);

CREATE TABLE IF NOT EXISTS quiz_opcoes (
    id SERIAL PRIMARY KEY,
    pergunta_id INTEGER NOT NULL REFERENCES quiz_perguntas(id) ON DELETE CASCADE,
    texto TEXT NOT NULL,
    correta BOOLEAN NOT NULL DEFAULT FALSE,
    ordem INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS quiz_sessions (
    id SERIAL PRIMARY KEY,
    utilizador_id INTEGER NOT NULL REFERENCES utilizadores(id) ON DELETE CASCADE,
    materia VARCHAR(20) NOT NULL CHECK (materia IN ('codigo', 'mecanica')),
    num_perguntas INTEGER NOT NULL,
    tempo_total_segundos INTEGER NOT NULL,
    iniciado_em TIMESTAMP NOT NULL DEFAULT NOW(),
    finalizado_em TIMESTAMP,
    status VARCHAR(20) NOT NULL DEFAULT 'em_progresso' CHECK (status IN ('em_progresso', 'finalizado'))
);

CREATE TABLE IF NOT EXISTS quiz_respostas (
    id SERIAL PRIMARY KEY,
    quiz_session_id INTEGER NOT NULL REFERENCES quiz_sessions(id) ON DELETE CASCADE,
    pergunta_id INTEGER NOT NULL REFERENCES quiz_perguntas(id),
    ordem INTEGER NOT NULL,
    opcoes_escolhidas INTEGER[] DEFAULT '{}',   -- ids das quiz_opcoes marcadas pelo utilizador
    correta BOOLEAN,
    saltada BOOLEAN NOT NULL DEFAULT FALSE,
    respondida_em TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_sinais_categoria ON sinais(categoria);
CREATE INDEX IF NOT EXISTS idx_mecanica_categoria ON perguntas_mecanica(categoria);
CREATE INDEX IF NOT EXISTS idx_quiz_respostas_session ON quiz_respostas(quiz_session_id);

// COD-IV — Frontend logic
"use strict";

const API_BASE = "/api";

// ---------- Estado global ----------
const state = {
  token: localStorage.getItem("cod_iv_token") || null,
  utilizador: JSON.parse(localStorage.getItem("cod_iv_user") || "null"),
  materiaEscolhida: null,
  numPerguntasEscolhido: null,
  quizSession: null,      // { id, materia, num_perguntas, tempo_total_segundos, perguntas: [...] }
  respostasLocais: {},    // pergunta_id -> { opcoes: [ids], saltada: bool, respondida: bool }
  indiceAtual: 0,
  timerInterval: null,
  segundosRestantes: 0,
};

// ---------- Helpers de DOM ----------
const $ = (sel) => document.querySelector(sel);
const $$ = (sel) => Array.from(document.querySelectorAll(sel));

function mostrarView(id) {
  $$(".view").forEach((v) => v.classList.add("hidden"));
  $(`#${id}`).classList.remove("hidden");
}

async function apiFetch(path, options = {}) {
  const headers = options.headers || {};
  headers["Content-Type"] = "application/json";
  if (state.token) headers["Authorization"] = `Bearer ${state.token}`;

  const resp = await fetch(`${API_BASE}${path}`, { ...options, headers });
  const data = await resp.json().catch(() => ({}));
  if (!resp.ok) {
    throw new Error(data.detail || "Ocorreu um erro. Tenta novamente.");
  }
  return data;
}

// ---------- Tema ----------
function initTheme() {
  const saved = localStorage.getItem("cod_iv_theme") || "light";
  document.documentElement.setAttribute("data-theme", saved);
  $("#btn-theme").textContent = saved === "dark" ? "☀️" : "🌙";
}

$("#btn-theme").addEventListener("click", () => {
  const atual = document.documentElement.getAttribute("data-theme");
  const novo = atual === "dark" ? "light" : "dark";
  document.documentElement.setAttribute("data-theme", novo);
  localStorage.setItem("cod_iv_theme", novo);
  $("#btn-theme").textContent = novo === "dark" ? "☀️" : "🌙";
});

// ---------- Autenticação ----------
$$(".tab-btn").forEach((btn) => {
  btn.addEventListener("click", () => {
    $$(".tab-btn").forEach((b) => b.classList.remove("active"));
    $$(".tab-panel").forEach((p) => p.classList.remove("active"));
    btn.classList.add("active");
    $(`#form-${btn.dataset.tab}`).classList.add("active");
  });
});

$("#form-login").addEventListener("submit", async (e) => {
  e.preventDefault();
  const form = e.target;
  const errorEl = $("#login-error");
  errorEl.textContent = "";

  const nomeCompleto = form.nome_completo.value.trim().replace(/\s+/g, " ");
  const partes = nomeCompleto.split(" ");
  if (partes.length < 2) {
    errorEl.textContent = "Escreve o nome completo (primeiro nome e último nome).";
    return;
  }
  const primeiro_nome = partes[0];
  const ultimo_nome = partes.slice(1).join(" ");

  try {
    const data = await apiFetch("/login", {
      method: "POST",
      body: JSON.stringify({ primeiro_nome, ultimo_nome, password: form.password.value }),
    });
    autenticarSucesso(data);
  } catch (err) {
    errorEl.textContent = err.message;
  }
});

$("#form-cadastro").addEventListener("submit", async (e) => {
  e.preventDefault();
  const form = e.target;
  const errorEl = $("#cadastro-error");
  errorEl.textContent = "";
  try {
    const data = await apiFetch("/cadastro", {
      method: "POST",
      body: JSON.stringify({
        primeiro_nome: form.primeiro_nome.value.trim(),
        ultimo_nome: form.ultimo_nome.value.trim(),
        password: form.password.value,
      }),
    });
    autenticarSucesso(data);
  } catch (err) {
    errorEl.textContent = err.message;
  }
});

function autenticarSucesso(data) {
  state.token = data.token;
  state.utilizador = data.utilizador;
  localStorage.setItem("cod_iv_token", state.token);
  localStorage.setItem("cod_iv_user", JSON.stringify(state.utilizador));
  atualizarTopbar();
  irParaConfig();
}

$("#btn-logout").addEventListener("click", () => {
  state.token = null;
  state.utilizador = null;
  localStorage.removeItem("cod_iv_token");
  localStorage.removeItem("cod_iv_user");
  atualizarTopbar();
  mostrarView("view-auth");
});

function atualizarTopbar() {
  const logado = !!state.token;
  $("#btn-logout").classList.toggle("hidden", !logado);
  const greeting = $("#user-greeting");
  if (logado) {
    greeting.textContent = `Olá, ${state.utilizador.primeiro_nome}`;
    greeting.classList.remove("hidden");
  } else {
    greeting.classList.add("hidden");
  }
}

// ---------- Seleção de matéria / nº perguntas ----------
function irParaConfig() {
  state.materiaEscolhida = null;
  state.numPerguntasEscolhido = null;
  $$(".materia-btn").forEach((b) => b.classList.remove("selected"));
  $$(".num-btn").forEach((b) => b.classList.remove("selected"));
  $("#num-perguntas-wrap").classList.add("hidden");
  $("#btn-iniciar-quiz").disabled = true;
  $("#config-error").textContent = "";
  mostrarView("view-config");
}

$$(".materia-btn").forEach((btn) => {
  btn.addEventListener("click", () => {
    $$(".materia-btn").forEach((b) => b.classList.remove("selected"));
    btn.classList.add("selected");
    state.materiaEscolhida = btn.dataset.materia;
    $("#num-perguntas-wrap").classList.remove("hidden");
  });
});

const TEMPO_POR_PERGUNTA = 90; // 1.5 min, deve refletir o backend

$$(".num-btn").forEach((btn) => {
  btn.addEventListener("click", () => {
    $$(".num-btn").forEach((b) => b.classList.remove("selected"));
    btn.classList.add("selected");
    state.numPerguntasEscolhido = parseInt(btn.dataset.num, 10);
    const totalSeg = state.numPerguntasEscolhido * TEMPO_POR_PERGUNTA;
    const min = Math.floor(totalSeg / 60);
    const seg = totalSeg % 60;
    $("#tempo-info").textContent = `Tempo total: ${min}${seg ? `:${String(seg).padStart(2, "0")}` : " min"}`;
    $("#btn-iniciar-quiz").disabled = false;
  });
});

$("#btn-iniciar-quiz").addEventListener("click", async () => {
  const errorEl = $("#config-error");
  errorEl.textContent = "";
  try {
    const session = await apiFetch("/quiz/iniciar", {
      method: "POST",
      body: JSON.stringify({
        materia: state.materiaEscolhida,
        num_perguntas: state.numPerguntasEscolhido,
      }),
    });
    iniciarQuizUI(session);
  } catch (err) {
    errorEl.textContent = err.message;
  }
});

// ---------- Quiz ----------
function iniciarQuizUI(session) {
  state.quizSession = session;
  state.respostasLocais = {};
  session.perguntas.forEach((p) => {
    state.respostasLocais[p.id] = { opcoes: [], saltada: false, respondida: false };
  });
  state.indiceAtual = 0;
  state.segundosRestantes = session.tempo_total_segundos;

  construirMapaPerguntas();
  renderizarPergunta();
  iniciarTimer();
  mostrarView("view-quiz");
}

function iniciarTimer() {
  clearInterval(state.timerInterval);
  atualizarTimerUI();
  state.timerInterval = setInterval(() => {
    state.segundosRestantes--;
    atualizarTimerUI();
    if (state.segundosRestantes <= 0) {
      clearInterval(state.timerInterval);
      finalizarQuiz();
    }
  }, 1000);
}

function atualizarTimerUI() {
  const min = Math.floor(state.segundosRestantes / 60);
  const seg = state.segundosRestantes % 60;
  const el = $("#quiz-timer");
  el.textContent = `${min}:${String(seg).padStart(2, "0")}`;
  el.classList.toggle("timer-warning", state.segundosRestantes <= 60);
}

function construirMapaPerguntas() {
  const mapa = $("#quiz-mapa");
  mapa.innerHTML = "";
  state.quizSession.perguntas.forEach((p, i) => {
    const item = document.createElement("button");
    item.className = "mapa-item";
    item.textContent = i + 1;
    item.addEventListener("click", () => {
      state.indiceAtual = i;
      renderizarPergunta();
    });
    mapa.appendChild(item);
  });
  atualizarMapa();
}

function atualizarMapa() {
  const itens = $$(".mapa-item");
  state.quizSession.perguntas.forEach((p, i) => {
    const r = state.respostasLocais[p.id];
    const item = itens[i];
    item.classList.remove("atual", "respondida", "saltada");
    if (i === state.indiceAtual) item.classList.add("atual");
    else if (r.saltada) item.classList.add("saltada");
    else if (r.respondida) item.classList.add("respondida");
  });
}

function renderizarPergunta() {
  const pergunta = state.quizSession.perguntas[state.indiceAtual];
  const resposta = state.respostasLocais[pergunta.id];

  $("#quiz-progress-text").textContent =
    `Pergunta ${state.indiceAtual + 1} de ${state.quizSession.perguntas.length}`;
  $("#progress-fill").style.width =
    `${((state.indiceAtual + 1) / state.quizSession.perguntas.length) * 100}%`;

  $("#quiz-enunciado").textContent = pergunta.enunciado || "";

  const img = $("#quiz-imagem");
  if (pergunta.imagem_url) {
    img.src = pergunta.imagem_url;
    img.classList.remove("hidden");
  } else {
    img.classList.add("hidden");
  }

  const multiSelect = pergunta.tipo !== "reconhecimento" && pergunta.tipo !== "fotografia";

  const opcoesWrap = $("#quiz-opcoes");
  opcoesWrap.innerHTML = "";
  pergunta.opcoes.forEach((opcao) => {
    const btn = document.createElement("button");
    btn.className = "opcao-btn";
    btn.type = "button";
    const selecionada = resposta.opcoes.includes(opcao.id);
    if (selecionada) btn.classList.add("selecionada");

    const marcador = document.createElement("span");
    marcador.className = "opcao-marcador";
    marcador.textContent = selecionada ? "✓" : "";
    btn.appendChild(marcador);

    const texto = document.createElement("span");
    texto.textContent = opcao.texto;
    btn.appendChild(texto);

    btn.addEventListener("click", () => {
      if (multiSelect) {
        toggleOpcaoMultipla(pergunta.id, opcao.id);
      } else {
        selecionarOpcaoUnica(pergunta.id, opcao.id);
      }
      renderizarPergunta();
    });

    opcoesWrap.appendChild(btn);
  });

  $("#btn-anterior").disabled = state.indiceAtual === 0;
  const ultimaPergunta = state.indiceAtual === state.quizSession.perguntas.length - 1;
  $("#btn-seguinte").classList.toggle("hidden", ultimaPergunta);
  $("#btn-finalizar").classList.toggle("hidden", !ultimaPergunta);

  atualizarMapa();
}

function selecionarOpcaoUnica(perguntaId, opcaoId) {
  const r = state.respostasLocais[perguntaId];
  r.opcoes = [opcaoId];
  r.saltada = false;
  r.respondida = true;
  enviarResposta(perguntaId);
}

function toggleOpcaoMultipla(perguntaId, opcaoId) {
  const r = state.respostasLocais[perguntaId];
  if (r.opcoes.includes(opcaoId)) {
    r.opcoes = r.opcoes.filter((id) => id !== opcaoId);
  } else {
    r.opcoes.push(opcaoId);
  }
  r.saltada = false;
  r.respondida = r.opcoes.length > 0;
  enviarResposta(perguntaId);
}

async function enviarResposta(perguntaId) {
  const r = state.respostasLocais[perguntaId];
  try {
    await apiFetch(`/quiz/responder?quiz_session_id=${state.quizSession.id}`, {
      method: "POST",
      body: JSON.stringify({
        pergunta_id: perguntaId,
        opcoes_escolhidas: r.opcoes,
        saltada: r.saltada,
      }),
    });
  } catch (err) {
    console.error("Erro ao guardar resposta:", err);
  }
}

$("#btn-anterior").addEventListener("click", () => {
  if (state.indiceAtual > 0) {
    state.indiceAtual--;
    renderizarPergunta();
  }
});

$("#btn-seguinte").addEventListener("click", () => {
  if (state.indiceAtual < state.quizSession.perguntas.length - 1) {
    state.indiceAtual++;
    renderizarPergunta();
  }
});

$("#btn-saltar").addEventListener("click", () => {
  const pergunta = state.quizSession.perguntas[state.indiceAtual];
  const r = state.respostasLocais[pergunta.id];
  // Só marca como saltada se ainda não tiver sido respondida
  if (!r.respondida) {
    r.saltada = true;
    enviarResposta(pergunta.id);
  }
  if (state.indiceAtual < state.quizSession.perguntas.length - 1) {
    state.indiceAtual++;
  }
  renderizarPergunta();
});

$("#btn-finalizar").addEventListener("click", () => {
  finalizarQuiz();
});

async function finalizarQuiz() {
  clearInterval(state.timerInterval);
  try {
    const resultado = await apiFetch(`/quiz/${state.quizSession.id}/finalizar`, {
      method: "POST",
    });
    renderizarResultados(resultado);
    mostrarView("view-resultados");
  } catch (err) {
    alert("Não foi possível finalizar o quiz: " + err.message);
  }
}

// ---------- Resultados ----------
function renderizarResultados(resultado) {
  $("#score-certas").textContent = resultado.total_certas;
  $("#score-erradas").textContent = resultado.total_erradas;

  const lista = $("#lista-resultados");
  lista.innerHTML = "";

  resultado.respostas.forEach((r, i) => {
    const item = document.createElement("div");
    item.className = `resultado-item ${r.correta ? "item-correto" : "item-errado"}`;

    const badge = document.createElement("span");
    badge.className = "resultado-badge";
    badge.textContent = r.saltada ? "Saltada / Errada" : r.correta ? "Acertou" : "Errou";
    item.appendChild(badge);

    const enunciado = document.createElement("p");
    enunciado.className = "resultado-enunciado";
    enunciado.textContent = `${i + 1}. ${r.enunciado || ""}`;
    item.appendChild(enunciado);

    if (r.imagem_url) {
      const img = document.createElement("img");
      img.className = "resultado-imagem";
      img.src = r.imagem_url;
      item.appendChild(img);
    }

    r.opcoes.forEach((opcao) => {
      const div = document.createElement("div");
      div.className = "resultado-opcao";
      const ehCorreta = r.opcoes_corretas_ids.includes(opcao.id);
      const foiEscolhidaErrada =
        r.opcoes_escolhidas_ids.includes(opcao.id) && !ehCorreta;
      if (ehCorreta) div.classList.add("op-correta");
      if (foiEscolhidaErrada) div.classList.add("op-escolhida-errada");
      div.textContent = opcao.texto;
      item.appendChild(div);
    });

    lista.appendChild(item);
  });
}

$("#btn-novo-quiz").addEventListener("click", () => {
  irParaConfig();
});

// ---------- Feedback ----------
$("#form-feedback").addEventListener("submit", async (e) => {
  e.preventDefault();
  const form = e.target;
  const mensagem = form.mensagem.value.trim();
  const status = $("#feedback-status");
  status.textContent = "";
  try {
    const data = await apiFetch("/feedback", {
      method: "POST",
      body: JSON.stringify({ mensagem }),
    });
    status.textContent = data.mensagem;
    status.className = "form-success";
    form.reset();
  } catch (err) {
    status.textContent = err.message;
    status.className = "form-error";
  }
});

// ---------- Arranque ----------
function init() {
  initTheme();
  atualizarTopbar();
  if (state.token) {
    irParaConfig();
  } else {
    mostrarView("view-auth");
  }
}

init();

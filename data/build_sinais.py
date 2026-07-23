"""
COD-IV - Extração de dados do "Guia de Sinalização Rodoviária"
Gera data/sinais.json com todos os sinais organizados por categoria.
"""
import json

sinais = []

def add(codigo, nome, categoria, subcategoria=None, descricao=None):
    sinais.append({
        "codigo": codigo,
        "nome": nome,
        "categoria": categoria,
        "subcategoria": subcategoria,
        "imagem_url": f"/static/sinais/{codigo.replace(' ', '_')}.png",
        "descricao": descricao
    })

# ---------- SÍMBOLOS - I. Apoio ao utente - 1. Emergência ----------
emergencia = [
    ("1.1", "Hospital"), ("1.2", "Hospital com urgência médica"),
    ("1.3", "Posto de socorros"), ("1.4", "Farmácia"),
    ("1.5", "Bombeiros"), ("1.6", "GNR"), ("1.7", "PSP"), ("1.8", "Oficina"),
    ("1.9", "Posto de combustível com GPL"), ("1.10", "Posto de combustível"),
    ("1.11", "Telefone"),
]
for cod, nome in emergencia:
    add(cod, nome, "simbolos_apoio_utente", "emergencia")

# ---------- SÍMBOLOS - I. Apoio ao utente - 2. Outras indicações ----------
outras_indicacoes = [
    ("2.1", "Parque de estacionamento"), ("2.1A", "Parque de estacionamento com cobertura"),
    ("2.2", "Igreja / santuário"), ("2.3", "Cemitério"), ("2.4", "Mercado"),
    ("2.5", "Escola"), ("2.6", "Correios"), ("2.7", "Centro"),
    ("2.8", "Zona pedonal"), ("2.9", "Bairro"), ("2.10", "Metro"),
    ("2.11", "Estação ferroviária"), ("2.12", "Estação rodoviária"),
    ("2.13", "Táxis"), ("2.14", "Aluguer de viaturas"), ("2.15", "Ferry-boat"),
    ("2.16", "Cais de embarque"), ("2.17", "Porto"), ("2.18", "Aeroporto / aeródromo"),
    ("2.19", "Heliporto"), ("2.20", "Município"), ("2.21", "Auto-estrada"),
    ("2.22", "Deficiente"), ("2.23", "Passagem desnivelada para peões com rampa"),
    ("2.24", "Passagem desnivelada para peões com escada"), ("2.25", "Sanitários"),
    ("2.25A", "Sanitários"), ("2.26", "Centro de inspecções"),
    ("2.27", "Via reservada a automóveis e motociclos"), ("2.28", "Fontanário"),
]
for cod, nome in outras_indicacoes:
    add(cod, nome, "simbolos_apoio_utente", "outras_indicacoes")

# ---------- SÍMBOLOS - II. Indicações turísticas ----------
turisticas = [
    ("II-1", "Parque de campismo/ caravanismo"), ("II-2", "Parque de campismo"),
    ("II-3", "Parque de caravanismo"), ("II-4", "Pousada/estalagem"),
    ("II-5", "Albergue"), ("II-6", "Pousada de juventude"),
    ("II-7", "Hotel / motel/ residencial"), ("II-8", "Posto de informações"),
    ("II-9", "Restaurante"), ("II-10", "Bar"), ("II-11", "Zoo"),
    ("II-12", "Turismo Rural"), ("II-13", "Termas"), ("II-14", "Aquário"),
    ("II-15", "Artesanato"), ("II-16", "Praça de touros"),
    ("II-17", "Alojamento particular"), ("II-18", "Marina"), ("II-19", "Cabo"),
    ("II-20", "Casino"), ("II-21", "Centro de exposições"),
]
for cod, nome in turisticas:
    add(cod, nome, "simbolos_turisticos")

# ---------- SÍMBOLOS - III. Indicações geográficas e ecológicas ----------
geograficas = [
    ("III-1", "Rio/lago/albufeira"), ("III-2", "Serra"), ("III-3", "Gruta"),
    ("III-4", "Parque/jardim"), ("III-5", "Praia"), ("III-6", "Pinhal"),
    ("III-7", "Parque de merendas"), ("III-8", "Percursos pedestres"),
    ("III-9", "Miradouro/ponto de vista"), ("III-10", "Zona agrícola"),
    ("III-11", "Zona vinícola"), ("III-12", "Área protegida/ parque natural/reserva natural"),
    ("III-13", "Parque nacional"),
]
for cod, nome in geograficas:
    add(cod, nome, "simbolos_geograficos_ecologicos")

# ---------- SÍMBOLOS - IV. Indicações culturais ----------
culturais = [
    ("IV-1", "Monumento / castelo"), ("IV-2", "Museu"), ("IV-3", "Biblioteca"),
    ("IV-4", "Ruínas"), ("IV-5", "Monumento pré-histórico"), ("IV-6", "Teatro"),
    ("IV-7", "Património mundial"), ("IV-8", "Aldeia preservada"),
    ("IV-9", "Pelourinho/cruzeiro"), ("IV-10", "Ponte"), ("IV-11", "Solar"),
    ("IV-12", "Aldeia histórica"),
]
for cod, nome in culturais:
    add(cod, nome, "simbolos_culturais")

# ---------- SÍMBOLOS - V. Indicações desportivas ----------
desportivas = [
    ("V-1", "Vela"), ("V-2", "Estádio"), ("V-3", "Hipódromo"), ("V-4", "Campo de golfe"),
    ("V-5", "Autódromo"), ("V-6", "Ténis"), ("V-7", "Piscina"), ("V-8", "Pesca desportiva"),
    ("V-9", "Centro desportivo"), ("V-10", "Campo de tiro"), ("V-11", "Ski"),
    ("V-12", "Parque aquático"), ("V-13", "Kartódromo"), ("V-14", "Centro hípico"),
    ("V-15", "Remo"), ("V-16", "Montanhismo"), ("V-17", "Windsurf"), ("V-18", "Caça"),
    ("V-19", "Motonáutica"), ("V-20", "Canoagem"), ("V-21", "Atletismo"),
]
for cod, nome in desportivas:
    add(cod, nome, "simbolos_desportivos")

# ---------- SÍMBOLOS - VI. Indicações industriais ----------
industriais = [
    ("VI-1", "Fábrica / zona industrial"), ("VI-2", "Indústria pesqueira"),
    ("VI-3", "Terminal rodoviário de pesados"), ("VI-4", "Coudelaria nacional"),
]
for cod, nome in industriais:
    add(cod, nome, "simbolos_industriais")

# ---------- SINAIS DE PERIGO (A) ----------
perigo = [
    ("A1a", "Curva à direita"), ("A1b", "Curva à esquerda"),
    ("A1c", "Curva à direita e contracurva"), ("A1d", "Curva à esquerda e contracurva"),
    ("A2a", "Lomba"), ("A2b", "Depressão"), ("A2c", "Lomba ou depressão"),
    ("A3a", "Descida perigosa"), ("A3b", "Subida de inclinação acentuada"),
    ("A4a", "Passagem estreita"), ("A4b", "Passagem estreita"), ("A4c", "Passagem estreita"),
    ("A5", "Pavimento escorregadio"), ("A6", "Projecção de gravilha"),
    ("A7a", "Bermas baixas"), ("A7b", "Bermas baixas"),
    ("A8", "Saída num cais ou precipício"), ("A9", "Queda de pedras"),
    ("A10", "Ponte móvel"), ("A11", "Neve ou gelo"), ("A12", "Vento lateral"),
    ("A13", "Visibilidade insuficiente"), ("A14", "Crianças"), ("A15", "Idosos"),
    ("A16a", "Passagem de peões"), ("A16b", "Travessia de peões"),
    ("A17", "Saída de ciclistas"), ("A18", "Cavaleiros"), ("A19a", "Animais"),
    ("A19b", "Animais selvagens"), ("A20", "Túnel"), ("A21", "Pista de aviação"),
    ("A22", "Sinalização luminosa"), ("A23", "Trabalhos na via"),
    ("A24", "Cruzamento ou entroncamento"), ("A25", "Trânsito nos dois sentidos"),
    ("A26", "Passagem de nível com guarda"), ("A27", "Passagem de nível sem guarda"),
    ("A28", "Intersecção com via onde circulam veículos sobre carris"),
    ("A29", "Outros perigos"), ("A30", "Congestionamento"), ("A31", "Obstrução da via"),
    ("A32a", "Local de passagem de nível sem guarda"),
    ("A32b", "Local de passagem de nível sem guarda com duas ou mais vias"),
]
for cod, nome in perigo:
    add(cod, nome, "sinais_perigo")

# ---------- SINAIS DE CEDÊNCIA DE PASSAGEM (B) ----------
cedencia = [
    ("B1", "Cedência de passagem"), ("B2", "Paragem obrigatória em cruzamentos ou entroncamentos"),
    ("B3", "Via com prioridade"), ("B4", "Fim de via com prioridade"),
    ("B5", "Cedência de passagem nos estreitamentos da faixa de rodagem"),
    ("B6", "Prioridade nos estreitamentos da faixa de rodagem"),
    ("B7", "Aproximação de rotunda"), ("B8", "Cruzamento com via sem prioridade"),
    ("B9a", "Entroncamento com via sem prioridade"), ("B9b", "Entroncamento com via sem prioridade"),
    ("B9c", "Entroncamento com via sem prioridade"), ("B9d", "Entroncamento com via sem prioridade"),
]
for cod, nome in cedencia:
    add(cod, nome, "sinais_cedencia_passagem")

# ---------- SINAIS DE PROIBIÇÃO (C) ----------
proibicao = [
    ("C1", "Sentido proibido"), ("C2", "Trânsito proibido"),
    ("C3a", "Trânsito proibido a automóveis e motociclos com carro"),
    ("C3b", "Trânsito proibido a automóveis pesados"),
    ("C3c", "Trânsito proibido a automóveis de mercadorias"),
    ("C3d", "Trânsito proibido a automóveis de mercadorias de peso total superior a ... t"),
    ("C3e", "Trânsito proibido a motociclos simples"),
    ("C3f", "Trânsito proibido a ciclomotores"),
    ("C3g", "Trânsito proibido a velocípedes"),
    ("C3h", "Trânsito proibido a veículos agrícolas"),
    ("C3i", "Trânsito proibido a veículos de tracção animal"),
    ("C3j", "Trânsito proibido a carros de mão"),
    ("C3l", "Trânsito proibido a peões"), ("C3m", "Trânsito proibido a cavaleiros"),
    ("C3n", "Trânsito proibido a veículos com reboque"),
    ("C3o", "Trânsito proibido a veículos com reboque de dois ou mais eixos"),
    ("C3p", "Trânsito proibido a veículos transportando mercadorias perigosas"),
    ("C3q", "Trânsito proibido a veículos transportando produtos facilmente inflamáveis ou explosivos"),
    ("C3r", "Trânsito proibido a veículos transportando produtos susceptíveis de poluírem as águas"),
    ("C4a", "Trânsito proibido a automóveis e motociclos"),
    ("C4b", "Trânsito proibido a automóveis de mercadorias e a veículos a motor com reboque"),
    ("C4c", "Trânsito proibido a automóveis, a motociclos e a veículos de tracção animal"),
    ("C4d", "Trânsito proibido a automóveis de mercadorias e a veículos de tracção animal"),
    ("C4e", "Trânsito proibido a peões, a animais e a veículos que não sejam automóveis ou motociclos"),
    ("C4f", "Trânsito proibido a veículos de duas rodas"),
    ("C5", "Trânsito proibido a veículos de peso por eixo superior a ... t"),
    ("C6", "Trânsito proibido a veículos de peso total superior a ... t"),
    ("C7", "Trânsito proibido a veículos ou conjunto de veículos de comprimento superior a ... m"),
    ("C8", "Trânsito proibido a veículos de largura superior a ... m"),
    ("C9", "Trânsito proibido a veículos de altura superior a ... m"),
    ("C10", "Proibição de transitar a menos de ... m do veículo precedente"),
    ("C11a", "Proibição de virar à direita"), ("C11b", "Proibição de virar à esquerda"),
    ("C12", "Proibição de inversão do sentido de marcha"),
    ("C13", "Proibição de exceder a velocidade máxima de ... km/h"),
    ("C14a", "Proibição de ultrapassar"),
    ("C14b", "Proibição de ultrapassar para automóveis pesados"),
    ("C14c", "Proibição de ultrapassar para motociclos e ciclomotores"),
    ("C15", "Estacionamento proibido"), ("C16", "Paragem e estacionamento proibidos"),
    ("C17", "Proibição de sinais sonoros"), ("C18", "Paragem obrigatória na alfândega"),
    ("C19", "Outras paragens obrigatórias"),
    ("C20a", "Fim de todas as proibições impostas anteriormente por sinalização a veículos em marcha"),
    ("C20b", "Fim da limitação de velocidade"), ("C20c", "Fim da proibição de ultrapassar"),
    ("C20d", "Fim da proibição de ultrapassar para automóveis pesados"),
    ("C20e", "Fim da proibição de ultrapassar para motociclos e ciclomotores"),
    ("C21", "Fim da paragem ou estacionamento proibidos"),
    ("C22", "Fim da proibição de sinais sonoros"),
]
for cod, nome in proibicao:
    add(cod, nome, "sinais_proibicao")

# ---------- SINAIS DE OBRIGAÇÃO (D) ----------
obrigacao = [
    ("D1a", "Sentido obrigatório"), ("D1b", "Sentido obrigatório"),
    ("D1c", "Sentido obrigatório"), ("D1d", "Sentido obrigatório"), ("D1e", "Sentido obrigatório"),
    ("D2a", "Sentidos obrigatórios possíveis"), ("D2b", "Sentidos obrigatórios possíveis"),
    ("D2c", "Sentidos obrigatórios possíveis"),
    ("D3a", "Obrigação de contornar a placa ou obstáculo"),
    ("D3b", "Obrigação de contornar a placa ou obstáculo"), ("D4", "Rotunda"),
    ("D5a", "Via obrigatória para automóveis de mercadorias"),
    ("D5b", "Via obrigatória para automóveis pesados"),
    ("D6", "Via reservada a veículos de transporte público"),
    ("D7a", "Pista obrigatória para velocípedes"), ("D7b", "Pista obrigatória para peões"),
    ("D7c", "Pista obrigatória para cavaleiros"), ("D7d", "Pista obrigatória para gado em manada"),
    ("D7e", "Pista obrigatória para peões e velocípedes"),
    ("D7f", "Pista obrigatória para peões e velocípedes"),
    ("D8", "Obrigação de transitar à velocidade mínima de ... km/h"),
    ("D9", "Obrigação de utilizar correntes de neve"),
    ("D10", "Obrigação de utilizar as luzes de cruzamento (médios) acesas"),
    ("D11a", "Fim da via obrigatória para automóveis de mercadorias"),
    ("D11b", "Fim da via obrigatória para automóveis pesados"),
    ("D12", "Fim da via reservada a veículos de transporte público"),
    ("D13a", "Fim da pista obrigatória para velocípedes"),
    ("D13b", "Fim da pista obrigatória para peões"),
    ("D13c", "Fim da pista obrigatória para cavaleiros"),
    ("D13d", "Fim da pista obrigatória para gado em manada"),
    ("D13e", "Fim da pista obrigatória para peões e velocípedes"),
    ("D13f", "Fim da pista obrigatória para peões e velocípedes"),
    ("D14", "Fim da obrigação de transitar à velocidade mínima de ... km/h"),
    ("D15", "Fim da obrigação de utilizar correntes de neve"),
    ("D16", "Fim da obrigação de utilizar as luzes de cruzamento (médios) acesas"),
]
for cod, nome in obrigacao:
    add(cod, nome, "sinais_obrigacao")

# ---------- SINAIS DE SELECÇÃO DE VIAS (E) ----------
seleccao_vias = [
    ("E1", "Destinos sobre o itinerário"), ("E2", "Destinos de saída"),
    ("E3", "Sinal de selecção lateral"),
]
for cod, nome in seleccao_vias:
    add(cod, nome, "sinais_seleccao_vias")

# ---------- SINAIS DE AFECTAÇÃO DE VIAS (F) ----------
afectacao_vias = [
    ("F1a", "Aplicação de prescrição a via de trânsito"),
    ("F1b", "Aplicação de prescrição a via de trânsito"),
    ("F1c", "Aplicação de prescrição a via de trânsito"),
    ("F2", "Via de trânsito reservada a veículos de transporte público"),
]
for cod, nome in afectacao_vias:
    add(cod, nome, "sinais_afectacao_vias")

# ---------- SINAIS DE ZONA (G) ----------
zona = [
    ("G1", "Zona de estacionamento autorizado"), ("G2a", "Zona de estacionamento proibido"),
    ("G2b", "Zona de estacionamento proibido"), ("G3", "Zona de paragem e estacionamento proibidos"),
    ("G4", "Zona de velocidade limitada"), ("G5a", "Zona de trânsito proibido"),
    ("G5b", "Zona de trânsito proibido"), ("G6", "Fim de zona de estacionamento autorizado"),
    ("G7a", "Fim de zona de paragem e estacionamento proibidos"),
    ("G7b", "Fim de zona de paragem e estacionamento proibidos"),
    ("G8", "Fim de zona de velocidade limitada"),
    ("G9", "Fim de todas as proibições impostas na zona"),
]
for cod, nome in zona:
    add(cod, nome, "sinais_zona")

# ---------- SINAIS DE INFORMAÇÃO (H) ----------
informacao = [
    ("H1a", "Estacionamento autorizado"), ("H1b", "Estacionamento autorizado"),
    ("H2", "Hospital"), ("H3", "Trânsito de sentido único"), ("H4", "Via pública sem saída"),
    ("H5", "Correntes de neve recomendadas"), ("H6", "Velocidade recomendada"),
    ("H7", "Passagem para peões"), ("H8a", "Passagem desnivelada para peões"),
    ("H8b", "Passagem desnivelada para peões"), ("H9", "Hospital com urgência médica"),
    ("H10", "Posto de socorros"), ("H11", "Oficina"), ("H12", "Telefone"),
    ("H13a", "Posto de abastecimento de combustível"),
    ("H13b", "Posto de abastecimento de combustível com GPL"),
    ("H14a", "Parque de campismo"), ("H14b", "Parque para reboques de campismo"),
    ("H14c", "Parque misto para campismo e reboques de campismo"),
    ("H15", "Telefone de emergência"), ("H16a", "Pousada ou estalagem"),
    ("H16b", "Albergue"), ("H16c", "Pousada de juventude"), ("H16d", "Turismo rural"),
    ("H17", "Hotel"), ("H18", "Restaurante"), ("H19", "Café ou bar"),
    ("H20a", "Paragem de veículos de transporte colectivo de passageiros"),
    ("H20b", "Paragem de veículos de transporte colectivo de passageiros que transitem sobre carris"),
    ("H20c", "Paragem de veículos afectos ao transporte de crianças"),
    ("H21", "Aeroporto"), ("H22", "Posto de informações"), ("H23", "Estação de radiodifusão"),
    ("H24", "Auto-estrada"), ("H25", "Via reservada a automóveis e motociclos"),
    ("H26", "Escapatória"), ("H27", "Inversão de marcha"), ("H28", "Limites de velocidade"),
    ("H29a", "Identificação de país"), ("H29b", "Identificação de país"),
    ("H30", "Praticabilidade da via"),
    ("H31a", "Número e sentido das vias de trânsito"),
    ("H31b", "Número e sentido das vias de trânsito"),
    ("H31c", "Número e sentido das vias de trânsito"),
    ("H31d", "Número e sentido das vias de trânsito"),
    ("H32", "Supressão de via de trânsito"), ("H33", "Via verde"),
    ("H34", "Centro de inspecções"), ("H35", "Túnel"),
    ("H36", "Fim da recomendação do uso de correntes de neve"),
    ("H37", "Fim de velocidade recomendada"), ("H38", "Fim de auto-estrada"),
    ("H39", "Fim de via reservada a automóveis e motociclos"),
    ("H40", "Fim de estacionamento autorizado"), ("H41", "Fim de túnel"),
    ("H42", "Velocidade média"),
]
for cod, nome in informacao:
    add(cod, nome, "sinais_informacao")

# ---------- SINAIS DE PRÉ-SINALIZAÇÃO (I) ----------
pre_sinalizacao = [
    ("I1", "Pré-aviso simplificado (Intersecção desnivelada)"),
    ("I2a", "Pré-aviso gráfico (Intersecção de nível)"),
    ("I2b", "Pré-aviso gráfico (Rotunda)"),
    ("I2c", "Pré-aviso gráfico (Intersecção de nível)"),
    ("I2d", "Pré-aviso gráfico (Intersecção desnivelada)"),
    ("I2e", "Pré-aviso gráfico"), ("I2f", "Pré-aviso gráfico"),
    ("I3a", "Pré-aviso reduzido"), ("I3b", "Pré-aviso reduzido"),
    ("I4a", "Aproximação de área de serviço"),
    ("I4b", "Aproximação de via de saída para área de serviço"),
    ("I5a", "Aproximação de área de repouso"),
    ("I5b", "Aproximação de via de saída para uma área de repouso"),
    ("I6", "Pré-sinalização de itinerário"),
    ("I7a", "Pré-sinalização de via sem saída"), ("I7b", "Pré-sinalização de via sem saída"),
    ("I8", "Aproximação de travessia de crianças"),
    ("I9a", "Aproximação de passagem de nível"), ("I9b", "Aproximação de passagem de nível"),
    ("I9c", "Aproximação de passagem de nível"), ("I9d", "Aproximação de passagem de nível"),
    ("I9e", "Aproximação de passagem de nível"), ("I9f", "Aproximação de passagem de nível"),
]
for cod, nome in pre_sinalizacao:
    add(cod, nome, "sinais_pre_sinalizacao")

# ---------- SINAIS DE DIRECÇÃO (J) ----------
direccao = [
    ("J1", "Direcção da via de saída"), ("J2", "Direcção de via de acesso"),
    ("J3a", "Indicação de âmbito urbano"), ("J3b", "Indicação de âmbito urbano"),
    ("J3c", "Indicação de âmbito urbano"), ("J3d", "Indicação de âmbito urbano"),
]
for cod, nome in direccao:
    add(cod, nome, "sinais_direccao")

# ---------- SINAIS DE CONFIRMAÇÃO (L) ----------
add("L1", "Sinal de confirmação", "sinais_confirmacao")

# ---------- SINAIS DE IDENTIFICAÇÃO DE LOCALIDADES (N) ----------
localidades = [
    ("N1a", "Início de localidade"), ("N1b", "Início de localidade"),
    ("N2a", "Fim de localidade"), ("N2b", "Fim de localidade"),
]
for cod, nome in localidades:
    add(cod, nome, "sinais_identificacao_localidades")

# ---------- SINAIS COMPLEMENTARES (O) ----------
complementares = [
    ("O1a", "Demarcação hectométrica da via - IP"), ("O1b", "Demarcação hectométrica da via – IC"),
    ("O1c", "Demarcação hectométrica da via – restantes estradas"),
    ("O1d", "Demarcação hectométrica da via – estradas municipais"),
    ("O2a", "Demarcação quilométrica da via – AE"), ("O2b", "Demarcação quilométrica da via - IP"),
    ("O2c", "Demarcação quilométrica da via – IC"),
    ("O2d", "Demarcação quilométrica da via – restantes estradas"),
    ("O2e", "Demarcação quilométrica da via – estradas municipais"),
    ("O3a", "Demarcação miriamétrica da via - AE"), ("O3b", "Demarcação miriamétrica da via - IP"),
    ("O3c", "Demarcação miriamétrica da via – IC"),
    ("O3d", "Demarcação miriamétrica da via – restantes estradas"),
    ("O3e", "Demarcação miriamétrica da via – estradas municipais"),
    ("O4a", "Sinal de aproximação de saída"), ("O4b", "Sinal de aproximação de saída"),
    ("O4c", "Sinal de aproximação de saída"),
    ("O5a", "Baia direccional para balizamento de pontos de divergência"),
    ("O5b", "Baia direccional para balizamento de pontos de divergência"),
    ("O6a", "Baia direccional"), ("O6b", "Baia direccional"),
    ("O7a", "Baliza de posição"), ("O7b", "Baliza de posição"),
]
for cod, nome in complementares:
    add(cod, nome, "sinais_complementares")

# ---------- SINALIZAÇÃO TURÍSTICO-CULTURAL (T) ----------
turistico_cultural = [
    ("T1", "Região"), ("T2", "Património"), ("T3", "Património cultural"),
    ("T4a", "Identificação de circuito"), ("T4b", "Direcção de circuito"),
    ("T5a", "Identificação de rota"), ("T5b", "Direcção de rota"), ("T6", "Localidade"),
]
for cod, nome in turistico_cultural:
    add(cod, nome, "sinalizacao_turistico_cultural")

# ---------- MARCAS RODOVIÁRIAS (M) ----------
marcas = [
    ("M1", "Linha contínua"), ("M2", "Linha descontínua"), ("M3", "Linha mista"),
    ("M4", "Linha descontínua de aviso"), ("M5", "Linha de sentido reversível"),
    ("M6", "Linha descontínua de abrandamento"), ("M6a", "Linha descontínua de aceleração"),
    ("M7", "Linha contínua (corredor de circulação)"), ("M7a", "Linha descontínua (corredor de circulação)"),
    ("M8", "Linha de paragem"), ("M8a", "Linha de paragem com símbolo \"STOP\""),
    ("M9", "Linha de cedência de passagem"), ("M9a", "Linha de cedência de passagem com símbolo triangular"),
    ("M10", "Passagem para ciclistas"), ("M10a", "Passagem para ciclistas"),
    ("M11", "Passagem para peões"), ("M11a", "Passagem para peões"),
    ("M12", "Linha contínua junto ao limite da faixa de rodagem"),
    ("M12a", "Linha contínua sobre o bordo do passeio"),
    ("M13", "Linha descontínua junto ao limite da faixa de rodagem"),
    ("M13a", "Linha descontínua sobre o bordo do passeio"),
    ("M14", "Linha em ziguezague"), ("M14a", "Paragem e estacionamento para cargas e descargas"),
    ("M15", "Seta de selecção"), ("M15a", "Seta de selecção"), ("M15b", "Seta de selecção"),
    ("M15c", "Seta de selecção"), ("M15d", "Seta de selecção"), ("M15e", "Seta de selecção"),
    ("M15f", "Seta de selecção"),
    ("M16", "Seta de desvio"), ("M16a", "Seta de desvio"), ("M16b", "Seta de desvio"),
    ("M17", "Raias oblíquas delimitadas por linhas contínuas"),
    ("M17a", "Raias oblíquas delimitadas por linhas contínuas"),
    ("M17b", "Cruzamento ou entroncamento facilmente congestionável"),
    ("M18", "Marcação de objectos contíguos à faixa de rodagem"),
    ("M19", "Guias"), ("M20", "Bandas cromáticas"), ("M21", "Marcas de segurança"),
]
for cod, nome in marcas:
    add(cod, nome, "marcas_rodoviarias")

# ---------- SINALIZAÇÃO TEMPORÁRIA - Sinais de indicação (ST) ----------
temporaria_st = [
    ("ST1a", "Número e sentido das vias de trânsito"), ("ST1b", "Número e sentido das vias de trânsito"),
    ("ST1c", "Número e sentido das vias de trânsito"), ("ST1d", "Número e sentido das vias de trânsito"),
    ("ST2", "Supressão de via de trânsito"), ("ST3", "Supressão da berma"),
    ("ST4", "Desvio de via de trânsito"), ("ST5", "Desvio para a faixa de rodagem contrária"),
    ("ST6", "Estreitamento de via de trânsito"),
    ("ST7", "Pré-sinalização de desvio de itinerário"),
    ("ST8a", "Desvio de itinerário"), ("ST8b", "Desvio de itinerário"),
    ("ST9", "Fim de desvio"), ("ST10", "Circulação alternada"),
    ("ST11", "Trânsito sujeito a demora"), ("ST12", "Telefone de emergência"),
    ("ST13", "Acidente"), ("ST14", "Fim de obras"),
]
for cod, nome in temporaria_st:
    add(cod, nome, "sinalizacao_temporaria")

# ---------- DISPOSITIVOS COMPLEMENTARES (ET) ----------
temporaria_et = [
    ("ET1", "Raquetas de sinalização"), ("ET2", "Baias direccionais"),
    ("ET3", "Baias de posição"), ("ET4", "Baliza de alinhamento"),
    ("ET5", "Balizas de posição"), ("ET6", "Cones"), ("ET7", "Pórticos"),
    ("ET8", "Conjunto de lanternas sequenciais sem fios"),
    ("ET9", "Conjunto de lanternas sequenciais com fios"),
    ("ET10", "Perfil móvel de plástico"), ("ET11", "Robot"),
    ("ET12", "Atrelado de balizamento"), ("ET13", "Seta luminosa"),
]
for cod, nome in temporaria_et:
    add(cod, nome, "dispositivos_complementares")

# ---------- Exportar ----------
with open("/home/claude/cod-iv/data/sinais.json", "w", encoding="utf-8") as f:
    json.dump(sinais, f, ensure_ascii=False, indent=2)

print(f"Total de sinais extraídos: {len(sinais)}")

# Contagem por categoria
from collections import Counter
cats = Counter(s["categoria"] for s in sinais)
for cat, count in cats.items():
    print(f"  {cat}: {count}")

# -*- coding: utf-8 -*-
"""
COD-IV - Extração de dados do "Manual de Mecânica" (Escola de Condução Auto-Marmindo)
Gera data/mecanica.json com perguntas e respostas organizadas por categoria.
"""
import json

perguntas = []

def add(pergunta, resposta, categoria):
    perguntas.append({
        "pergunta": pergunta,
        "resposta_correta": resposta,
        "categoria": categoria,
        "imagem_url": None
    })

# ---------- PARTES CONSTITUINTES DE UM VEÍCULO ----------
cat = "partes_do_veiculo"
add("O que é chassi?",
    "Chassi é a estrutura que serve de base para o apoio do motor, depósito de combustível, a caixa ou carroçaria, a caixa de velocidade, os eixos, sistema de transmissão etc.",
    cat)
add("O que é caixa ou carroçaria?",
    "Caixa ou carroçaria é a parte do veículo que assenta sobre o chassi. Serve para o alojamento do condutor, dos passageiros ou da carga a transportar. Pode ser aberto ou fechado.",
    cat)
add("O que é cabine simples?",
    "Comporta duas ou três pessoas. É mais indicada para trabalho (para o transporte de pequenas cargas).",
    cat)
add("O que é cabine dupla?",
    "Comporta cinco ou seis pessoas. Indicado para trabalho ou uso doméstico.",
    cat)
add("O que é cabine estendida?",
    "Comporta duas ou três pessoas e possui um espaço extra atrás dos bancos dianteiros, para colocar bagagens. Pode ser basculante ou não.",
    cat)
add("O que é o conjunto de veículos?",
    "É o grupo constituído por um veículo tractor e seu reboque ou semi-reboque. Para efeitos de circulação, o conjunto de veículos é equiparado a veículo único.",
    cat)
add("Quantos tipos de tractor são conhecidos?",
    "São conhecidos dois tipos de tractor: tractor de estrada (cavalo mecânico) e tractor de campo ou agrícola.",
    cat)

# ---------- TIPOS DE CHASSI ----------
cat = "tipos_de_chassi"
add("O que é o chassi monobloco?",
    "É utilizado nos veículos ligeiros. O chassi é colado com a caixa, e a sua estrutura é construída como uma peça única. Por essa característica, dá-se o nome de monobloco.",
    cat)
add("O que é o chassi tubular?",
    "É feito de um conjunto de armação de tubos, utilizado nos automóveis de competição e em outros tipos de automóveis.",
    cat)
add("O que é o chassi de longarinas?",
    "É utilizado nos veículos pesados e ligeiros. É composto por duas longarinas (vigas) e várias travessas.",
    cat)
add("O que é o chassi monocoque?",
    "É utilizado em automóveis de competição do tipo Fórmula 1.",
    cat)
add("Como é chamado o chassi nas motocicletas (motos)?",
    "Nas motocicletas o chassi é chamado de \"quadro\", é a estrutura que suporta o motor, o suporte para o piloto, o acompanhante e os demais componentes.",
    cat)

# ---------- PAINEL / ILUMINAÇÃO ----------
cat = "painel_iluminacao"
add("Para que serve o painel ou quadro de instrumentos?",
    "Serve para dar ao condutor indicações como a velocidade do veículo, a temperatura do motor entre outros. Varia de acordo com o fabricante e o modelo do veículo.",
    cat)
add("O que diz a lei sobre a iluminação obrigatória do veículo desde o anoitecer ao amanhecer?",
    "Nenhum veículo pode transitar nas vias públicas desde o anoitecer ao amanhecer, sem que tenha acesas uma ou duas luzes brancas à frente e uma ou duas luzes vermelhas à retaguarda, perfeitamente visíveis.",
    cat)

# ---------- O MOTOR E A SUA DIVISÃO ----------
cat = "motor"
add("O que é a mecânica?",
    "Mecânica é a Ciência que estuda os movimentos e o equilíbrio das forças motrizes das máquinas. Ou seja, é a arte da construção, reparação ou montagem de máquinas.",
    cat)
add("O que é o motor?",
    "Motor é um conjunto de órgãos que se destina a transformar a energia calorífica ou térmica em energia mecânica. O mesmo está dividido em três partes: cabeça ou culatra, bloco de cilindros e cárter.",
    cat)
add("O que é a cabeça do motor (culatra)?",
    "É a parte superior que tapa os cilindros, nela estão situadas as válvulas (de admissão e de escape) e as velas de ignição.",
    cat)
add("O que é o bloco de cilindros?",
    "Estrutura sólida em ferro fundido, que serve de apoio a todas as peças (pistões, biela etc.).",
    cat)
add("O que é o cárter do motor?",
    "É uma peça rígida de metal, que fica debaixo do motor. Serve de depósito do óleo para a lubrificação do motor e também protege o motor das impurezas (resíduos sólidos).",
    cat)
add("Quais são as partes fixas do motor?",
    "As partes fixas do motor são: tampa da culatra, culatra, bloco de cilindros e cárter.",
    cat)
add("Quais são os órgãos móveis do motor?",
    "Os órgãos móveis do motor são: cambota, bielas, êmbolos, volante do motor etc.",
    cat)
add("O que é camisa do motor ou camisa do cilindro?",
    "Camisa do motor são tubos cilíndricos, que servem para revestir o interior dos cilindros. Se o bloco não tivesse vestido, o movimento de vai e vem do pistão desgastaria o bloco.",
    cat)
add("O que é a cambota e para que serve?",
    "Cambota é um veio de manivela com tantos moentes de apoios e de impulsos consoante o número de cilindros que tiver o motor. Serve para receber o movimento dos êmbolos por intermédio da biela e transmitir aos órgãos de distribuição e ao volante do motor.",
    cat)
add("Quais são as partes que compõem a cambota?",
    "As partes que compõem a cambota são: contrapeso, moentes de apoio, moentes de impulso, braços e falange.",
    cat)
add("Quantos tipos de cambota conheces?",
    "Conheço dois tipos de cambota: cambota com contrapeso e cambota sem contrapeso.",
    cat)
add("Qual é a diferença entre cambota com contrapeso e cambota sem contrapeso?",
    "A diferença é que a cambota sem contrapeso necessita de ter um volante maior, sendo portanto maior o seu esforço.",
    cat)
add("O que é o êmbolo e para que serve?",
    "O êmbolo é um corpo cilíndrico em forma de vaso invertido. Serve para receber o movimento das explosões dos gases por intermédio da biela.",
    cat)
add("Em quantas partes está dividido o êmbolo?",
    "O êmbolo divide-se em duas partes: Cabeça e Saia.",
    cat)
add("O que é que fica nas ranhuras que têm os êmbolos?",
    "Nas ranhuras que têm os êmbolos ficam os segmentos ou anéis de vedação.",
    cat)
add("Quantos tipos de segmentos conheces?",
    "Conheço dois tipos de segmentos: segmento de compressão ou de vedação e segmento de óleo.",
    cat)
add("Para que servem os segmentos?",
    "Os segmentos de óleo servem para raspar o óleo nas paredes dos cilindros, evitando que o mesmo passe para a cabeça do êmbolo e fazer a vedação. Os segmentos de compressão ou vedação servem para evitar que o combustível passe da cabeça do êmbolo para o cárter e fazer a vedação.",
    cat)
add("Para que serve a biela e como está composta?",
    "A biela serve para transmitir o movimento do êmbolo à cambota e vice-versa. Sua função é transformar o movimento rectilíneo em movimento circular contínuo. A biela está composta por: Cabeça, Haste e Pé.",
    cat)
add("O que é o volante do motor e para que serve?",
    "Volante do motor é uma roda metálica que se encontra na parte traseira da cambota. Serve para com o seu movimento vencer os pontos mortos do motor e nela está fixa a roda cremalheira, o prato de molas que serve para o encosto do disco de embraiagem.",
    cat)
add("O que é ponto morto?",
    "Ponto morto é a paragem dos êmbolos na parte superior ou inferior do cilindro para inverter o seu passeio.",
    cat)
add("Quantos pontos mortos tem o motor?",
    "O motor tem dois pontos mortos: ponto morto superior (P.M.S) e inferior (P.M.I).",
    cat)
add("Quantos tipos de motores a gasolina conheces?",
    "Conheço dois tipos de motores a gasolina: motor a dois tempos e motor a quatro tempos.",
    cat)
add("Qual é a diferença entre um motor a dois tempos e um motor a quatro tempos?",
    "A diferença é que o motor a dois tempos não tem órgãos de distribuição mecânica e não tem óleo depositado no cárter para lubrificação do motor, este é feito por uma mistura de óleo na gasolina numa percentagem de 5%, e os tempos do motor são feitos com dois passeios do êmbolo, e o distribuidor recebe o movimento da ponta da cambota, visto não haver veio de excêntrico.",
    cat)
add("O que são tempos do motor?",
    "Tempos do motor são as operações realizadas pelo passeio dos êmbolos. Isso é necessário para o funcionamento do motor.",
    cat)
add("Quais são os motores mais utilizados na maioria dos automóveis?",
    "Os motores mais utilizados na maioria dos automóveis modernos são de quatro tempos. Diz-se quatro tempos porque o seu funcionamento se baseia em quatro estágios diferentes: admissão, compressão, explosão e escape (motores a gasolina) ou admissão, compressão, combustão e escape (motores a gasóleo).",
    cat)
add("Descreve o ciclo de funcionamento de um motor a gasolina (4 tempos).",
    "1º Admissão: o êmbolo desloca do P.M.S ao P.M.I com as válvulas de admissão abertas e as de escape fechadas, admitindo a entrada do gás; a cambota dá meia volta. 2º Compressão: o êmbolo desloca do P.M.I ao P.M.S com as válvulas fechadas comprimindo o gás; a cambota dá meia volta. 3º Explosão: com as duas válvulas fechadas, a vela de ignição emite uma faísca que inflama o gás e provoca a explosão, empurrando o êmbolo do P.M.S ao P.M.I, produzindo energia; a cambota dá meia volta. 4º Escape: a válvula de escape abre-se, a de admissão fecha-se, o êmbolo desloca-se do P.M.I ao P.M.S libertando os gases de escape para a atmosfera.",
    cat)
add("Descreve o ciclo de funcionamento de um motor diesel (4 tempos).",
    "1º Admissão: o êmbolo desloca-se do P.M.S ao P.M.I com as válvulas de admissão abertas e a de escape fechada, entra ar fresco; a cambota dá meia volta. 2º Compressão: o êmbolo desloca-se do P.M.I ao P.M.S com as válvulas fechadas, o ar é comprimido; a cambota dá meia volta. 3º Combustão: o combustível é injectado no cilindro e inflama ao contactar o ar comprimido e quente, o êmbolo desloca-se do P.M.S ao P.M.I com as válvulas fechadas; a cambota dá meia volta. 4º Escape: válvulas de escape abertas, admissão fechadas, o êmbolo desloca-se do P.M.I ao P.M.S expelindo os gases queimados.",
    cat)
add("Que tipos de motores conheces?",
    "Os principais tipos de motores que conheço são: motor diesel e motor de explosão a gasolina. Existem ainda motores a gás pobre e motores que funcionam com álcool.",
    cat)
add("Quantos tipos de motores diesel conheces?",
    "Conheço três tipos de motores diesel: de baixa, de média e de alta compressão.",
    cat)

# ---------- SISTEMA DE DISTRIBUIÇÃO ----------
cat = "sistema_distribuicao"
add("Para que servem os órgãos de distribuição mecânica?",
    "Servem para fazer os tempos do motor em combinação com o passeio dos êmbolos, e fazer funcionar o distribuidor, a bomba mecânica de gasolina e a bomba de óleo.",
    cat)
add("Quais são os órgãos de distribuição do motor?",
    "Os órgãos de distribuição do motor são: roda condutora, roda conduzida, veio de excêntrico, touches/impulsores, varetas, veio de balanceiros, martelos, válvulas e molas.",
    cat)
add("Quantos sistemas de engrenagem de distribuição existem?",
    "Existem dois tipos de engrenagem de distribuição: engrenagem directa e engrenagem por corrente silenciosa ou por correia de distribuição mecânica.",
    cat)
add("Qual a diferença entre engrenagem directa e por corrente silenciosa?",
    "Na engrenagem directa a roda condutora está directamente ligada à roda conduzida; por corrente silenciosa, essa ligação é feita por intermédio de uma correia de distribuição mecânica.",
    cat)
add("Quantos tipos de distribuição conheces?",
    "Conheço dois tipos de distribuição: distribuição de motores com válvulas à cabeça e distribuição de motores com válvulas laterais.",
    cat)
add("Qual a diferença entre motor com válvulas à cabeça e motor com válvulas laterais?",
    "Nos motores com válvulas à cabeça, as válvulas situam-se na cabeça do motor e abrem-se de cima para baixo. Nos motores com válvulas laterais, as válvulas situam-se no bloco de cilindro e abrem-se de baixo para cima; estes motores não possuem vareta, veio de balanceiro nem balanceiros, pois os touches actuam directamente no pé da válvula.",
    cat)
add("Para que serve o veio de excêntrico?",
    "Serve para abrir e fechar as válvulas por intermédio de varetas, molas e balanceiros. Também faz funcionar a bomba de óleo e o distribuidor.",
    cat)
add("Para que serve a mola vareta?",
    "Serve para auxiliar o veio de excêntrico na abertura e o fecho das válvulas.",
    cat)
add("Para que serve a roda condutora e onde fica localizada?",
    "Serve para transmitir o movimento da cambota ao veio de excêntrico por meio da roda conduzida. Encontra-se colocada na frente da cambota.",
    cat)
add("Para que serve a roda conduzida?",
    "Serve para receber o movimento da roda condutora e transmitir ao veio de excêntrico.",
    cat)
add("Quantas válvulas tem o motor e para que servem?",
    "O motor tem duas válvulas para cada cilindro (uma de admissão e outra de escape). A válvula de admissão permite a entrada da mistura gasosa e faz a vedação; a de escape permite a saída dos gases queimados e faz a vedação.",
    cat)
add("Como se distingue uma válvula de escape de uma válvula de admissão?",
    "Distinguem-se pelos colectores ou pela cor. Se usadas, as válvulas de escape ficam mais escuras por causa dos gases queimados. Se novas, reconhece-se pelo diâmetro: o diâmetro da cabeça da válvula de admissão é maior que o da válvula de escape.",
    cat)
add("Para que serve a mola da válvula?",
    "Serve para dar mais consistência na abertura e o fecho das válvulas.",
    cat)
add("Para que serve o colector de admissão?",
    "Serve para expirar o ar para a transformação da gasolina em gás.",
    cat)
add("Para que serve o colector de escape?",
    "Serve para dar saída aos gases queimados no interior dos cilindros para a atmosfera.",
    cat)
add("Para que serve a correia de distribuição?",
    "Serve para comandar o motor através da roda condutora e a roda conduzida.",
    cat)
add("O que é comandar mecanicamente um motor?",
    "É engrenar as rodas de distribuição de forma que o movimento das válvulas fique combinado com o passeio dos êmbolos para que possam fazer os tempos do motor.",
    cat)

# ---------- SISTEMA DE TRAVAGEM ----------
cat = "sistema_travagem"
add("O que são travões?",
    "Travões é um conjunto de dispositivos que servem para abrandar ou parar o veículo através das rodas. Seus elementos fundamentais são: pedal, tirante, tambor e maxilas.",
    cat)
add("Como está composto o sistema de travagem?",
    "O sistema de travagem está composto por: travão de serviço e travão de estacionamento (travão de mão).",
    cat)
add("Quantos sistemas de travagem são conhecidos?",
    "São conhecidos três sistemas de travagem: sistema de travagem mecânica, sistema de travagem hidráulica e sistema de travagem por ar comprimido.",
    cat)
add("Como funcionam os travões mecânicos?",
    "Carregando-se no pedal de travão, existem tirantes que vão accionar as alavancas que fazem rodar os excêntricos entre as maxilas, apertando-as contra os tambores, ficando o veículo travado. Soltando-se o pedal, as maxilas unem-se por acção das molas de chamada e o veículo fica destravado.",
    cat)
add("Como é constituído o sistema de travão hidráulico?",
    "Está constituído por pedal de travões, bomba central dos travões servofreio, depósito de óleo, tubos condutores de óleo, duas maxilas guarnecidas de ferodo, um ou mais parafusos de afinação, um cilindro com uma mola no interior, duas borrachas vedantes e dois pequenos êmbolos da válvula de comando.",
    cat)
add("Como é constituído o sistema de ar comprimido?",
    "É constituído por: um compressor de ar, um ou vários depósitos de ar, uma válvula retentora de pressão, manómetro de pressão de ar, válvulas de comando, tubos condutores e cilindro de comando de travões.",
    cat)
add("Qual é a diferença entre o travão de serviço e o travão de estacionamento?",
    "O travão de serviço tem como objectivo imobilizar as quatro rodas do veículo, enquanto o de estacionamento imobiliza apenas as rodas de trás.",
    cat)
add("Que outros tipos de travões são conhecidos?",
    "São conhecidos ainda: travões de disco, travões eléctricos e travões Anti-bloqueio.",
    cat)
add("Quais são as avarias mais comuns no sistema de travagem de ar comprimido?",
    "Compressor danificado, fuga na tubagem, má vedação das válvulas, maxilas muito afastadas, e massa que as reveste gasta e vidrada com valvulina.",
    cat)
add("Quais são as avarias mais frequentes no sistema de travagem?",
    "Pedal de travagem muito leve, ar nos tubos, bomba principal avariada, cinta de calços gastos, tambores avariados e servofreio danificado.",
    cat)
add("Como é constituída a bomba central de travagem?",
    "Por depósito de óleo dos travões, retentores (vácuo, mola principal e de separação), alinha de enchimento, anel de freio, intermédio e parafuso de união.",
    cat)
add("Para que servem as molas nas maxilas?",
    "Servem para afastar as sintas no tambor em caso de travagem.",
    cat)
add("Para que servem as sintas?",
    "Servem para prender o tambor no accionar do travão.",
    cat)
add("Para que serve o calço?",
    "Serve para prender o disco de roda no accionar do travão.",
    cat)
add("Para que serve o tambor?",
    "Serve para facilitar a travagem das rodas através das sintas.",
    cat)
add("Para que serve o disco de roda?",
    "Serve para travar as rodas através das sapatas e os calços.",
    cat)
add("Para que serve a bomba central dos travões?",
    "Serve para conduzir o óleo para os cilindros através das tubagens no accionar dos travões.",
    cat)
add("Para que serve o servo freio?",
    "Serve para auxiliar o condutor durante a travagem, permitindo exercer menor esforço. Está constituído por: diafragma, conduta de vácuo, válvula de disco, filtro de ar, mola de compressão, câmara da bomba e câmara de actuação.",
    cat)
add("O que é a sapata?",
    "Sapata é o suporte dos calços ou pastilhas.",
    cat)

# ---------- SISTEMA DE ARREFECIMENTO ----------
cat = "sistema_arrefecimento"
add("Para que serve o sistema de arrefecimento ou refrigeração?",
    "Serve para arrefecer o motor, mantendo-o a uma temperatura conveniente durante o seu funcionamento, uma temperatura que varia de 80 a 90 ºC.",
    cat)
add("Quais são os órgãos de arrefecimento do motor?",
    "São: radiador, tubagem, bomba de água, pá ventiladora, junta de cupla, termómetro e o termóstrato. O arrefecimento pode ser por água ou por ar.",
    cat)
add("Como é feito o arrefecimento por água?",
    "Quando o condutor liga o motor, a bomba de água é accionada pela correia do alternador, movimentando a turbina (ventoinha). Esta produz um vácuo que obriga a água vinda do radiador a circular através dos canais de arrefecimento, voltando novamente ao radiador pela parte superior, mantendo a circulação.",
    cat)
add("Como é feito o arrefecimento por ar?",
    "É feito pela deslocação do veículo formando uma corrente de ar à volta dos cilindros que os arrefece, ou por palhetas nos motores a dois tempos.",
    cat)
add("Como se distinguem os motores arrefecidos por ar?",
    "Distinguem-se pelas suas palhetas; os motores arrefecidos por água não têm palhetas mas sim bomba de água, radiador etc.",
    cat)
add("Quais são as principais avarias nos motores arrefecidos por água?",
    "Bomba de água avariada, falta de água no radiador, pá ventilador partida, radiador roto ou entupido, tubos rotos, correia do alternador rebentada ou larga e termóstrato avariado.",
    cat)
add("Para que serve o radiador?",
    "Serve para armazenar a água que arrefece o motor.",
    cat)
add("Para que serve a pá ventilador?",
    "Serve para arrefecer a água que arrefece o motor.",
    cat)
add("Para que serve a bomba de água?",
    "Serve para fazer circular a água do radiador para o interior do motor durante o seu funcionamento.",
    cat)
add("Como está composta a bomba de água?",
    "É composta por um corpo da bomba, um veio, uma turbina e um empanque ou vedante.",
    cat)
add("Quais são as principais avarias da bomba de água?",
    "Corpo estragado, veio empenado ou vedante mal instalado.",
    cat)
add("O que é o termóstrato e para que serve?",
    "É um dispositivo que controla automaticamente a temperatura, indicando a temperatura do motor durante o seu funcionamento. Encontra-se localizado no quadro ou painel de instrumento.",
    cat)
add("Qual é a função do termóstrato?",
    "Dar a passagem da água para o motor quando a água estiver quente.",
    cat)

# ---------- SISTEMA DE LUBRIFICAÇÃO ----------
cat = "sistema_lubrificacao"
add("Qual é a função do sistema de lubrificação?",
    "Distribuir o óleo lubrificante entre as partes móveis do motor, para evitar ou reduzir o desgaste das peças, evitando que elas entrem em contacto directo, e para auxiliar no arrefecimento do motor.",
    cat)
add("Quais são as peças que compõem o sistema de lubrificação?",
    "Cárter de óleo (depósito onde o óleo fica armazenado), pescador ou captador de óleo, bomba de óleo, filtro de óleo, válvula de alívio de pressão e interruptor de pressão de óleo.",
    cat)
add("O óleo a mais no motor é prejudicial?",
    "Pode ser prejudicial, dependendo do estado dos segmentos: se estiverem gastos, o óleo pode passar para a câmara de explosão e isolar as velas, e nesse caso o motor pára.",
    cat)
add("Como está constituída a bomba de óleo?",
    "É constituída por um veio, dois carretos e o filtro.",
    cat)
add("O que é o manómetro e onde fica situado?",
    "É um dispositivo que indica a pressão do óleo do motor. Encontra-se no quadro de instrumento.",
    cat)
add("Que tipos de óleo conheces e para que servem?",
    "Óleo 30: usado nos motores a gasolina. Óleo 40: usado nos motores a gasóleo. Óleo 10: usado nas caixas de velocidade automática e nas colunas de direcção hidráulica. Óleo dos travões: usado na bomba principal de embraiagem e dos travões. Valvulina ou óleo 90: usado na caixa de velocidade mecânica (automóveis ligeiros). Óleo 50: usado nos motores a gasóleo (diesel). Óleo 140: usado no diferencial e na caixa de velocidade dos automóveis pesados.",
    cat)
add("Para que serve a bomba de óleo?",
    "Serve para sugar o óleo do cárter e enviar às tubulações, mantendo-o em circulação.",
    cat)
add("Para que serve o pescador de óleo?",
    "Serve para colher e filtrar o óleo depositado no cárter, evitando que entrem detritos nas tubulações.",
    cat)
add("Para que serve o interruptor de pressão de óleo?",
    "Serve para informar ao condutor quando há falta ou queda de pressão de óleo no sistema de lubrificação.",
    cat)
add("Para que serve o cárter de óleo?",
    "Serve para o depósito do óleo do motor.",
    cat)
add("Quantos tipos de cárter conheces?",
    "Conheço dois tipos de cárter: cárter húmido e cárter seco.",
    cat)
add("Qual é a diferença entre o cárter húmido e o cárter seco?",
    "O cárter húmido serve de depósito do óleo. O cárter seco não funciona como depósito de óleo — em marcas como Ferrari e Porsche, o óleo fica armazenado num reservatório separado do motor, com maior capacidade (4 a 6 litros). No sistema de cárter seco existem duas bombas de óleo: uma para aspirar o óleo do cárter para o reservatório, e outra para fazer circular o óleo para as partes certas.",
    cat)
add("Para que serve o filtro de óleo?",
    "Serve para limpar o óleo, evitar impurezas na circulação e evitar que detritos prejudiquem o processo de lubrificação, causando danos no motor.",
    cat)
add("O que é óleo do motor?",
    "É o líquido que lubrifica e percorre o motor.",
    cat)

# ---------- SISTEMA DE TRANSMISSÃO ----------
cat = "sistema_transmissao"
add("O que é o sistema de transmissão?",
    "É um conjunto de mecanismos que transmite o movimento do motor às rodas motrizes. Os órgãos que o compõem são: embraiagem ou união de engate, caixa de velocidade, cardan ou junta universal, veio de transmissão, grupo cónico, diferencial, semi-eixos, cabos e rodas.",
    cat)
add("Onde se encontra localizado o sistema de embraiagem?",
    "Está montado no motor e serve para ligar e desligar o movimento da caixa de velocidade, permitindo um arranque mais suave ao veículo.",
    cat)
add("Quais são os elementos do sistema de embraiagem?",
    "Disco de embraiagem, prensa ou prato de mola, rolamento de embraiagem, garfo tirante, pedal e bomba de embraiagem.",
    cat)
add("Para que serve a caixa de velocidade?",
    "Serve para fornecer às rodas a força motriz necessária a todas as condições de locomoção, e para auxiliar o condutor na condução, ao pôr e variar de mudança.",
    cat)
add("Para que serve o cabo de embraiagem?",
    "Serve para fazer a ligação entre o pedal e a embraiagem, permitindo ligar e desligar a energia do motor à caixa de velocidade.",
    cat)
add("Para que serve o pedal de embraiagem?",
    "Serve para cortar a comunicação entre o motor e as rodas.",
    cat)
add("Para que serve o platon de embraiagem ou prato de mola?",
    "Serve para fazer a união do disco de embraiagem com o volante do motor.",
    cat)
add("Para que serve o disco de embraiagem?",
    "Serve para possibilitar que o condutor consiga pôr e variar de mudanças.",
    cat)
add("Para que serve o eixo cardan?",
    "Serve para transmitir a força do motor para as rodas.",
    cat)
add("Para que serve o diferencial?",
    "Serve para permitir que nas curvas uma roda dê mais volta em relação à outra.",
    cat)
add("Para que serve o semi-eixo?",
    "Serve para receber o movimento do torque (rotação do motor) e transmitir às rodas.",
    cat)
add("Para que serve o veio de transmissão?",
    "Serve para receber o movimento da caixa de velocidade e transmitir ao diferencial por meio de um pião de ataque.",
    cat)
add("Como está constituída a caixa de velocidade?",
    "Por uma caixa com vários carretos e quatro veios (primário, secundário, intermédio e inversor), uma tampa, alavanca, forquilha e o cárter da caixa.",
    cat)
add("Quais são os tipos de caixa de velocidade?",
    "Caixa mecânica e caixa automática, com posições diferentes: uma longínqua e outra transversal.",
    cat)
add("Qual é o lubrificante utilizado na caixa de velocidade mecânica?",
    "Trabalha com valvulina ou óleo 90 (automóveis ligeiros) ou óleo 140 (automóveis pesados).",
    cat)
add("Qual é o lubrificante utilizado na caixa de velocidade automática?",
    "Trabalha com óleo 10 hidráulico.",
    cat)
add("Qual é a função do diferencial?",
    "Distribuir o movimento produzido pelo motor aos semi-eixos de forma a chegar às rodas, evitando derrapagem, permitindo que nas curvas a roda de fora dê mais volta que a de dentro.",
    cat)
add("O que são rodas motrizes?",
    "São aquelas rodas que recebem o movimento directamente do motor.",
    cat)
add("Como está constituído o diferencial?",
    "Por dois semi-eixos, pião de ataque, concha, satélites, planetário e roda de coroa.",
    cat)
add("Qual é o lubrificante que trabalha no diferencial?",
    "Valvulina ou óleo 90 para automóveis ligeiros; os pesados trabalham com óleo 140.",
    cat)
add("O que encontramos no veio de transmissão ou árvore de transmissão?",
    "Encontramos cruzetas ou cardão, que servem de ligação da caixa de velocidade ao diferencial, sendo responsáveis pela transmissão do movimento entre estes órgãos.",
    cat)
add("Que tipos de veículos de tracção total existem?",
    "Veículos todo-o-terreno (para qualquer terreno, ultrapassam cursos de água), veículos turismo 4x4 (adaptam-se a terrenos escorregadios ou neve, mas não suportam grandes torções nos chassis) e veículos 4x4 de altas prestações (recorrem à tracção total para aumentar o desempenho).",
    cat)

# ---------- ÓRGÃOS DE SUSPENSÃO ----------
cat = "suspensao"
add("Quais são os órgãos de suspensão?",
    "Pneumáticos (pneus), barra estabilizadora, amortecedores a gás (telescópicos e hidráulicos), molas em lâminas (fecho de molas), molas em espirais (helicoidal), mangas de eixo e barra de torção.",
    cat)
add("Para que servem os órgãos de suspensão?",
    "Servem para reduzir as oscilações entre o veículo e o pavimento nas desigualdades da via.",
    cat)
add("O que é a suspensão?",
    "É um conjunto de órgãos flexíveis e resistentes que servem de apoio entre o quadro e o automóvel.",
    cat)
add("Qual é a função da suspensão?",
    "Efectuar a ligação entre a carroçaria e as rodas do veículo, mantendo a estabilidade do veículo. Deve ter estabilidade (evitar que os ressaltos das rodas sejam transmitidos ao veículo) e amortecimento (impedir o balanceamento excessivo da carroçaria).",
    cat)
add("Quais são as principais funções dos amortecedores?",
    "Reduzir as oscilações, controlar o movimento vertical do veículo, assegurar uma boa aderência das rodas ao solo, minimizar o desgaste das rodas e dos componentes do chassis, garantir a estabilidade do veículo (principalmente nas curvas) e evitar trepidações da direcção.",
    cat)
add("Quais são as principais avarias nos órgãos de suspensão?",
    "Barra estabilizadora empenada ou partida, amortecedores sem pressão, molas partidas e mangas de eixo empenadas.",
    cat)
add("Porquê o termo pneu radial?",
    "Diz-se pneu radial pela sua forma e revestimento ou constituição.",
    cat)
add("Qual é a diferença entre roda e pneu?",
    "Não há pneu sem roda. Pneu e roda: o pneu é o conjunto de pneu, câmara-de-ar e a jante.",
    cat)

# ---------- SISTEMA DE DIRECÇÃO ----------
cat = "direccao"
add("Quais são os componentes do sistema de direcção?",
    "Cremalheira, pinhão (sector dentado), terminais de direcção, bomba de pressão e tubos.",
    cat)
add("Qual é a função do sistema de direcção?",
    "Orientar as rodas dianteiras (directrizes) de modo a fazer o veículo seguir a trajectória desejada pelo condutor. Deve ser suave e precisa, sendo o sistema mais utilizado o de roda cremalheira e pinhão.",
    cat)
add("Qual é a característica do sistema de direcção?",
    "Segurança, precisão, facilidade de manejamento e não transmitir ao condutor as vibrações provocadas pelas irregularidades da estrada.",
    cat)
add("O que é a direcção assistida?",
    "É o tipo de direcção que diminui o esforço do condutor sobre o volante. Necessita de afinação ou alinhamento quando sofre golpes violentos por irregularidades do pavimento.",
    cat)
add("O que é a direcção assistida electricamente?",
    "É o tipo de direcção que auxilia o condutor através de um motor eléctrico instalado na coluna de direcção.",
    cat)
add("Quantos volantes dispõe um veículo?",
    "Um veículo dispõe pelo menos de dois volantes: volante de direcção e volante do motor.",
    cat)
add("Como pode ser o sistema de direcção quanto ao veículo?",
    "Pode ser mecânica, assistida ou assistida electricamente.",
    cat)
add("Quais são as principais avarias no sistema de direcção?",
    "Terminais de direcção estragados, bomba de pressão avariada, tubos rotos, fuga na direcção, rótulas estragadas (barulhentas), cremalheira e pinhão estragados.",
    cat)

# ---------- SISTEMA DE ALIMENTAÇÃO ----------
cat = "alimentacao"
add("Para que serve o sistema de alimentação?",
    "Serve para conduzir o combustível do reservatório até ao motor, a fim de o alimentar.",
    cat)
add("Quais são os sistemas de alimentação para fazer chegar a gasolina ao carburador?",
    "Bomba mecânica de gasolina, bomba eléctrica e sistema de gravidade.",
    cat)
add("Quando é que se aplica o sistema de gravidade?",
    "Aplica-se quando a bomba mecânica ou eléctrica está avariada, colocando-se um depósito num nível superior ao do carburador, e a gasolina desce por gravidade através dos tubos condutores.",
    cat)
add("Quais são os órgãos de alimentação e de escape do motor?",
    "Depósito ou reservatório de combustível, tubos condutores, bomba mecânica ou eléctrica de gasolina, filtro de gasolina, carburador ou sistema de injecção, colector de admissão e colector de escape.",
    cat)
add("Para que serve o reservatório de combustível?",
    "Serve para nele estar depositado o combustível a fim de o enviar ao motor quando for necessário.",
    cat)
add("Para que serve a bomba mecânica de gasolina?",
    "Serve para aspirar a gasolina do depósito e enviá-la ao carburador através dos tubos condutores.",
    cat)
add("Como está composta a bomba mecânica de gasolina?",
    "Corpo da bomba, diafragma, molas, válvulas de entrada e saída, retentoras (uma de entrada e outra de saída), filtro e braço.",
    cat)
add("Por que se diz que a bomba é mecânica?",
    "Porque é movida pelo veio de excêntrico, e tem um braço.",
    cat)
add("Quais são as avarias da bomba mecânica?",
    "Braço partido ou gasto, mola partida ou com pouca pressão, diafragma roto ou dilatado, válvulas retentoras entupidas e filtro sujo.",
    cat)
add("Como funciona a bomba mecânica?",
    "Funciona com o movimento do veio de excêntrico: quando o ressalto toca no braço, provoca a descida do diafragma, produzindo um vácuo que aspira a gasolina do reservatório. Ao passar o ressalto, a mola faz subir o diafragma, que empurra a gasolina para a cuba.",
    cat)
add("O motor sem bomba mecânica de gasolina ou avariada pode trabalhar?",
    "Sim, aplicando o sistema de gravidade, que consiste em colocar um reservatório mais alto que o nível do carburador.",
    cat)
add("Como se faz a aceleração de um motor a gasolina?",
    "Carregando no pedal do acelerador; um tirante acciona a borboleta de aceleração que, ao abrir-se, dá passagem à mistura gasosa para os cilindros e o motor acelera. Soltando o pedal, a borboleta fecha e o motor fica a trabalhar ao relanti.",
    cat)
add("Para que serve a bomba eléctrica de gasolina?",
    "Serve para aspirar a gasolina do depósito e enviá-la às injectoras.",
    cat)
add("Como está composta a bomba eléctrica de gasolina?",
    "Um diafragma, uma mola, um filtro, duas válvulas retentoras (entrada e saída), um electro-íman, um vibrador e um par de platinados.",
    cat)
add("Quais são as avarias mais frequentes na bomba eléctrica?",
    "Platinados sujos, abertos ou queimados; enrolamento do electro-íman queimado; diafragma roto ou dilatado; mola partida ou com pouca pressão; válvula entupida.",
    cat)
add("Como funciona a bomba eléctrica de gasolina?",
    "Funciona com corrente eléctrica de baixa tensão vinda da bateria.",
    cat)
add("O que é o carburador e para que serve?",
    "É um órgão do sistema de alimentação. Serve para transformar a gasolina em gás e enviá-la para o interior dos cilindros.",
    cat)
add("Que função tem o carburador além de transformar a gasolina em gás?",
    "Também tem a função de fazer acelerar por intermédio de uma borboleta que regula a quantidade de mistura que deve ir para o interior do cilindro.",
    cat)
add("Onde se encontra o carburador e o que o faz funcionar?",
    "Encontra-se fixo por cima do colector de admissão; o que o faz funcionar são as aspirações do motor, feitas pela descida dos êmbolos.",
    cat)
add("Como está composto o carburador?",
    "Cuba, bóia e agulha, dois gigleres ou pulverizadores (um do máximo e outro do mínimo), duas borboletas (uma de ar e outra de aceleração), câmara de carburação, difusor e válvula de entrada.",
    cat)
add("Em quantas partes divide-se o carburador?",
    "Em duas partes: Cuba e Câmara de carburação.",
    cat)
add("Quais são as principais avarias do carburador?",
    "Agulha presa ou a vedar mal, bóia furada ou larga, gigleres entupidos, borboletas presas e válvula de entrada entupida.",
    cat)
add("Quando é que a gasolina se transforma em gás?",
    "Quando se mistura com o ar na câmara de carburação.",
    cat)
add("Qual é a função da bóia e da agulha existentes na cuba?",
    "Manter o nível certo de gasolina na cuba, controlando a entrada da gasolina enviada ao carburador. Se a bóia romper, o motor não trabalha, porque vai muita gasolina para os cilindros e esta não encontra ar suficiente para arder toda, isolando as velas.",
    cat)
add("O motor pode trabalhar sem o carburador ou sem sistema de injecção?",
    "Não, porque não existe outro órgão capaz de transformar a gasolina em gás.",
    cat)

# ---------- SISTEMA DE ALIMENTAÇÃO DO MOTOR DIESEL ----------
cat = "alimentacao_diesel"
add("Quais são os órgãos do sistema de alimentação do motor diesel?",
    "Reservatório de combustível, tubos condutores, bomba de alimentação, bomba injectora, injectores, filtro de gasóleo, colector de admissão e escape.",
    cat)
add("O que é a bomba injectora e para que serve?",
    "É um dispositivo que serve para puxar e enviar o gasóleo em alta pressão a cada um dos injectores, obrigando-o a sair por pequenos orifícios do bico do injector, entrando em combustão em contacto com o ar.",
    cat)
add("Como está constituída a bomba injectora?",
    "Corpo da bomba, bomba de alimentação, filtro, veio excêntrico, elemento da bomba, régua dentada, válvula de retenção, impulsores e regulador automático.",
    cat)
add("Como está dividida a bomba injectora?",
    "Em três partes: coletores de alimentação, bloco e o cárter.",
    cat)
add("Para que servem os injectores e de que se compõem?",
    "Servem para pulverizar o gasóleo para o interior dos cilindros. Compõem-se de corpo de injector (com orifício de entrada e outro de retorno), porca de afinação, mola, haste e bico do injector.",
    cat)
add("Quem faz funcionar o injector?",
    "A pressão do gasóleo.",
    cat)
add("Quais são as avarias mais frequentes da bomba injectora?",
    "Bomba descomandada, retentores gastos, ar na bomba, bomba de alimentação avariada, impulsores desafinados e régua dentada presa.",
    cat)

# ---------- SISTEMA ELÉCTRICO (OU DE INFLAMAÇÃO) ----------
cat = "sistema_electrico"
add("Quais são os órgãos eléctricos ou de inflamação?",
    "Dínamo gerador ou alternador, conjuntor ou disjuntor, amperímetro, bateria, bobine de ignição, distribuidor, motor de arranque, fios, cabos e velas.",
    cat)
add("Para que serve a bateria?",
    "Serve para armazenar a energia gerada pelo dínamo ou alternador e fornecer aos órgãos que necessitam.",
    cat)
add("Como está composta a bateria?",
    "Um corpo ou carcaça, dois bornos (um positivo e outro negativo), separadores, placas de chumbo e os vasos.",
    cat)
add("Como é que se formata uma bateria nova?",
    "Formata-se com electrólito; depois da utilização deve-se colocar somente água destilada.",
    cat)
add("Quais são as principais avarias da bateria?",
    "Curto-circuito interno, bornos sujos, corpo da bateria estragado e acumuladores estragados.",
    cat)
add("Qual é o tempo de vida de uma bateria?",
    "Tem uma durabilidade de pelo menos dois anos, dependendo dos cuidados de quem usa.",
    cat)
add("Para que serve o motor de arranque?",
    "Serve para dar os primeiros impulsos ao motor por intermédio do carreto bendix, que engrena nos dentes da roda cremalheira.",
    cat)
add("Como está composto o motor de arranque?",
    "Caixa ou carcaça indutoras, induzido, colector, escovas de cobre, carreto bendix e a mola.",
    cat)
add("Quais são as principais avarias do motor de arranque?",
    "Indutoras e induzido queimados, colector sujo e escovas gastas.",
    cat)
add("Qual é a função do distribuidor?",
    "Fornecer a energia de alta tensão às velas de ignição.",
    cat)
add("Como está composto o distribuidor?",
    "Um corpo, dois pares de platinados (um móvel e outro fixo), veio de ressalto e um condensador.",
    cat)
add("Quais são as principais avarias do distribuidor?",
    "Platinados queimados, muito abertos ou muito fechados, veio de ressalto partido, tampa fechada ou húmida, condensador avariado, entre outras.",
    cat)
add("Para que serve a bobine de ignição?",
    "Serve para transformar a corrente baixa em corrente de alta tensão com o abrir e fechar dos platinados.",
    cat)
add("O motor pode trabalhar sem a bobine de ignição?",
    "Não, porque a corrente de baixa tensão não tem capacidade para produzir uma faísca entre os pólos da vela para inflamação da mistura comprimida no interior do cilindro.",
    cat)
add("Quais são as principais avarias da bobine de ignição?",
    "Rolamentos partidos e condutores queimados.",
    cat)
add("Qual é a função das velas de ignição e quais as principais avarias?",
    "Produzir uma faísca de alta tensão no pólo positivo das velas (usadas só nos motores a gasolina), originando uma explosão no interior dos cilindros. É constituída por um corpo, dois pólos (um positivo e outro negativo), cabeça e ensolamento de porcelana. Principais avarias: velas sujas ou queimadas, pólos muito abertos ou fechados e velas quebradas.",
    cat)
add("Quantos tipos de velas conheces?",
    "Dois ou três tipos: velas de ignição e velas de incandescência ou de aquecimento (ajudam o aquecimento dos motores a gasóleo/diesel quando estão frios e têm câmara de pré-combustão).",
    cat)
add("Para que servem os cabos de velas?",
    "Servem de condutores de energia eléctrica para as velas de ignição.",
    cat)
add("O que acontece quando os cabos de velas não são bem protegidos ou cuidados?",
    "Podem causar curto-circuito, danificando a instalação eléctrica do veículo ou mesmo incendiando o próprio veículo.",
    cat)
add("Para que servem os fusíveis?",
    "Servem para proteger a instalação eléctrica em caso de curto-circuito.",
    cat)
add("Para que serve o alternador?",
    "Serve para produzir corrente eléctrica, alimentar a bateria e todos os órgãos eléctricos.",
    cat)
add("Como é que o alternador gera corrente?",
    "Quando o induzido é accionado pela correia de ventoinha, gira entre a indutora, faz surgir corrente alterna no induzido, que vai ao colector, onde transforma em corrente contínua e é captada pelas escovas, passando pelo conjuntor disjuntor e amperímetro até à bateria.",
    cat)
add("Quais são as principais avarias do dínamo gerador ou alternador?",
    "Indutoras queimadas, colector sujo, escovas gastas e corte interno.",
    cat)
add("O que é o conjuntor disjuntor?",
    "É um interruptor automático que serve para dar passagem à corrente eléctrica do alternador à bateria quando o motor estiver a trabalhar.",
    cat)
add("Para que serve o conjuntor disjuntor?",
    "Serve para dar passagem de corrente ao dínamo e à bateria quando o motor pára, evitando que a bateria descarregue sobre o dínamo, queimando o induzido.",
    cat)
add("Para que serve o amperímetro?",
    "Serve para indicar quando o dínamo está a carregar ou a descarregar a bateria. Encontra-se montado no quadro de instrumento.",
    cat)

# ---------- Exportar ----------
with open("/home/claude/cod-iv/data/mecanica.json", "w", encoding="utf-8") as f:
    json.dump(perguntas, f, ensure_ascii=False, indent=2)

print(f"Total de perguntas de mecânica extraídas: {len(perguntas)}")

from collections import Counter
cats = Counter(p["categoria"] for p in perguntas)
for cat_name, count in cats.items():
    print(f"  {cat_name}: {count}")

# Genera pt/index.html a partir de index.html (español).
# Uso, desde la raíz del repo:  python _herramientas/armar_pt.py
# Cada par (es, pt) tiene que aparecer en index.html; si un texto en español cambió, corta y dice cuál:
# hay que actualizar ese par. Al final avisa si quedó en pt/index.html algún texto que parece español.
import re, sys, os

raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src, dst = os.path.join(raiz, "index.html"), os.path.join(raiz, "pt", "index.html")
s = open(src, encoding="utf-8").read()

def rep(a, b, n=None):
    global s
    c = s.count(a)
    if c == 0 or (n is not None and c != n):
        sys.exit(f"ERROR ({c} apariciones): {a[:90]}")
    s = s.replace(a, b)

# ---------- Cabecera ----------
ini = s.index("<script>\n// Idioma:"); fin = s.index("</script>", ini) + len("</script>\n")
s = s[:ini] + s[fin:]                                   # /pt/ no redirige
rep('<html lang="es">', '<html lang="pt-BR">', 1)
rep('''<meta name="description" content="Software para talleres metalúrgicos: nesting de piezas DXF y desarrollos de chapa (T, curvas, conos, transiciones) para CNC de plasma, oxicorte o láser, foto a DXF, y sin CNC: corte de barras, guillotina, rejas, portones y presupuesto. DEMO gratis, PRO 49 USDT.">''',
    '''<meta name="description" content="Software para serralherias e metalúrgicas: nesting de peças DXF e planificação de chapas (T, curvas, cones, transições) para CNC de plasma, oxicorte ou laser, foto para DXF e, sem CNC, corte de barras, guilhotina, grades, portões e orçamento. DEMO grátis, PRO 49 USDT.">''', 1)
rep('<meta property="og:title" content="optiMAX: nesting, desarrollos de chapa y cortes para talleres metalúrgicos">',
    '<meta property="og:title" content="optiMAX: nesting, planificação de chapas e cortes para serralherias e metalúrgicas">', 1)
rep('<meta property="og:description" content="Todo el corte del taller, optimizado en un solo programa: nesting, desarrollos, barras, guillotina, rejas y presupuesto. DEMO gratis para Windows.">',
    '<meta property="og:description" content="Todo o corte da oficina, otimizado em um só programa: nesting, planificações, barras, guilhotina, grades e orçamento. DEMO grátis para Windows.">', 1)
rep('<meta property="og:url" content="https://optimax.lat/">', '<meta property="og:url" content="https://optimax.lat/pt/">\n<meta property="og:locale" content="pt_BR">', 1)
rep('<link rel="canonical" href="https://optimax.lat/">', '<link rel="canonical" href="https://optimax.lat/pt/">', 1)
rep('<title>optiMAX: nesting, desarrollos de chapa y cortes para talleres metalúrgicos</title>',
    '<title>optiMAX: nesting, planificação de chapas e cortes para serralherias e metalúrgicas</title>', 1)

# ---------- Rutas (la página vive en /pt/) ----------
for a in ('src="img/', 'href="img/', 'src="video/', 'poster="video/'):
    rep(a, a.replace('="', '="../'))
rep('href="comun.css"', 'href="../comun.css"', 1)
rep('src="comun.js"', 'src="../comun.js"', 1)
rep('<a href="ayuda/">Ayuda</a>', '<a href="../ayuda/pt/">Ajuda</a>', 1)
rep('<a href="ayuda/">Ayuda del programa</a>', '<a href="../ayuda/pt/">Ajuda do programa</a>', 1)

# ---------- Selector de idioma ----------
rep('<span class="idiomas" role="group" aria-label="Idioma"><span class="idioma actual" title="Español"><svg class="bandera" viewBox="0 0 30 20" aria-hidden="true"><rect width="30" height="20" fill="#c60b1e"/><rect y="5" width="30" height="10" fill="#ffc400"/></svg>ES</span><a class="idioma js-idioma" href="pt/index.html" hreflang="pt-BR" lang="pt-BR" data-idioma="pt" title="Português"><svg class="bandera" viewBox="0 0 30 20" aria-hidden="true"><rect width="30" height="20" fill="#009c3b"/><path d="M15 2.6 27.4 10 15 17.4 2.6 10z" fill="#ffdf00"/><circle cx="15" cy="10" r="4.1" fill="#002776"/></svg>PT</a></span>',
    '<span class="idiomas" role="group" aria-label="Idioma"><a class="idioma js-idioma" href="../index.html" hreflang="es" lang="es" data-idioma="es" title="Español"><svg class="bandera" viewBox="0 0 30 20" aria-hidden="true"><rect width="30" height="20" fill="#c60b1e"/><rect y="5" width="30" height="10" fill="#ffc400"/></svg>ES</a><span class="idioma actual" title="Português"><svg class="bandera" viewBox="0 0 30 20" aria-hidden="true"><rect width="30" height="20" fill="#009c3b"/><path d="M15 2.6 27.4 10 15 17.4 2.6 10z" fill="#ffdf00"/><circle cx="15" cy="10" r="4.1" fill="#002776"/></svg>PT</span></span>', 1)
rep('<span class="idiomas" role="group" aria-label="Idioma"><span class="idioma actual" title="Español"><svg class="bandera" viewBox="0 0 30 20" aria-hidden="true"><rect width="30" height="20" fill="#c60b1e"/><rect y="5" width="30" height="10" fill="#ffc400"/></svg>Español</span><a class="idioma js-idioma" href="pt/index.html" hreflang="pt-BR" lang="pt-BR" data-idioma="pt" title="Português"><svg class="bandera" viewBox="0 0 30 20" aria-hidden="true"><rect width="30" height="20" fill="#009c3b"/><path d="M15 2.6 27.4 10 15 17.4 2.6 10z" fill="#ffdf00"/><circle cx="15" cy="10" r="4.1" fill="#002776"/></svg>Português</a></span>',
    '<span class="idiomas" role="group" aria-label="Idioma"><a class="idioma js-idioma" href="../index.html" hreflang="es" lang="es" data-idioma="es" title="Español"><svg class="bandera" viewBox="0 0 30 20" aria-hidden="true"><rect width="30" height="20" fill="#c60b1e"/><rect y="5" width="30" height="10" fill="#ffc400"/></svg>Español</a><span class="idioma actual" title="Português"><svg class="bandera" viewBox="0 0 30 20" aria-hidden="true"><rect width="30" height="20" fill="#009c3b"/><path d="M15 2.6 27.4 10 15 17.4 2.6 10z" fill="#ffdf00"/><circle cx="15" cy="10" r="4.1" fill="#002776"/></svg>Português</span></span>', 1)

# ---------- Textos del JS ----------
ini = s.index("<script>\n// Textos que arma el JS"); fin = s.index("</script>", ini) + len("</script>")
s = s[:ini] + r'''<script>
// Textos que arma el JS (comun.js), en portugués de Brasil. La versión en español está en ../index.html.
window.T = {
  idioma: "pt-BR",
  urlCompartir: "https://optimax.lat/pt/#descargar",
  dirCopiada: "Endereço copiado", dirSeleccionada: "Endereço selecionado: copie com Ctrl+C",
  idCopiado: "ID copiado", idSeleccionado: "ID selecionado: copie com Ctrl+C",
  enlaceCopiado: "Link copiado: cole no seu WhatsApp ou e-mail e abra no computador.",
  abriEnlace: "Abra este link no seu computador: ",
  compartirTexto: "Baixe a DEMO do optiMAX no computador (Windows):",
  enlaceCorto: "Link para o meu PC", enlaceLargo: "Enviar o link para o meu PC",
  soloPC: "O optiMAX é para PC com Windows: envie o link para você mesmo e baixe no computador.",
  sinDescarga: "O download será liberado nos próximos dias. Enquanto isso, fale com a gente pelo WhatsApp +591 78516826.",
  formas: {binance: "ID da Binance, 49 USDT", usdt: "USDT BEP-20, 49 USDT", qr: "QR do BNB (Bolívia), 590 Bs"},
  comprarBs: "Comprar o PRO por 590 Bs",
  precioBsDetalle: "ou 49 USDT de outros países. Pagamento único, um PC.",
  montoBsDetalle: "ou 49 USDT de outros países · um PC",
  errNombre: "Escreva o nome ou a empresa para a licença.",
  errLargo: "O nome é muito longo: encurte um pouco (máximo de 80 caracteres sem acentos).",
  errCodigo: "O código do PC tem 12 letras e números, por exemplo 5ZS5-FJFM-AJVR. Copie da janela «Ativar optiMAX PRO».",
  mensajeWA: (nome, codigo, forma) => `Olá, paguei o optiMAX PRO.\nNome para a licença: ${nome}\nCódigo do PC: ${codigo}\nForma de pagamento: ${forma}\nSegue o comprovante do pagamento.`,
  tituloVideo: "Vídeo do optiMAX",
  conCnc: "Com a sua CNC", sinCnc: "Sem CNC", de: " de ", anterior: "Anterior: ", siguiente: "Próximo: "
};
</script>''' + s[fin:]

# ---------- Contenido ----------
BR = '<span><svg viewBox="0 0 30 20" aria-hidden="true"><rect width="30" height="20" fill="#009c3b"/><path d="M15 2.6 27.4 10 15 17.4 2.6 10z" fill="#ffdf00"/><circle cx="15" cy="10" r="4.1" fill="#002776"/></svg>Brasil</span>'
m = re.search(r'<span class="paises" aria-label="Para talleres de Bolivia, Perú, Colombia y Paraguay">.*?</span></span>\n', s)
if not m: sys.exit("ERROR: banderas")
s = s[:m.start()] + f'<span class="paises" aria-label="Para serralherias e metalúrgicas do Brasil">{BR}</span>\n' + s[m.end():]

P = [
# Menú y portada
('aria-label="optiMAX, inicio"', 'aria-label="optiMAX, início"'),
('<nav aria-label="Secciones">', '<nav aria-label="Seções">'),
('<a href="#f-foto">Foto a DXF</a>', '<a href="#f-foto">Foto para DXF</a>'),
('<a href="#funciones">Funciones</a>', '<a href="#funciones">Funções</a>'),
('<a href="#desarrollos">Desarrollos</a>', '<a href="#desarrollos">Planificações</a>'),
('<a href="#f-letras">Carteles</a>', '<a href="#f-letras">Placas</a>'),
('<a href="#versiones">DEMO y PRO</a>', '<a href="#versiones">DEMO e PRO</a>'),
('<a href="#comprar">Comprar</a>', '<a href="#comprar">Comprar</a>'),
('<a href="#preguntas">Preguntas</a>', '<a href="#preguntas">Perguntas</a>'),
('href="#descargar">Descargar DEMO</a>', 'href="#descargar">Baixar DEMO</a>'),
('<span class="etiqueta"><i></i>Software para talleres metalúrgicos</span>', '<span class="etiqueta"><i></i>Software para serralherias e metalúrgicas</span>'),
('<h1>Todo el corte del taller, <span class="acento">optimizado</span> en un solo programa</h1>', '<h1>Todo o corte da oficina, <span class="acento">otimizado</span> em um só programa</h1>'),
('<p class="lista-modulos">Nesting – Desarrollos de chapa – Carteles y logos – Foto a DXF – Barras y tubos – Guillotina – Rejas y portones – Presupuesto</p>',
 '<p class="lista-modulos">Nesting – Planificação de chapas – Placas e logos – Foto para DXF – Barras e tubos – Guilhotina – Grades e portões – Orçamento</p>'),
('Descargar DEMO gratis</a>', 'Baixar DEMO grátis</a>'),
('<a class="boton boton-linea" href="#comprar">Comprar PRO por 49 USDT</a>', '<a class="boton boton-linea" href="#comprar">Comprar o PRO por 49 USDT</a>'),
('<span>Windows 10 y 11</span><span>DXF estándar</span><span>En español</span><span>Funciona sin internet</span><span>DEMO sin vencimiento</span>',
 '<span>Windows 10 e 11</span><span>DXF padrão</span><span>Em português</span><span>Funciona sem internet</span><span>DEMO sem vencimento</span>'),
('aria-label="Ampliar captura del nesting"', 'aria-label="Ampliar a captura do nesting"'),
('alt="optiMAX con 72 piezas distribuidas en 8 planchas de 1.000 × 2.000 mm"', 'alt="optiMAX com 72 peças distribuídas em 8 chapas de 1.000 × 2.000 mm"'),
('<figcaption>72 piezas en 8 planchas. De fondo, la mesa plasma del taller donde se desarrolla optiMAX, en Santa Cruz de la Sierra.</figcaption>',
 '<figcaption>72 peças em 8 chapas. Ao fundo, a mesa de plasma da oficina onde o optiMAX é desenvolvido, em Santa Cruz de la Sierra (Bolívia).</figcaption>'),

# Funciones: tarjetas
('<h2>Todo el trabajo de corte en un solo programa</h2>', '<h2>Todo o trabalho de corte em um só programa</h2>'),
('<p>Para talleres que cortan chapa en una CNC y para los que trabajan solo con sierra, guillotina y soldadora. Tocá cada módulo para ver qué hace.</p>',
 '<p>Para oficinas que cortam chapa em uma CNC e para as que trabalham só com serra, guilhotina e máquina de solda. Toque em cada módulo para ver o que ele faz.</p>'),
('<span class="grupo-etq etq-cnc">Con tu CNC</span><span>Piezas para plasma, oxicorte o láser, en DXF estándar</span>',
 '<span class="grupo-etq etq-cnc">Com a sua CNC</span><span>Peças para plasma, oxicorte ou laser, em DXF padrão</span>'),
('<span class="mod-sello">En DEMO</span>', '<span class="mod-sello">Na DEMO</span>'),
('<span class="mod-linea">Distribuye tus DXF en la plancha con el menor desperdicio</span>', '<span class="mod-linea">Distribui seus DXF na chapa com o menor desperdício</span>'),
('<span class="mod-nombre">Desarrollos de chapa<svg', '<span class="mod-nombre">Planificação de chapas<svg'),
('<span class="mod-linea">Injertos en T, curvas, conos, transiciones y helicoides</span>', '<span class="mod-linea">Derivações em T, curvas, cones, transições e helicoides</span>'),
('<span class="mod-nombre">Letras y carteles<svg', '<span class="mod-nombre">Letras e placas<svg'),
('<span class="mod-linea">Texto calado en chapa, con puentes y la forma del cartel</span>', '<span class="mod-linea">Texto vazado na chapa, com pontes e o formato da placa</span>'),
('<span class="mod-nombre">Logos e imágenes<svg', '<span class="mod-nombre">Logos e imagens<svg'),
('<span class="mod-linea">Del PNG o JPG del cliente a una pieza para cortar</span>', '<span class="mod-linea">Do PNG ou JPG do cliente a uma peça para cortar</span>'),
('<span class="mod-sello">Detectar en DEMO</span>', '<span class="mod-sello">Detectar na DEMO</span>'),
('<span class="mod-nombre">Foto a DXF<svg', '<span class="mod-nombre">Foto para DXF<svg'),
('<span class="mod-linea">El contorno medido de una pieza a partir de una foto</span>', '<span class="mod-linea">O contorno medido de uma peça a partir de uma foto</span>'),
('<span class="mod-nombre">Costos y presupuesto<svg', '<span class="mod-nombre">Custos e orçamento<svg'),
('<span class="mod-linea">Metros de corte, tiempo y costo de cada pieza</span>', '<span class="mod-linea">Metros de corte, tempo e custo de cada peça</span>'),
('<span class="grupo-etq etq-sin">Sin CNC</span><span>Para el taller que trabaja con sierra, cizalla y soldadora</span>',
 '<span class="grupo-etq etq-sin">Sem CNC</span><span>Para a oficina que trabalha com serra, tesoura e máquina de solda</span>'),
('<span class="mod-sello">DEMO: 5 piezas</span>', '<span class="mod-sello">DEMO: 5 peças</span>'),
('<span class="mod-nombre">Barras y tubos<svg', '<span class="mod-nombre">Barras e tubos<svg'),
('<span class="mod-linea">Cuántas barras comprar y cómo cortar cada una</span>', '<span class="mod-linea">Quantas barras comprar e como cortar cada uma</span>'),
('<span class="mod-nombre">Guillotina<svg', '<span class="mod-nombre">Guilhotina<svg'),
('<span class="mod-linea">Cortes de lado a lado, numerados en orden</span>', '<span class="mod-linea">Cortes de lado a lado, numerados em ordem</span>'),
('<span class="mod-sello">Reja en DEMO</span>', '<span class="mod-sello">Grade na DEMO</span>'),
('<span class="mod-nombre">Rejas y portones<svg', '<span class="mod-nombre">Grades e portões<svg'),
('<span class="mod-linea">Plano, lista de corte y barras a comprar</span>', '<span class="mod-linea">Desenho, lista de corte e barras a comprar</span>'),

# Funciones: detalle
('<h3>Nesting por forma real <span class="sello sello-demo">DEMO y PRO</span></h3><p>Cargás tus DXF, indicás cantidades y la medida de la plancha. optiMAX prueba decenas de órdenes de colocación en paralelo y se queda con el que usa menos planchas y deja el sobrante más aprovechable.</p>',
 '<h3>Nesting pela forma real <span class="sello sello-demo">DEMO e PRO</span></h3><p>Carregue seus DXF, informe as quantidades e a medida da chapa. O optiMAX testa dezenas de ordens de encaixe em paralelo e fica com a que usa menos chapas e deixa a sobra mais aproveitável.</p>'),
('<li>Piezas irregulares, con agujeros y piezas chicas dentro de los agujeros</li>', '<li>Peças irregulares, com furos e peças pequenas dentro dos furos</li>'),
('<li>Importa un DXF con muchas piezas y agrupa las iguales</li>', '<li>Importa um DXF com muitas peças e agrupa as iguais</li>'),
('<li>Rotación desde 90° hasta libre cada 5°</li>', '<li>Rotação de 90° até livre a cada 5°</li>'),
('<li>Orden de corte optimizado: agujeros primero y mínimo recorrido en vacío</li>', '<li>Ordem de corte otimizada: furos primeiro e o mínimo de deslocamento em vazio</li>'),
('<li>Verifica cada DXF exportado contra la distribución, pieza por pieza</li>', '<li>Confere cada DXF exportado com a distribuição, peça por peça</li>'),
('alt="optiMAX con 72 piezas distribuidas en 8 planchas de 1.000 × 2.000 mm, 71,2 % de aprovechamiento"', 'alt="optiMAX com 72 peças distribuídas em 8 chapas de 1.000 × 2.000 mm, 71,2 % de aproveitamento"'),
('<h3>Desarrollos de chapa <span class="sello sello-pro">PRO</span></h3><p>Completás las medidas y la pieza desarrollada entra directo al nesting. Ves la vista previa antes de agregarla y la podés reeditar después.</p>',
 '<h3>Planificação de chapas <span class="sello sello-pro">PRO</span></h3><p>Preencha as medidas e a peça planificada vai direto para o nesting. Veja a prévia antes de adicionar e edite de novo quando quiser.</p>'),
('<li>Injertos en T a cualquier ángulo y con excentricidad</li>', '<li>Derivações em T (boca de lobo) em qualquer ângulo e com excentricidade</li>'),
('<li>Curvas redondas y rectangulares, conos, transiciones y helicoides</li>', '<li>Curvas redondas e retangulares, cones, transições e helicoides</li>'),
('<li>Agujero en la chapa del caño principal incluido</li>', '<li>Furo na chapa do tubo principal incluído</li>'),
('<li>Plano de armado en PDF con marcas y líneas de plegado</li>', '<li>Plano de montagem em PDF com marcas e linhas de dobra</li>'),
('aria-label="Ampliar captura de Crear pieza"', 'aria-label="Ampliar a captura de Criar peça"'),
('alt="Ventana Crear pieza con el desarrollo de una T cilindro sobre cilindro de 100 mm a 90°"', 'alt="Janela Criar peça com a planificação de um T cilindro sobre cilindro de 100 mm a 90°"'),
('aria-label="Ampliar plano de armado en PDF"', 'aria-label="Ampliar o plano de montagem em PDF"'),
('alt="Plano de armado en PDF de una transición rectangular a redondo de 300 × 300 mm a Ø 100 mm, escala 1:10, con líneas de plegado"', 'alt="Plano de montagem em PDF de uma transição retangular para redondo de 300 × 300 mm para Ø 100 mm, escala 1:10, com linhas de dobra"'),
('<h3>Letras y carteles <span class="sello sello-pro">PRO</span></h3><p>Escribís el texto, elegís la forma del cartel y optiMAX arma la chapa entera con las letras caladas. Los centros de la O, la A, la B o el 0 quedan sostenidos con puentes para que no se caigan.</p>',
 '<h3>Letras e placas <span class="sello sello-pro">PRO</span></h3><p>Escreva o texto, escolha o formato da placa e o optiMAX monta a chapa inteira com as letras vazadas. Os miolos do O, do A, do B ou do 0 ficam presos por pontes para não caírem.</p>'),
('<li>1 o 2 líneas de texto, con 6 fuentes incluidas de uso comercial libre</li>', '<li>1 ou 2 linhas de texto, com 6 fontes incluídas de uso comercial livre</li>'),
('<li>9 formas de cartel: rectángulo, esquinas en chaflán o invertidas, arco, ticket, hexágono, escudo, círculo y óvalo</li>', '<li>9 formatos de placa: retângulo, cantos chanfrados ou invertidos, arco, ticket, hexágono, escudo, círculo e oval</li>'),
('<li>Agujeros para colgar o atornillar, y fondo liso o calado decorativo</li>', '<li>Furos para pendurar ou parafusar, e fundo liso ou vazado decorativo</li>'),
('<li>Sin cartel: solo las letras, al ancho exacto que necesitás, en DXF</li>', '<li>Sem placa: só as letras, na largura exata que você precisa, em DXF</li>'),
('aria-label="Ampliar captura de Letras para cartel"', 'aria-label="Ampliar a captura de Letras para placa"'),
('alt="Ventana Crear pieza con un cartel tipo escudo de 350 × 350 mm con el texto optiMAX 3.2 calado y fondo calado"', 'alt="Janela Criar peça com uma placa tipo escudo de 350 × 350 mm com o texto optiMAX 3.2 vazado e fundo vazado"'),
('alt="El mismo cartel tipo escudo cortado en chapa y pintado de rojo"', 'alt="A mesma placa tipo escudo cortada em chapa e pintada de vermelho"'),
('<h3>Logos e imágenes <span class="sello sello-pro">PRO</span></h3><p>El logo que te manda el cliente en PNG o JPG pasa directo a pieza para cortar. Ponés la medida y optiMAX separa el dibujo del fondo, suaviza el borde y agrega los puentes.</p>',
 '<h3>Logos e imagens <span class="sello sello-pro">PRO</span></h3><p>O logo que o cliente manda em PNG ou JPG vira direto uma peça para cortar. Informe a medida e o optiMAX separa o desenho do fundo, suaviza a borda e adiciona as pontes.</p>'),
('<li>Calado en la chapa o silueta suelta</li>', '<li>Vazado na chapa ou silhueta solta</li>'),
('<li>Separa por color o por claro y oscuro: sirve para logos, escaneos y fotos de un dibujo</li>', '<li>Separa por cor ou por claro e escuro: serve para logos, digitalizações e fotos de um desenho</li>'),
('<li>Limpia manchas y el escalonado de los píxeles</li>', '<li>Limpa manchas e o serrilhado dos pixels</li>'),
('<li>Con o sin cartel alrededor, con las mismas formas y agujeros que las letras</li>', '<li>Com ou sem placa em volta, com os mesmos formatos e furos das letras</li>'),
('aria-label="Ampliar captura de Logo / imagen"', 'aria-label="Ampliar a captura de Logo / imagem"'),
('alt="Ventana Crear pieza con un logo de león calado en un cartel de 300 × 300 mm con esquinas invertidas"', 'alt="Janela Criar peça com um logo de leão vazado em uma placa de 300 × 300 mm com cantos invertidos"'),
('alt="Panel de chapa roja con un león calado"', 'alt="Painel de chapa vermelha com um leão vazado"'),
('<h3>Pieza desde una foto <span class="sello sello-demo">Detectar en DEMO</span> <span class="sello sello-pro">PRO</span></h3><p>Sacás una foto de una pieza apoyada sobre la hoja de calibración y optiMAX te da el contorno medido, listo para el nesting.</p>',
 '<h3>Peça a partir de uma foto <span class="sello sello-demo">Detectar na DEMO</span> <span class="sello sello-pro">PRO</span></h3><p>Tire uma foto da peça apoiada sobre a folha de calibração e o optiMAX entrega o contorno medido, pronto para o nesting.</p>'),
('<li>Detecta rectas, arcos y círculos con sus medidas</li>', '<li>Detecta retas, arcos e círculos com suas medidas</li>'),
('<li>Ajustás el contorno si hace falta</li>', '<li>Ajuste o contorno se precisar</li>'),
('<li>Lo agregás al nesting o lo exportás en DXF (PRO)</li>', '<li>Adicione ao nesting ou exporte em DXF (PRO)</li>'),
('aria-label="Ampliar captura de Pieza desde una foto"', 'aria-label="Ampliar a captura de Peça a partir de uma foto"'),
('alt="Ventana Pieza desde una foto con el contorno detectado"', 'alt="Janela Peça a partir de uma foto com o contorno detectado"'),
('<h3>Costos y presupuesto <span class="sello sello-pro">PRO</span></h3><p>Con el precio de la chapa y los datos de tu máquina calcula metros de corte, perforaciones, tiempo estimado y costo de cada pieza.</p>',
 '<h3>Custos e orçamento <span class="sello sello-pro">PRO</span></h3><p>Com o preço da chapa e os dados da sua máquina, calcula metros de corte, perfurações, tempo estimado e custo de cada peça.</p>'),
('<li>Descuenta el sobrante que se puede reutilizar</li>', '<li>Desconta a sobra que pode ser reaproveitada</li>'),
('<li>Presupuesto en PDF interno o versión para el cliente</li>', '<li>Orçamento em PDF interno ou versão para o cliente</li>'),
('<li>Moneda y datos de tu empresa configurables</li>', '<li>Moeda e dados da sua empresa configuráveis</li>'),
('aria-label="Ampliar captura del presupuesto"', 'aria-label="Ampliar a captura do orçamento"'),
('alt="Presupuesto del trabajo: 72 piezas, 123 m de corte, 1 h 55 min estimados"', 'alt="Orçamento do trabalho: 72 peças, 123 m de corte, 1 h 55 min estimados"'),
('<h3>Barras, tubos y angulares <span class="sello sello-demo">DEMO hasta 5 piezas</span> <span class="sello sello-pro">PRO</span></h3><p>Optimiza el corte de perfiles en barras de largo fijo. Pegás la lista desde Excel y obtenés cuántas barras comprar y cómo cortar cada una.</p>',
 '<h3>Barras, tubos e cantoneiras <span class="sello sello-demo">DEMO até 5 peças</span> <span class="sello sello-pro">PRO</span></h3><p>Otimiza o corte de perfis em barras de comprimento fixo. Cole a lista do Excel e veja quantas barras comprar e como cortar cada uma.</p>'),
('<li>Largo de barra y ancho de corte a elección</li>', '<li>Comprimento da barra e largura do corte à sua escolha</li>'),
('<li>Lista de corte en PDF con la medida de cada tramo</li>', '<li>Lista de corte em PDF com a medida de cada pedaço</li>'),
('<li>Precio por pieza según el costo de la barra</li>', '<li>Preço por peça conforme o custo da barra</li>'),
('aria-label="Ampliar captura de barras"', 'aria-label="Ampliar a captura de barras"'),
('alt="Corte de 79 piezas de ángulo 40×40×3 en 20 barras de 6.000 mm con 94,5 % de aprovechamiento"', 'alt="Corte de 79 peças de cantoneira 40×40×3 em 20 barras de 6.000 mm com 94,5 % de aproveitamento"'),
('<h3>Guillotina (cizalla) <span class="sello sello-demo">DEMO hasta 5 piezas</span> <span class="sello sello-pro">PRO</span></h3><p>Para rectángulos que cortás con cizalla: cortes de lado a lado, como trabaja la máquina, respetando el largo máximo de corte.</p>',
 '<h3>Guilhotina (tesoura) <span class="sello sello-demo">DEMO até 5 peças</span> <span class="sello sello-pro">PRO</span></h3><p>Para retângulos cortados na tesoura: cortes de lado a lado, como a máquina trabalha, respeitando o comprimento máximo de corte.</p>'),
('<li>Cortes numerados en el orden en que se hacen</li>', '<li>Cortes numerados na ordem em que são feitos</li>'),
('<li>Plan de cortes en PDF para llevar a la máquina</li>', '<li>Plano de cortes em PDF para levar à máquina</li>'),
('aria-label="Ampliar captura de guillotina"', 'aria-label="Ampliar a captura da guilhotina"'),
('alt="Ventana de guillotina con 18 piezas en 3 planchas y 25 cortes"', 'alt="Janela da guilhotina com 18 peças em 3 chapas e 25 cortes"'),
('aria-label="Ampliar plan de cortes en PDF"', 'aria-label="Ampliar o plano de cortes em PDF"'),
('alt="Plan de cortes de guillotina en PDF con los cortes numerados"', 'alt="Plano de cortes da guilhotina em PDF com os cortes numerados"'),
('<h3>Rejas y portones <span class="sello sello-demo">Reja en DEMO</span> <span class="sello sello-pro">Portones PRO</span></h3><p>Ponés el ancho y el alto del portón o la reja, elegís los perfiles y el relleno, y te arma el plano con todas las medidas, la lista de corte con cada pieza marcada y cuántas barras comprar de cada perfil.</p>',
 '<h3>Grades e portões <span class="sello sello-demo">Grade na DEMO</span> <span class="sello sello-pro">Portões PRO</span></h3><p>Informe a largura e a altura do portão ou da grade, escolha os perfis e o preenchimento, e o programa monta o desenho com todas as medidas, a lista de corte com cada peça marcada e quantas barras comprar de cada perfil.</p>'),
('<li>Reja, portón batiente de 1 y 2 hojas y portón corredizo</li>', '<li>Grade, portão de abrir de 1 e 2 folhas e portão de correr</li>'),
('<li>Relleno vertical, horizontal, diagonal, rombos, cuadrícula, cruz o chapa ciega</li>', '<li>Preenchimento vertical, horizontal, diagonal, losangos, quadriculado, cruz ou chapa fechada</li>'),
('<li>Cortes a 45° con croquis; peso, metros de soldadura y m² de pintura</li>', '<li>Cortes a 45° com croqui; peso, metros de solda e m² de pintura</li>'),
('<li>Plano en PDF, DXF y copia para Excel (PRO); perfiles en mm o pulgadas</li>', '<li>Desenho em PDF, DXF e cópia para o Excel (PRO); perfis em mm ou polegadas</li>'),
('<li>En la DEMO: reja de ventana de hasta 1.500 × 1.000 mm</li>', '<li>Na DEMO: grade de janela de até 1.500 × 1.000 mm</li>'),
('aria-label="Ampliar captura de rejas y portones"', 'aria-label="Ampliar a captura de grades e portões"'),
('alt="Ventana Rejas y portones con un portón batiente de 2 hojas de 3.000 × 2.100 mm: 28 piezas, 10 barras, 57 kg"', 'alt="Janela Grades e portões com um portão de abrir de 2 folhas de 3.000 × 2.100 mm: 28 peças, 10 barras, 57 kg"'),
('aria-label="Ampliar plano con medidas en PDF"', 'aria-label="Ampliar o desenho com medidas em PDF"'),
('alt="Plano en PDF del portón batiente de 2 hojas con cotas acumuladas y piezas marcadas por letra"', 'alt="Desenho em PDF do portão de abrir de 2 folhas com cotas acumuladas e peças marcadas por letra"'),

# Catálogo
('<h2>Catálogo de piezas</h2>', '<h2>Catálogo de peças</h2>'),
('<p>Las formas básicas y la curva redonda por sectores vienen en la DEMO. El resto de los desarrollos es parte de la PRO.</p>', '<p>As formas básicas e a curva redonda por gomos vêm na DEMO. As demais planificações fazem parte do PRO.</p>'),
('<span>Rectángulo</span>', '<span>Retângulo</span>'),
('<span>Disco / arandela</span>', '<span>Disco / arruela</span>'),
('<span>Brida</span>', '<span>Flange</span>'),
('<span>Curva redonda por sectores</span>', '<span>Curva redonda por gomos</span>'),
('<span>T ramal rectangular sobre caño</span>', '<span>T ramal retangular sobre tubo</span>'),
('<span>T ramal redondo sobre caja</span>', '<span>T ramal redondo sobre duto retangular</span>'),
('<span>Curva rectangular</span>', '<span>Curva retangular</span>'),
('<span>Curva directa 90°</span>', '<span>Curva direta 90°</span>'),
('<span>Curva directa</span>', '<span>Curva direta</span>'),
('<span>Desvío circular paralelo</span>', '<span>Desvio circular paralelo</span>'),
('<span>Tronco de cono / reducción</span>', '<span>Tronco de cone / redução</span>'),
('<span>Transición rectangular a redondo</span>', '<span>Transição retangular para redondo</span>'),
('<span>Helicoide (hélice de sinfín)</span>', '<span>Helicoide (hélice de rosca transportadora)</span>'),
('<p class="nota-tecnica">Las medidas se cargan como diámetros y secciones exteriores; el desarrollo se calcula sobre el espesor neutro de la chapa. Las líneas de plegado llevan muescas en V opcionales y van al plano PDF, nunca al DXF de corte.</p>',
 '<p class="nota-tecnica">As medidas são informadas como diâmetros e seções externas; a planificação é calculada na linha neutra da espessura da chapa. As linhas de dobra levam entalhes em V opcionais e vão para o plano em PDF, nunca para o DXF de corte.</p>'),

# Video y taller
('<h2>Miralo funcionando</h2>', '<h2>Veja funcionando</h2>'),
('<p>Nesting, desarrollos, guillotina, portones, tolvas y pieza desde una foto.</p>', '<p>Nesting, planificações, guilhotina, portões, tremonhas e peça a partir de uma foto. Vídeo com o programa em espanhol.</p>'),
('aria-label="Reproducir el video de optiMAX"', 'aria-label="Reproduzir o vídeo do optiMAX"'),
('alt="Video de optiMAX: uso completo del programa"', 'alt="Vídeo do optiMAX: uso completo do programa"'),
('<h2>Hecho en un taller que corta todos los días</h2>', '<h2>Feito numa oficina que corta todos os dias</h2>'),
('<p>optiMAX nació para resolver el corte de nuestras propias máquinas de chapa y angulares. Cada función se pensó con un problema real del taller.</p>',
 '<p>O optiMAX nasceu para resolver o corte das nossas próprias máquinas de chapa e cantoneiras. Cada função foi pensada a partir de um problema real da oficina.</p>'),
('alt="Pieza de chapa cortada con plasma y armada en el taller"><figcaption>Pieza cortada y armada</figcaption>', 'alt="Peça de chapa cortada a plasma e montada na oficina"><figcaption>Peça cortada e montada</figcaption>'),
('aria-label="Arco de plasma cortando"></video><figcaption>Corte en curso</figcaption>', 'aria-label="Arco de plasma cortando"></video><figcaption>Corte em andamento</figcaption>'),
('alt="Máquinas agrícolas de chapa terminadas en el taller"><figcaption>Máquinas terminadas</figcaption>', 'alt="Máquinas agrícolas de chapa prontas na oficina"><figcaption>Máquinas prontas</figcaption>'),
('alt="Tolvas de chapa en fabricación"><figcaption>Tolvas en fabricación</figcaption>', 'alt="Tremonhas de chapa em fabricação"><figcaption>Tremonhas em fabricação</figcaption>'),

# DEMO y PRO
('<h2>DEMO y PRO</h2>', '<h2>DEMO e PRO</h2>'),
('<p>La DEMO no vence y ya hace el nesting completo. La PRO suma los desarrollos, los portones, los costos, los proyectos y quita los límites de barras, guillotina y rejas.</p>',
 '<p>A DEMO não vence e já faz o nesting completo. O PRO acrescenta as planificações, os portões, os custos e os projetos, e tira os limites de barras, guilhotina e grades.</p>'),
('<div class="monto">Gratis<small>Sin vencimiento</small></div>', '<div class="monto">Grátis<small>Sem vencimento</small></div>'),
('<li>Nesting completo y DXF de todas las planchas</li>', '<li>Nesting completo e DXF de todas as chapas</li>'),
('<li>Formas básicas y curva redonda por sectores</li>', '<li>Formas básicas e curva redonda por gomos</li>'),
('<li>Foto a DXF: detectar, medir y editar</li>', '<li>Foto para DXF: detectar, medir e editar</li>'),
('<li>Barras y guillotina hasta 5 piezas</li>', '<li>Barras e guilhotina até 5 peças</li>'),
('<li>Reja de ventana hasta 1.500 × 1.000 mm</li>', '<li>Grade de janela até 1.500 × 1.000 mm</li>'),
('<span class="cinta">PAGO ÚNICO</span>', '<span class="cinta">PAGAMENTO ÚNICO</span>'),
('<div class="monto js-precio-pro">49 USDT<small>o 590 Bs desde Bolivia · una PC</small></div>', '<div class="monto js-precio-pro">49 USDT<small>ou 590 Bs pelo QR boliviano · um PC</small></div>'),
('<li>Todo lo de la DEMO, sin límites</li>', '<li>Tudo da DEMO, sem limites</li>'),
('<li>Los 10 desarrollos de chapa</li>', '<li>As 10 planificações de chapa</li>'),
('<li>Foto a DXF al nesting y exportar</li>', '<li>Foto para DXF: adicionar ao nesting e exportar</li>'),
('<li>Todos los portones, con DXF, PDF y Excel</li>', '<li>Todos os portões, com DXF, PDF e Excel</li>'),
('<li>Costos, presupuesto y proyectos guardados</li>', '<li>Custos, orçamento e projetos salvos</li>'),
('<a class="boton boton-rojo" href="#comprar">Comprar PRO</a>', '<a class="boton boton-rojo" href="#comprar">Comprar o PRO</a>'),
('<a class="boton boton-linea" href="#comprar">Comprar PRO</a>', '<a class="boton boton-linea" href="#comprar">Comprar o PRO</a>'),
('<summary>Ver la comparación completa</summary>', '<summary>Ver a comparação completa</summary>'),
('<th scope="col">Función</th><th scope="col">DEMO<small>Gratis</small></th><th scope="col" class="col-pro">PRO<small>49 USDT o 590 Bs, pago único</small></th>',
 '<th scope="col">Função</th><th scope="col">DEMO<small>Grátis</small></th><th scope="col" class="col-pro">PRO<small>49 USDT ou 590 Bs, pagamento único</small></th>'),
('<td>Nesting por forma real, DXF con varias piezas y orden de corte optimizado</td>', '<td>Nesting pela forma real, DXF com várias peças e ordem de corte otimizada</td>'),
('<td class="si">Sí</td>', '<td class="si">Sim</td>'),
('<td class="si col-pro">Sí</td>', '<td class="si col-pro">Sim</td>'),
('<td class="no">No</td>', '<td class="no">Não</td>'),
('<td>Niveles de cálculo</td><td class="parcial">Rápido y Normal (hasta 24 órdenes)</td><td class="parcial col-pro">+ Profundo y Máximo</td>',
 '<td>Profundidade do cálculo</td><td class="parcial">Rápido e Normal (até 24 ordens)</td><td class="parcial col-pro">+ Profundo e Máximo</td>'),
('<td>Exportar el DXF de todas las planchas (R12, con arcos)</td>', '<td>Exportar o DXF de todas as chapas (R12, com arcos)</td>'),
('<td>Plano de armado en PDF y pesos</td>', '<td>Plano de montagem em PDF e pesos</td>'),
('<td>Costos, tiempo de corte y presupuesto en PDF</td>', '<td>Custos, tempo de corte e orçamento em PDF</td>'),
('<td>Guardar y abrir proyectos</td>', '<td>Salvar e abrir projetos</td>'),
('<td>Formas básicas y curva redonda por sectores</td>', '<td>Formas básicas e curva redonda por gomos</td>'),
('<td>Los otros 10 desarrollos (T, curvas, cono, transición, desvío, helicoide)</td>', '<td>As outras 10 planificações (T, curvas, cone, transição, desvio, helicoide)</td>'),
('<td>Foto a DXF: detectar, medir y editar</td>', '<td>Foto para DXF: detectar, medir e editar</td>'),
('<td>Foto a DXF: agregar al nesting y exportar el DXF</td>', '<td>Foto para DXF: adicionar ao nesting e exportar o DXF</td>'),
('<td>Barras, tubos y guillotina: calcular y dibujar</td><td class="parcial">Hasta 5 piezas</td><td class="parcial col-pro">Sin límite</td>',
 '<td>Barras, tubos e guilhotina: calcular e desenhar</td><td class="parcial">Até 5 peças</td><td class="parcial col-pro">Sem limite</td>'),
('<td>Barras y guillotina: precio por pieza, PDF y Excel</td>', '<td>Barras e guilhotina: preço por peça, PDF e Excel</td>'),
('<td>Rejas y portones: plano, lista de corte y barras</td><td class="parcial">Reja de ventana hasta 1.500 × 1.000 mm</td><td class="parcial col-pro">Todos los tipos y medidas</td>',
 '<td>Grades e portões: desenho, lista de corte e barras</td><td class="parcial">Grade de janela até 1.500 × 1.000 mm</td><td class="parcial col-pro">Todos os tipos e medidas</td>'),
('<td>Rejas y portones: DXF, PDF, Excel y costos</td>', '<td>Grades e portões: DXF, PDF, Excel e custos</td>'),
('<td>Ajustes del sistema</td><td class="parcial">Edita materiales (sin precio ni velocidad); el resto solo lo ve</td><td class="parcial col-pro">Todo</td>',
 '<td>Configurações do sistema</td><td class="parcial">Edita materiais (sem preço nem velocidade); o resto só visualiza</td><td class="parcial col-pro">Tudo</td>'),
('<td>Actualizaciones gratis</td>', '<td>Atualizações grátis</td>'),

# Descargar
('<h2>Descargá la DEMO</h2>', '<h2>Baixe a DEMO</h2>'),
('<p>optiMAX es un programa de escritorio para Windows. Se instala como cualquier programa, sin nada extra.</p>', '<p>O optiMAX é um programa de computador para Windows. Instala como qualquer programa, sem nada extra.</p>'),
('<dt>Sistema</dt><dd>Windows 10 u 11 de 64 bits</dd>', '<dt>Sistema</dt><dd>Windows 10 ou 11 de 64 bits</dd>'),
('<dt>Procesador</dt><dd>x64 de 4 núcleos o más recomendado; el cálculo usa varios núcleos a la vez</dd>', '<dt>Processador</dt><dd>x64 de 4 núcleos ou mais recomendado; o cálculo usa vários núcleos ao mesmo tempo</dd>'),
('<dt>Memoria</dt><dd>4 GB mínimo, 8 GB recomendado</dd>', '<dt>Memória</dt><dd>4 GB mínimo, 8 GB recomendado</dd>'),
('<dt>Disco</dt><dd>Unos 300 MB libres</dd>', '<dt>Disco</dt><dd>Cerca de 300 MB livres</dd>'),
('<dt>Pantalla</dt><dd>1366 × 768 o mayor</dd>', '<dt>Tela</dt><dd>1366 × 768 ou maior</dd>'),
('<dt>Archivos</dt><dd>Lee y exporta DXF; detecta si el dibujo está en milímetros o pulgadas</dd>', '<dt>Arquivos</dt><dd>Lê e exporta DXF; detecta se o desenho está em milímetros ou polegadas</dd>'),

# Comprar
('<h2>Comprar optiMAX PRO</h2>', '<h2>Comprar o optiMAX PRO</h2>'),
('<div class="precio" style="margin-top:22px"><b>49 USDT</b><span>o 590 Bs desde Bolivia. Pago único, una PC.</span></div>', '<div class="precio" style="margin-top:22px"><b>49 USDT</b><span>ou 590 Bs pelo QR boliviano. Pagamento único, um PC.</span></div>'),
('<li><div><b>Instalá la DEMO</b><span>En la ventana «Activar optiMAX PRO» aparece el código de tu PC.</span></div></li>', '<li><div><b>Instale a DEMO</b><span>Na janela «Ativar optiMAX PRO» aparece o código do seu PC.</span></div></li>'),
('<li><div><b>Pagá la licencia</b><span>Desde cualquier país, 49 USDT al ID de Binance o por la red BNB Smart Chain (BEP-20). Desde Bolivia, también 590 Bs con el QR del BNB.</span></div></li>',
 '<li><div><b>Pague a licença</b><span>De qualquer país, 49 USDT para o ID da Binance ou pela rede BNB Smart Chain (BEP-20). Ou 590 Bs com o QR do Banco Nacional da Bolívia.</span></div></li>'),
('<li><div><b>Mandanos tus datos y la captura por WhatsApp</b><span>Completá tu nombre y el código de tu PC: se arma el mensaje solo y le adjuntás la captura del pago.</span></div></li>',
 '<li><div><b>Envie seus dados e o comprovante pelo WhatsApp</b><span>Preencha seu nome e o código do seu PC: a mensagem é montada sozinha e você anexa o comprovante do pagamento.</span></div></li>'),
('<li><div><b>Recibí tu clave PRO</b><span>Verificamos el pago y te enviamos la clave para activar en esa PC.</span></div></li>', '<li><div><b>Receba sua chave PRO</b><span>Conferimos o pagamento e enviamos a chave para ativar nesse PC.</span></div></li>'),
('<p><b>Una licencia, una PC.</b> La clave queda atada al equipo.</p>', '<p><b>Uma licença, um PC.</b> A chave fica vinculada ao computador.</p>'),
('<p><b>Sin devoluciones.</b> Probá la DEMO con tus propios DXF antes de comprar.</p>', '<p><b>Sem reembolso.</b> Teste a DEMO com os seus próprios DXF antes de comprar.</p>'),
('aria-label="Forma de pago"', 'aria-label="Forma de pagamento"'),
('aria-selected="true">ID de Binance<small>49 USDT</small></button>', 'aria-selected="true">ID da Binance<small>49 USDT</small></button>'),
('aria-selected="false">Otra billetera<small>USDT BEP-20</small></button>', 'aria-selected="false">Outra carteira<small>USDT BEP-20</small></button>'),
('aria-selected="false">Desde Bolivia<small>QR, 590 Bs</small></button>', 'aria-selected="false">QR boliviano<small>590 Bs</small></button>'),
('<small>ID de Binance</small>', '<small>ID da Binance</small>'),
('id="copiar-id">Copiar ID</button>', 'id="copiar-id">Copiar ID</button>'),
('<div class="pago-red"><span>ID de Binance</span><span>Monto: 49 USDT</span></div>', '<div class="pago-red"><span>ID da Binance</span><span>Valor: 49 USDT</span></div>'),
('<p class="tenue">Nombre de la cuenta: <b style="color:var(--texto)">GMSoftware</b></p>', '<p class="tenue">Nome da conta: <b style="color:var(--texto)">GMSoftware</b></p>'),
('<p class="tenue">En la app de Binance: <b style="color:var(--texto)">Activos → USDT → Enviar → Enviar a usuario de Binance</b>. Pegá el ID y enviá 49 USDT.</p>',
 '<p class="tenue">No app da Binance: <b style="color:var(--texto)">Ativos → USDT → Enviar → Enviar para usuário da Binance</b>. Cole o ID e envie 49 USDT.</p>'),
('<p class="tenue">Es una transferencia entre cuentas de Binance: llega al instante y sin comisión.</p>', '<p class="tenue">É uma transferência entre contas da Binance: chega na hora e sem taxa.</p>'),
('<ul class="avisos"><li>Guardá la captura del pago: la vas a mandar por WhatsApp.</li></ul>', '<ul class="avisos"><li>Guarde o comprovante do pagamento: você vai enviá-lo pelo WhatsApp.</li></ul>'),
('<div class="pago-red"><span>USDT en red BNB Smart Chain (BEP-20)</span><span>Monto: 49 USDT</span></div>', '<div class="pago-red"><span>USDT na rede BNB Smart Chain (BEP-20)</span><span>Valor: 49 USDT</span></div>'),
('aria-label="Código QR de la dirección de pago"', 'aria-label="Código QR do endereço de pagamento"'),
('id="copiar">Copiar dirección</button>', 'id="copiar">Copiar endereço</button>'),
('<li>Desde cualquier billetera o exchange: Binance, MEXC, Bybit, etc.</li>', '<li>De qualquer carteira ou exchange: Binance, MEXC, Bybit etc.</li>'),
('<li>Usá solamente la red BNB Smart Chain (BEP-20). Si enviás por otra red (TRC-20, ERC-20) el dinero puede perderse.</li>', '<li>Use somente a rede BNB Smart Chain (BEP-20). Se enviar por outra rede (TRC-20, ERC-20), o dinheiro pode ser perdido.</li>'),
('<li>Enviá 49 USDT. La comisión de la red corre por nuestra cuenta.</li>', '<li>Envie 49 USDT. A taxa da rede fica por nossa conta.</li>'),
('<li>Guardá la captura del envío: la vas a mandar por WhatsApp.</li>', '<li>Guarde o comprovante do envio: você vai enviá-lo pelo WhatsApp.</li>'),
('alt="QR de cobro del Banco Nacional de Bolivia por 590 Bs, concepto licencia optiMAX PRO"', 'alt="QR de cobrança do Banco Nacional da Bolívia de 590 Bs, referente à licença optiMAX PRO"'),
('<div class="pago-red"><span>QR del Banco Nacional de Bolivia</span><span>Monto: 590 Bs</span></div>', '<div class="pago-red"><span>QR do Banco Nacional da Bolívia</span><span>Valor: 590 Bs</span></div>'),
('<p class="tenue">Escaneá el QR con la app de tu banco o billetera. El monto ya está cargado.</p>', '<p class="tenue">Escaneie o QR com o app do seu banco ou carteira. O valor já está preenchido.</p>'),
('<p class="tenue">Si estás mirando la página desde el celular, guardá el QR y cargalo desde la galería en la app de tu banco.</p>', '<p class="tenue">Se estiver vendo a página no celular, salve o QR e abra pela galeria no app do seu banco.</p>'),
('download="QR-optiMAX-PRO.jpg">Guardar QR</a>', 'download="QR-optiMAX-PRO.jpg">Salvar QR</a>'),
('<ul class="avisos"><li>Guardá la captura del comprobante: la vas a mandar por WhatsApp.</li></ul>', '<ul class="avisos"><li>Guarde o comprovante: você vai enviá-lo pelo WhatsApp.</li></ul>'),
('<label for="nombre-lic">Nombre o empresa para la licencia', '<label for="nombre-lic">Nome ou empresa para a licença'),
('placeholder="Así aparece en «Acerca de» del programa"', 'placeholder="Assim aparece em «Sobre» no programa"'),
('<label for="codigo-pc">Código de tu PC (ventana «Activar optiMAX PRO»)', '<label for="codigo-pc">Código do seu PC (janela «Ativar optiMAX PRO»)'),
('placeholder="Ej.: 5ZS5-FJFM-AJVR"', 'placeholder="Ex.: 5ZS5-FJFM-AJVR"'),
('type="submit">Preparar mensaje de WhatsApp</button>', 'type="submit">Preparar mensagem de WhatsApp</button>'),
('<p><b>Último paso:</b> enviá el mensaje y adjuntá la captura del pago.</p>', '<p><b>Último passo:</b> envie a mensagem e anexe o comprovante do pagamento.</p>'),
('aria-label="Código QR para abrir WhatsApp en el celular"', 'aria-label="Código QR para abrir o WhatsApp no celular"'),
('<span class="tenue">¿Pagaste desde el celular? Escaneá este QR con la cámara: se abre WhatsApp con el mensaje listo para adjuntar la captura.</span>',
 '<span class="tenue">Pagou pelo celular? Escaneie este QR com a câmera: o WhatsApp abre com a mensagem pronta para anexar o comprovante.</span>'),
('rel="noopener">Enviar por WhatsApp</a>', 'rel="noopener">Enviar pelo WhatsApp</a>'),
('<span class="tenue">Abre WhatsApp en este dispositivo.</span>', '<span class="tenue">Abre o WhatsApp neste dispositivo.</span>'),
('WhatsApp de ventas: <span', 'WhatsApp de vendas: <span'),
('<p class="tenue" style="font-size:.9rem">¿Dudas antes de comprar? Preguntale a nuestro asistente:</p>', '<p class="tenue" style="font-size:.9rem">Dúvidas antes de comprar? Pergunte ao nosso assistente:</p>'),
('<span>Escribinos tu consulta</span>', '<span>Envie sua dúvida</span>'),

# Preguntas
('<h2>Preguntas frecuentes</h2><p>¿Tenés otra pregunta? Escribile a nuestro asistente por WhatsApp, contesta al instante.</p>', '<h2>Perguntas frequentes</h2><p>Tem outra pergunta? Escreva para o nosso assistente pelo WhatsApp, ele responde na hora.</p>'),
('<summary>¿Sirve para mi máquina CNC?</summary><p>optiMAX exporta un DXF estándar por plancha, solo con las líneas de corte y en el orden optimizado. Ese archivo lo abre el programa de tu máquina de plasma, oxicorte o láser (FastCAM u otro), que agrega entradas, compensación y velocidad como siempre. En el taller lo usamos con FastCAM en una plasma.</p>',
 '<summary>Serve para a minha máquina CNC?</summary><p>O optiMAX exporta um DXF padrão por chapa, só com as linhas de corte e na ordem otimizada. Esse arquivo é aberto pelo programa da sua máquina de plasma, oxicorte ou laser (FastCAM ou outro), que adiciona entradas, compensação e velocidade como sempre. Na nossa oficina usamos com o FastCAM em uma plasma.</p>'),
('<summary>¿Me sirve si no tengo CNC?</summary><p>Sí. El corte de barras y tubos, la guillotina y las rejas y portones no necesitan CNC: te dicen cuántas barras o planchas comprar y cómo cortar cada una, con la lista de cortes para la sierra o la guillotina. El nesting, los desarrollos y la foto a DXF generan archivos a escala real para cortar en una CNC.</p>',
 '<summary>Serve se eu não tiver CNC?</summary><p>Sim. O corte de barras e tubos, a guilhotina e as grades e portões não precisam de CNC: mostram quantas barras ou chapas comprar e como cortar cada uma, com a lista de cortes para a serra ou a guilhotina. O nesting, as planificações e a foto para DXF geram arquivos em escala real para cortar em uma CNC.</p>'),
('<summary>¿Windows muestra un aviso de seguridad al instalar?</summary><p>Es un control habitual de Windows al instalar. Tocá «Más información» y después «Ejecutar de todas formas». optiMAX está <a class="js-vt" target="_blank" rel="noopener">verificado con 68 antivirus</a>, sin ninguna detección. En Windows 11 la ventana se ve distinta, pero los botones son los mismos. Si usás Edge y la descarga queda en pausa, tocá «…» sobre la descarga y «Conservar». Descargalo siempre desde optimax.lat.</p>',
 '<summary>O Windows mostra um aviso de segurança ao instalar?</summary><p>É uma verificação normal do Windows ao instalar. Clique em «Mais informações» e depois em «Executar assim mesmo». O optiMAX foi <a class="js-vt" target="_blank" rel="noopener">verificado com 68 antivírus</a>, sem nenhuma detecção. No Windows 11 a janela é diferente, mas os botões são os mesmos. Se usar o Edge e o download ficar pausado, clique em «…» sobre o download e em «Manter». Baixe sempre em optimax.lat.</p>'),
('<summary>¿Necesita internet?</summary><p>No. El programa y la activación de la PRO funcionan sin conexión.</p>', '<summary>Precisa de internet?</summary><p>Não. O programa e a ativação do PRO funcionam sem conexão.</p>'),
('<summary>¿La DEMO tiene vencimiento?</summary><p>No. Podés usarla todo el tiempo que quieras, con los límites de la tabla DEMO y PRO.</p>', '<summary>A DEMO tem vencimento?</summary><p>Não. Você pode usar pelo tempo que quiser, com os limites da tabela DEMO e PRO.</p>'),
('<summary>¿Puedo usar la licencia en dos computadoras?</summary><p>No. Cada clave sirve para una PC. Para otra computadora hace falta otra licencia.</p>', '<summary>Posso usar a licença em dois computadores?</summary><p>Não. Cada chave serve para um PC. Para outro computador é preciso outra licença.</p>'),
('<summary>¿Puedo pagar de otra forma?</summary><p>Desde cualquier país, 49 USDT al ID de Binance (entre cuentas de Binance) o por la red BNB Smart Chain (BEP-20) desde cualquier billetera o exchange. Desde Bolivia, también 590 Bs con el QR del Banco Nacional de Bolivia. Por ahora no hay otras formas de pago.</p>',
 '<summary>Posso pagar de outra forma?</summary><p>De qualquer país, 49 USDT para o ID da Binance (entre contas da Binance) ou pela rede BNB Smart Chain (BEP-20) de qualquer carteira ou exchange. Também 590 Bs com o QR do Banco Nacional da Bolívia. Por enquanto não há outras formas de pagamento.</p>'),

# Pie, barra móvil, flotante y diálogos
('<span>Desarrollado por GMSoftware, Santa Cruz de la Sierra, Bolivia</span>', '<span>Desenvolvido pela GMSoftware, Santa Cruz de la Sierra, Bolívia</span>'),
('<span>Ventas: +591 77626675</span>', '<span>Vendas: +591 77626675</span>'),
('data-movil="Enviar la DEMO a mi PC"', 'data-movil="Enviar a DEMO para o meu PC"'),
('aria-label="Consultas por WhatsApp, asistente automático"', 'aria-label="Dúvidas pelo WhatsApp, assistente automático"'),
('</svg><span>Consultas</span></a>', '</svg><span>Dúvidas</span></a>'),
('aria-label="Detalle del módulo"', 'aria-label="Detalhe do módulo"'),
('aria-label="Cerrar">✕</button>', 'aria-label="Fechar">✕</button>'),
('aria-label="Captura ampliada"', 'aria-label="Captura ampliada"'),
('<button type="button" id="cerrar-visor">Cerrar</button>', '<button type="button" id="cerrar-visor">Fechar</button>'),
('<h2 id="instalar-titulo">Tu descarga empezó</h2>', '<h2 id="instalar-titulo">Seu download começou</h2>'),
('<p class="tenue">Para instalar, abrí el archivo descargado.</p>', '<p class="tenue">Para instalar, abra o arquivo baixado.</p>'),
('''<p class="instalar-aviso"><b>¿Windows muestra un aviso de seguridad?</b> Es un control habitual de Windows al instalar.
      Tocá «Más información» y después «Ejecutar de todas formas». optiMAX está
      <a class="js-vt" target="_blank" rel="noopener">verificado con 68 antivirus</a>, sin ninguna detección.</p>''',
 '''<p class="instalar-aviso"><b>O Windows mostra um aviso de segurança?</b> É uma verificação normal do Windows ao instalar.
      Clique em «Mais informações» e depois em «Executar assim mesmo». O optiMAX foi
      <a class="js-vt" target="_blank" rel="noopener">verificado com 68 antivírus</a>, sem nenhuma detecção.</p>'''),
('alt="Ventana «Windows protegió su PC» con «Más información» marcado"', 'alt="Janela «O Windows protegeu o computador» com «Mais informações» marcado"'),
('<div><span class="num">1</span>Tocá <b>«Más información»</b></div>', '<div><span class="num">1</span>Clique em <b>«Mais informações»</b></div>'),
('alt="Ventana «Windows protegió su PC» con «Ejecutar de todas formas» marcado"', 'alt="Janela «O Windows protegeu o computador» com «Executar assim mesmo» marcado"'),
('<div><span class="num">2</span>Tocá <b>«Ejecutar de todas formas»</b></div>', '<div><span class="num">2</span>Clique em <b>«Executar assim mesmo»</b></div>'),
('''<li class="ancho"><div><span class="num">3</span>Si Windows pregunta si permitís que la aplicación haga cambios, tocá
        <b>«Sí»</b>. En el instalador de optiMAX aceptá las condiciones de uso y seguí con <b>«Siguiente»</b> hasta
        <b>«Instalar»</b>.</div></li>''',
 '''<li class="ancho"><div><span class="num">3</span>Se o Windows perguntar se você permite que o aplicativo faça alterações, clique em
        <b>«Sim»</b>. No instalador do optiMAX, aceite as condições de uso e siga com <b>«Avançar»</b> até
        <b>«Instalar»</b>.</div></li>'''),
('<p class="instalar-nota tenue">En Windows 11 la ventana se ve distinta, pero los botones son los mismos.</p>', '<p class="instalar-nota tenue">No Windows 11 a janela é diferente, mas os botões são os mesmos. As imagens mostram o Windows em espanhol.</p>'),
('<p class="instalar-nota tenue">¿Usás Edge y la descarga quedó en pausa? Tocá «…» sobre la descarga y «Conservar».</p>', '<p class="instalar-nota tenue">Usa o Edge e o download ficou pausado? Clique em «…» sobre o download e em «Manter».</p>'),
('''<details><summary>¿Por qué Windows pide confirmar?</summary>
      <p>Windows pide una confirmación extra con los programas que no tienen un certificado de firma digital de pago, y
      optiMAX se distribuye sin ese certificado. El instalador es el que publica GMSoftware en su repositorio oficial de
      GitHub: descargalo siempre desde optimax.lat.</p></details>''',
 '''<details><summary>Por que o Windows pede confirmação?</summary>
      <p>O Windows pede uma confirmação extra para programas que não têm um certificado pago de assinatura digital, e
      o optiMAX é distribuído sem esse certificado. O instalador é o que a GMSoftware publica no seu repositório oficial no
      GitHub: baixe sempre em optimax.lat.</p></details>'''),
('<span>¿Dudas para instalar? Escribinos</span>', '<span>Dúvidas para instalar? Fale com a gente</span>'),
('<span class="tenue">¿No empezó? <a id="descarga-otra" href="#">Descargalo de nuevo</a></span>', '<span class="tenue">Não começou? <a id="descarga-otra" href="#">Baixe de novo</a></span>'),
]
for a, b in P:
    rep(a, b)

open(dst, "w", encoding="utf-8").write(s)
print("pt/index.html generado,", len(P), "pares")

# Control: textos visibles que parecen haber quedado en español (palabras que no existen en portugués)
v = re.sub(r"<script.*?</script>|<style.*?</style>|<svg.*?</svg>", "", s, flags=re.S)
textos = [t.strip() for t in re.sub(r"<[^>]+>", "\n", v).split("\n") if t.strip()]
textos += re.findall(r'(?:alt|aria-label|placeholder|title|content)="([^"]*)"', v)
esp = re.compile(r"\b(el|los|las|del|una|un|es|con|desde|hasta|tu|tus|pieza|piezas|plancha|planchas|también|y|ción|ciones)\b|ñ|¿|¡", re.I)
dudosos = [t for t in textos if esp.search(t) and t not in ("Español", "ES")
           and "Santa Cruz de la Sierra" not in t]
for t in dudosos: print("  ¿sin traducir?", t[:120])
if dudosos: sys.exit(1)

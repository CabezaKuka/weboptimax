/* Código común de optimax.lat (español) y optimax.lat/pt/ (portugués).
   Los textos que arma el JS vienen de window.T, definido en cada página antes de cargar este archivo. */
const T = window.T;

/* ===== Configuración: cambiar solo esto ===== */
const CONFIG = {
  direccionPago: "0xb4cd33650f254214ed24188ed087f6848add00d1",  // USDT en BNB Smart Chain (BEP-20)
  idBinance: "211223373",     // ID de Binance (transferencia entre usuarios de Binance)
  urlDescarga: "https://github.com/CabezaKuka/optimax-descargas/releases/latest/download/optiMAX_Setup.exe",
  virusTotal: "https://www.virustotal.com/gui/file/30e18a4ecebf462709de0d66eef38cbbe3848314cfd9a002184437ca48932d55",  // análisis del instalador optiMAX_Setup.exe (0/67, 20/11/2026); actualizar si se cambia el .exe
  whatsapp: "59177626675",            // ventas (comprobantes), solo dígitos
  whatsappConsultas: "59178516826",   // asistente de consultas, solo dígitos
  qrBancoVence: "2028-10-25"          // QR del BNB (590 Bs): generar uno nuevo antes de esta fecha
};
/* =========================================== */

// Dirección y QR
const dir = document.getElementById("direccion");
dir.textContent = CONFIG.direccionPago;
document.querySelectorAll(".js-consultas").forEach(a => a.href = `https://wa.me/${CONFIG.whatsappConsultas}`);
try {
  new QRCode(document.getElementById("qr"), {text: CONFIG.direccionPago, width: 136, height: 136, correctLevel: QRCode.CorrectLevel.M});
} catch (e) { document.getElementById("qr").hidden = true; }

// Copiar al portapapeles (si el navegador no deja, queda seleccionado para Ctrl+C)
function copiarTexto(boton, nodo, texto, aviso, listo, seleccionado) {
  boton.addEventListener("click", () => {
    const marcar = () => { const r = document.createRange(); r.selectNodeContents(nodo); const s = getSelection(); s.removeAllRanges(); s.addRange(r); };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(texto)
        .then(() => { aviso.textContent = listo; })
        .catch(() => { marcar(); aviso.textContent = seleccionado; });
    } else { marcar(); aviso.textContent = seleccionado; }
  });
}
copiarTexto(document.getElementById("copiar"), dir, CONFIG.direccionPago, document.getElementById("copiado"),
            T.dirCopiada, T.dirSeleccionada);
const idb = document.getElementById("id-binance");
idb.textContent = CONFIG.idBinance;
copiarTexto(document.getElementById("copiar-id"), idb, CONFIG.idBinance, document.getElementById("copiado-id"),
            T.idCopiado, T.idSeleccionado);

// Descarga: arranca sola (enlace directo) y a la vez se abren los pasos de instalación
const instalar = document.getElementById("instalar");
document.getElementById("descarga-otra").href = CONFIG.urlDescarga || "#descargar";
document.querySelectorAll(".js-vt").forEach(vt => { if (CONFIG.virusTotal) vt.href = CONFIG.virusTotal; });  // sin URL queda como texto
document.getElementById("cerrar-instalar").addEventListener("click", () => instalar.close());
instalar.addEventListener("click", ev => { if (ev.target === instalar) instalar.close(); });
// Celular o tablet: el .exe no sirve ahí, así que el botón ofrece mandarse el enlace para abrirlo en la PC
const esMovil = (() => {
  try {
    if (navigator.userAgentData && navigator.userAgentData.mobile) return true;
    const ua = navigator.userAgent || "";
    if (/Android|iPhone|iPad|iPod|Mobile|Windows Phone/i.test(ua)) return true;
    return navigator.platform === "MacIntel" && navigator.maxTouchPoints > 1;   // iPad que se presenta como Mac
  } catch (e) { return false; }
})();
function avisoDescarga(a, texto) {
  document.querySelectorAll(".js-mensaje-descarga").forEach(m => m.textContent = "");
  const zona = a.closest("section") || document;
  const m = zona.querySelector(".js-mensaje-descarga") || document.querySelector(".js-mensaje-descarga");
  if (m) m.textContent = texto;
}
function compartirEnlace(a) {
  const url = T.urlCompartir;   // enlace que se manda a sí mismo quien entra desde el celular
  const listo = T.enlaceCopiado;
  const copiar = () => {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(url).then(() => avisoDescarga(a, listo))
        .catch(() => avisoDescarga(a, T.abriEnlace + url));
    } else avisoDescarga(a, T.abriEnlace + url);
  };
  if (navigator.share) {
    navigator.share({title: "optiMAX DEMO", text: T.compartirTexto, url: url})
      .catch(err => { if (!err || err.name !== "AbortError") copiar(); });
  } else copiar();
}
if (esMovil) {
  document.querySelectorAll(".js-descarga").forEach(a => {
    a.textContent = a.dataset.movil || (a.classList.contains("boton-chico") ? T.enlaceCorto : T.enlaceLargo);
    a.href = "#descargar";
    a.addEventListener("click", ev => { ev.preventDefault(); compartirEnlace(a); });
  });
  document.querySelectorAll(".js-mensaje-descarga").forEach(m =>
    m.textContent = T.soloPC);
}
document.querySelectorAll(".js-descarga").forEach(a => {
  if (esMovil) return;
  if (CONFIG.urlDescarga) {
    a.href = CONFIG.urlDescarga;
    a.addEventListener("click", () => setTimeout(() => { if (instalar.showModal && !instalar.open) instalar.showModal(); }, 150));
    return;
  }
  a.addEventListener("click", ev => {
    ev.preventDefault();
    document.querySelectorAll(".js-mensaje-descarga").forEach(m => m.textContent = "");
    const zona = a.closest("section") || document;
    const m = zona.querySelector(".js-mensaje-descarga") || document.querySelector(".js-mensaje-descarga");
    m.textContent = T.sinDescarga;
  });
});

// Pestañas de forma de pago, en este orden: ID de Binance, USDT BEP-20, QR del BNB
// (en Bolivia abre la del QR; en otros países, la del ID de Binance)
const FORMAS = T.formas;   // {binance, usdt, qr}: el orden de las claves es el de las pestañas
let formaPago = "binance";
function elegirPago(forma) {
  formaPago = forma;
  for (const f of Object.keys(FORMAS)) {
    document.getElementById("tab-" + f).setAttribute("aria-selected", String(f === forma));
    document.getElementById("panel-" + f).hidden = f !== forma;
  }
  document.getElementById("mensaje-form").textContent = "";
  if (!document.getElementById("envio").hidden) prepararMensaje(false);   // el mensaje ya armado cambia de forma de pago
}
for (const f of Object.keys(FORMAS)) document.getElementById("tab-" + f).addEventListener("click", () => elegirPago(f));
document.querySelector(".pestanas").addEventListener("keydown", ev => {
  if (ev.key !== "ArrowRight" && ev.key !== "ArrowLeft") return;
  const orden = Object.keys(FORMAS), k = orden.indexOf(formaPago);
  const otra = orden[(k + (ev.key === "ArrowRight" ? 1 : orden.length - 1)) % orden.length];
  elegirPago(otra); document.getElementById("tab-" + otra).focus();
});
try {
  if (Intl.DateTimeFormat().resolvedOptions().timeZone === "America/La_Paz") {
    elegirPago("qr");
    // Desde Bolivia el precio se muestra en bolivianos
    const comprar = document.querySelector('.portada a[href="#comprar"]');
    if (comprar) comprar.textContent = T.comprarBs;
    const precio = document.querySelector(".precio");
    if (precio) {
      precio.querySelector("b").textContent = "590 Bs";
      precio.querySelector("span").textContent = T.precioBsDetalle;
    }
    document.querySelectorAll(".js-precio-pro").forEach(m =>
      m.innerHTML = "590 Bs<small>" + T.montoBsDetalle + "</small>");
  }
} catch (e) {}

// Código de PC: mismas reglas que el programa (12 caracteres de base32; 0, 1 y 8 se leen como O, I y B)
function normalizarCodigo(c) {
  let t = String(c).toUpperCase().replace(/[^A-Z0-9]/g, "");
  t = t.replace(/0/g, "O").replace(/1/g, "I").replace(/8/g, "B");
  if (t.length !== 12 || /[^A-Z2-7]/.test(t)) return null;
  return t.slice(0, 4) + "-" + t.slice(4, 8) + "-" + t.slice(8);
}
// El programa abre la página con ?codigo=XXXX-XXXX-XXXX#comprar: se completa solo
try {
  const c = new URLSearchParams(location.search).get("codigo");
  const n = c && normalizarCodigo(c);
  if (n) document.getElementById("codigo-pc").value = n;
} catch (e) {}

// Nombre: el generador de claves acepta hasta 80 bytes (las letras con tilde ocupan 2)
const bytes = t => new TextEncoder().encode(t).length;

function prepararMensaje(mostrarErrores) {
  const msg = document.getElementById("mensaje-form");
  const nombre = document.getElementById("nombre-lic").value.split(/\s+/).filter(Boolean).join(" ");
  const campoCod = document.getElementById("codigo-pc");
  if (!nombre) { if (mostrarErrores) msg.textContent = T.errNombre; return false; }
  if (bytes(nombre) > 80) { if (mostrarErrores) msg.textContent = T.errLargo; return false; }
  const codigo = normalizarCodigo(campoCod.value);
  if (!codigo) {
    if (mostrarErrores) msg.textContent = T.errCodigo;
    return false;
  }
  campoCod.value = codigo;
  msg.textContent = "";
  const texto = T.mensajeWA(nombre, codigo, FORMAS[formaPago]);
  const url = `https://wa.me/${CONFIG.whatsapp}?text=${encodeURIComponent(texto)}`;
  document.getElementById("abrir-wa").href = url;
  document.getElementById("vista-msg").textContent = texto;
  const caja = document.getElementById("qr-wa");
  caja.innerHTML = "";
  try { new QRCode(caja, {text: url, width: 360, height: 360, correctLevel: QRCode.CorrectLevel.L}); }
  catch (e) { caja.parentElement.hidden = true; }
  document.getElementById("envio").hidden = false;
  return true;
}

document.getElementById("form-comprobante").addEventListener("submit", ev => {
  ev.preventDefault();
  if (prepararMensaje(true)) document.getElementById("envio").scrollIntoView({behavior: "smooth", block: "nearest"});
});
["nombre-lic", "codigo-pc"].forEach(id => document.getElementById(id).addEventListener("input", () => {
  document.getElementById("envio").hidden = true;          // si cambian los datos, se vuelve a preparar
}));

// Píxel de Meta: clics que interesan (si un bloqueador frena el píxel, no pasa nada)
// Todos los eventos llevan el idioma de la página (es / pt-BR) para medir Brasil aparte
const conIdioma = datos => Object.assign({idioma: T.idioma}, datos || {});
function evento(nombre, datos) { try { if (window.fbq) fbq("track", nombre, conIdioma(datos)); } catch (e) {} }
function eventoPropio(nombre, datos) { try { if (window.fbq) fbq("trackCustom", nombre, conIdioma(datos)); } catch (e) {} }
document.querySelectorAll(".js-descarga").forEach(a => a.addEventListener("click", () => {
  if (esMovil) eventoPropio("EnlacePC", {content_name: "optiMAX DEMO"});   // celular: no es una descarga
  else evento("Lead", {content_name: "optiMAX DEMO"});                     // PC: descarga real
}));
document.getElementById("abrir-wa").addEventListener("click", () =>
  evento("InitiateCheckout", formaPago === "qr" ? {content_name: "optiMAX PRO", value: 590, currency: "BOB"}
                                                : {content_name: "optiMAX PRO", value: 49, currency: "USD"}));
document.querySelectorAll(".js-consultas").forEach(a => a.addEventListener("click", () => evento("Contact")));

// Visor de capturas
const visor = document.getElementById("visor"), vimg = document.getElementById("visor-img");
document.querySelectorAll(".js-ampliar").forEach(b => b.addEventListener("click", () => {
  const img = b.querySelector("img"); vimg.src = img.src; vimg.alt = img.alt;
  if (visor.showModal) visor.showModal();
}));
document.getElementById("cerrar-visor").addEventListener("click", () => visor.close());
visor.addEventListener("click", ev => { if (ev.target === visor) visor.close(); });

// Aparición al hacer scroll, cifras que cuentan y barra fija del celular
(() => {
  const quieto = matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (!("IntersectionObserver" in window)) return;
  const contar = b => {
    const fin = parseFloat(b.dataset.contar), dec = +(b.dataset.dec || 0), nodo = b.firstChild, t0 = performance.now();
    const fmt = v => v.toFixed(dec).replace(".", ",");
    const paso = t => { const k = Math.min(1, (t - t0) / 1200); nodo.textContent = fmt(fin * (1 - Math.pow(1 - k, 3))); if (k < 1) requestAnimationFrame(paso); };
    requestAnimationFrame(paso);
  };
  if (!quieto) {
    const sel = ".intro, .video-yt, .col-foto, .mods-grupo, .cifras .dato, .catalogo, .taller figure, .plan, .requisitos div, .pasos li, .pago, .preguntas";
    const obs = new IntersectionObserver(es => es.forEach(e => {
      if (!e.isIntersecting) return;
      e.target.classList.add("visto"); obs.unobserve(e.target);
      e.target.querySelectorAll("[data-contar]").forEach(contar);
    }), {rootMargin: "0px 0px -8% 0px"});
    document.querySelectorAll(sel).forEach((el, i) => {
      el.classList.add("revelar");
      const hermanos = el.parentElement ? [...el.parentElement.children].indexOf(el) : 0;
      el.style.transitionDelay = Math.min(hermanos, 5) * 70 + "ms";
      obs.observe(el);
    });
  }
  const barra = document.getElementById("barra-movil"), portada = document.querySelector(".portada");
  if (barra && portada) new IntersectionObserver(([e]) => barra.classList.toggle("activa", !e.isIntersecting)).observe(portada);
})();

// Video de YouTube: el reproductor se carga recién al tocar
document.querySelectorAll(".js-video-yt").forEach(b => b.addEventListener("click", () => {
  const f = document.createElement("iframe");
  f.src = "https://www.youtube-nocookie.com/embed/" + b.dataset.id + "?autoplay=1&rel=0&modestbranding=1";
  f.title = T.tituloVideo;
  f.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture";
  f.allowFullscreen = true;
  f.referrerPolicy = "strict-origin-when-cross-origin";
  b.replaceWith(f);
  eventoPropio("VerVideo");
}));

// Funciones: tarjetas de módulos con detalle emergente (anterior / siguiente)
(() => {
  const dlg = document.getElementById("mod-detalle"), fuente = document.querySelector(".mod-fuente");
  if (!dlg || !fuente || !dlg.showModal) return;
  const cuerpo = dlg.querySelector(".md-cuerpo"), caja = dlg.querySelector(".md-caja");
  const tarjetas = [...document.querySelectorAll(".mod")], ids = tarjetas.map(t => t.dataset.mod);
  const nombre = k => tarjetas[(k + ids.length) % ids.length].querySelector(".mod-nombre").textContent;
  const ant = dlg.querySelector(".md-ant"), sig = dlg.querySelector(".md-sig");
  let i = -1, origen = null;
  const mostrar = (k, usuario) => {
    const previo = cuerpo.firstElementChild; if (previo) fuente.appendChild(previo);
    i = (k + ids.length) % ids.length;
    const art = document.getElementById(ids[i]); art.hidden = false; cuerpo.appendChild(art);
    caja.scrollTop = 0;
    const sinCnc = art.classList.contains("sin-cnc");
    dlg.classList.toggle("sin-cnc", sinCnc);
    dlg.querySelector(".md-grupo").textContent = sinCnc ? T.sinCnc : T.conCnc;
    dlg.querySelector(".md-cuenta").textContent = (i + 1) + T.de + ids.length;
    ant.querySelector("span").textContent = nombre(i - 1);
    sig.querySelector("span").textContent = nombre(i + 1);
    ant.setAttribute("aria-label", T.anterior + nombre(i - 1));
    sig.setAttribute("aria-label", T.siguiente + nombre(i + 1));
    if (usuario) eventoPropio("VerModulo", {modulo: ids[i].slice(2)});
  };
  const abrir = (id, desde) => {
    origen = desde || null;
    mostrar(ids.indexOf(id), true);
    if (!dlg.open) dlg.showModal();
  };
  tarjetas.forEach(t => t.addEventListener("click", () => abrir(t.dataset.mod, t)));
  ant.addEventListener("click", () => mostrar(i - 1, true));
  sig.addEventListener("click", () => mostrar(i + 1, true));
  dlg.querySelector(".md-cerrar").addEventListener("click", () => dlg.close());
  dlg.addEventListener("click", ev => { if (ev.target === dlg) dlg.close(); });
  dlg.addEventListener("keydown", ev => {
    if (ev.key === "ArrowRight") { ev.preventDefault(); mostrar(i + 1, true); }
    else if (ev.key === "ArrowLeft") { ev.preventDefault(); mostrar(i - 1, true); }
  });
  // Celular: deslizar de costado para pasar de módulo
  let x0 = null, y0 = 0;
  cuerpo.addEventListener("touchstart", ev => { const t = ev.touches[0]; x0 = t.clientX; y0 = t.clientY; }, {passive: true});
  cuerpo.addEventListener("touchend", ev => {
    if (x0 === null) return;
    const t = ev.changedTouches[0], dx = t.clientX - x0, dy = t.clientY - y0; x0 = null;
    if (Math.abs(dx) > 60 && Math.abs(dx) > 1.5 * Math.abs(dy)) mostrar(i + (dx < 0 ? 1 : -1), true);
  }, {passive: true});
  dlg.addEventListener("close", () => {
    if (ids.includes(location.hash.slice(1))) history.replaceState(null, "", location.pathname + location.search);
    if (origen) { origen.focus({preventScroll: true}); origen = null; }
  });
  dlg.querySelector(".md-descarga").addEventListener("click", () => {
    eventoPropio("DescargaDesdeModulo", {modulo: ids[i].slice(2)});
    if (!esMovil) dlg.close();
  });
  // Enlaces del menú (#f-foto, #f-letras…) abren el detalle de ese módulo
  const deHash = () => {
    const h = location.hash.slice(1); if (!ids.includes(h)) return;
    document.getElementById("funciones").scrollIntoView({block: "start"});
    abrir(h);
  };
  addEventListener("hashchange", deHash);
  deHash();
})();

// Videos: respetar movimiento reducido
if (matchMedia("(prefers-reduced-motion: reduce)").matches) {
  document.querySelectorAll("video[autoplay]").forEach(v => { v.removeAttribute("autoplay"); v.pause(); if (!v.classList.contains("fondo-portada")) v.controls = true; });
}

// Selector de idioma: guarda la elección (así la portada no vuelve a redirigir) y conserva ?codigo= y el #ancla
document.querySelectorAll(".js-idioma").forEach(a => a.addEventListener("click", () => {
  try { localStorage.setItem("ox_idioma", a.dataset.idioma); } catch (e) {}
  a.href = a.getAttribute("href").split(/[?#]/)[0] + location.search + location.hash;
}));

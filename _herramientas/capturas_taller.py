"""Capturas de la vista 3D de optiMAX Taller para la página taller/ (taller/img/3d-*.webp y og.jpg).

Abre la app (repo optimax-pwa, con el código PRO enlazado en pro/ para ver los portones) en un navegador sin pantalla,
arma cada trabajo con los botones de la app, abre la vista 3D, esconde la barra, los avisos y los botones y saca la
foto al doble de resolución (después se achica, para que los bordes salgan suaves).

    pip install playwright pillow
    python _herramientas/capturas_taller.py --app RUTA/optimax-pwa [--chrome /usr/bin/google-chrome] [--solo porton]

RUTA/optimax-pwa/pro tiene que ser el repo privado optimax-pwa-pro (enlace o carpeta): la app lo carga con ?pro=1.
Escribe en taller/img/ (al lado de esta carpeta). Si cambia la app (colores, 3D, alrededor), volver a correrlo.
"""
import argparse
import os
import subprocess
import sys
import time

from PIL import Image
from playwright.sync_api import sync_playwright

AQUI = os.path.dirname(os.path.abspath(__file__))
SALIDA = os.path.join(AQUI, "..", "taller", "img")
PUERTO = 8791
# la vista sin la barra de arriba, los avisos, los botones de alrededor ni la ayuda
CSS = ".p-completa-barra,.p-3d-aviso,.p-3d-ayuda,.p-3d-entorno{display:none!important}"


def portones(pg, base):
    """Entra a Rejas y portones con la PRO de desarrollo (?pro=1) y el trabajo de muestra."""
    pg.goto(base + "?pro=1#chapa")
    pg.wait_for_selector("#chapas li")
    pg.evaluate("localStorage.removeItem('optimax-portones')")
    pg.goto(base + "#portones")
    pg.wait_for_selector("#p-lista li")


def esperar(pg):
    pg.wait_for_timeout(1500)
    pg.wait_for_selector("#p-opt", state="hidden", timeout=30000)
    if pg.is_visible("#p-error"):
        raise RuntimeError(pg.inner_text("#p-error"))


def foto_3d(pg, entorno, nombre, ancho, alto, mover=None):
    """Abre la vista 3D con el alrededor pedido y guarda la foto (ancho × alto px; se saca al doble)."""
    pg.set_viewport_size({"width": ancho // 2, "height": alto // 2})
    pg.wait_for_timeout(300)
    pg.click("#p-3d")
    pg.wait_for_selector(".p-3d[data-piezas]", timeout=20000)
    pg.wait_for_timeout(1200)
    if entorno:
        pg.click(f".p-3d-entorno label:has-text('{entorno}')")
        pg.wait_for_timeout(500)
    estilo = pg.add_style_tag(content=CSS)
    if mover:
        mover(pg)
    pg.wait_for_timeout(900)
    tmp = os.path.join(SALIDA, f"_{nombre}.png")
    pg.locator(".p-3d-lienzo canvas").screenshot(path=tmp)
    estilo.evaluate("e => e.remove()")
    pg.click(".p-3d .p-c-cerrar")
    img = Image.open(tmp).convert("RGB")
    img = img.resize((ancho, alto), Image.LANCZOS) if img.size != (ancho, alto) else img
    destino = os.path.join(SALIDA, nombre)
    if nombre.endswith(".jpg"):
        img.save(destino, quality=86, optimize=True)
    else:
        img.save(destino, quality=82, method=6)
    os.remove(tmp)
    print(f"  {nombre}: {ancho} × {alto}")


def acercar(pasos):
    def mover(pg):
        caja = pg.locator(".p-3d-lienzo canvas").bounding_box()
        pg.mouse.move(caja["x"] + caja["width"] / 2, caja["y"] + caja["height"] / 2)
        for _ in range(abs(pasos)):
            pg.mouse.wheel(0, -120 if pasos > 0 else 120)
            pg.wait_for_timeout(60)
    return mover


def porton(pg, base):
    """Portada y og.jpg: batiente de 2 hojas de barrotes entre columnas."""
    portones(pg, base)
    pg.click(".p-tarjeta[data-v=batiente_2]")
    pg.fill("#p-ancho", "3000")
    pg.fill("#p-alto", "1800")
    esperar(pg)
    foto_3d(pg, "Columnas", "3d-porton.webp", 1200, 780, acercar(2))
    foto_3d(pg, "Columnas", "og.jpg", 1200, 630, acercar(2))


def corredizo(pg, base):
    portones(pg, base)
    pg.click(".p-tarjeta[data-v=corredizo]")
    pg.fill("#p-ancho", "3500")
    pg.fill("#p-alto", "1800")
    esperar(pg)
    foto_3d(pg, "Paredes", "3d-corredizo.webp", 1200, 780, acercar(2))


def reja(pg, base):
    """Reja de ventana de rombos, sobrepuesta en el hueco de la pared."""
    portones(pg, base)
    pg.click(".p-tarjeta[data-v=reja_ventana]")
    pg.click(".p-tarjeta[data-v=rombos]")
    pg.fill("#p-ancho", "1200")
    pg.fill("#p-alto", "1000")
    pg.fill("#p-sob_lat", "50")
    pg.fill("#p-sob_arr", "50")
    pg.fill("#p-sob_abj", "50")
    esperar(pg)
    foto_3d(pg, "Pared", "3d-reja.webp", 800, 800, acercar(1))


def panos(pg, base):
    """Travesaño doble con barrotes en la franja y chapa en 3 paños a lo ancho, entre paredes."""
    portones(pg, base)
    pg.click(".p-tarjeta[data-v=batiente_2]")
    pg.click(".p-tarjeta[data-v=chapa]")
    pg.fill("#p-ancho", "3000")
    pg.fill("#p-alto", "1800")
    pg.check("input[name=p-trav_modo][value=doble]")
    pg.fill("#p-franja", "220")
    for _ in range(5):
        pg.click("[data-paso=n_franja][data-d='1']")
    for _ in range(2):
        pg.click("[data-paso=n_panos][data-d='1']")
    esperar(pg)
    foto_3d(pg, "Paredes", "3d-panos.webp", 1200, 780, acercar(2))


CAPTURAS = {"porton": porton, "corredizo": corredizo, "reja": reja, "panos": panos}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--app", required=True, help="repo optimax-pwa (con pro/ = optimax-pwa-pro)")
    ap.add_argument("--chrome", default="/usr/bin/google-chrome" if os.path.exists("/usr/bin/google-chrome") else None)
    ap.add_argument("--solo", choices=sorted(CAPTURAS), action="append")
    a = ap.parse_args()
    if not os.path.isdir(os.path.join(a.app, "pro")):
        sys.exit("Falta pro/ en la app (el repo optimax-pwa-pro): sin la PRO no se ven los portones.")
    os.makedirs(SALIDA, exist_ok=True)
    srv = subprocess.Popen([sys.executable, "-m", "http.server", str(PUERTO), "-d", a.app],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1)
    base = f"http://localhost:{PUERTO}/"
    try:
        with sync_playwright() as p:
            b = p.chromium.launch(executable_path=a.chrome, args=["--no-sandbox"])
            pg = b.new_page(viewport={"width": 600, "height": 390}, device_scale_factor=2)
            errores = []
            pg.on("pageerror", lambda e: errores.append(str(e)))
            for nombre in a.solo or CAPTURAS:
                print(nombre)
                CAPTURAS[nombre](pg, base)
            b.close()
            if errores:
                sys.exit(f"Errores de la app: {errores}")
    finally:
        srv.terminate()


if __name__ == "__main__":
    main()

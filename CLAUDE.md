# weboptimax: notas para Claude

Sitio estático de optiMAX (software de nesting y corte para talleres metalúrgicos), publicado con GitHub Pages desde la rama `main` en https://optimax.lat (archivo `CNAME`). Dos idiomas: `index.html` (español, con voseo) y `pt/index.html` (portugués de Brasil). Las dos usan los mismos `comun.css` y `comun.js`, y las mismas `img/` y `video/`.

## Idiomas (español y portugués)

- **`comun.js`** tiene toda la lógica y el bloque `CONFIG` (dirección de pago, ID de Binance, URL de descarga, WhatsApp, vencimiento del QR): se cambia una sola vez para las dos páginas. Los textos que arma el JS (mensaje de WhatsApp, avisos, «Comprar PRO por 590 Bs», etc.) vienen de `window.T`, definido al final de cada página.
- **`pt/index.html` no se edita a mano**: se genera desde `index.html` con `python _herramientas/armar_pt.py` (tabla de pares español → portugués). Después de cambiar un texto en español, correr el script: si corta, actualizar o agregar el par en la tabla. Al final avisa si quedó algo en español. `_herramientas/` empieza con guion bajo, así que GitHub Pages no la publica.
- **Redirección:** el script del principio de `index.html` pasa a `/pt/` si el navegador está en portugués, o si en el selector se eligió portugués (`localStorage` `ox_idioma`). Conserva `?codigo=` y `#comprar`, porque el botón «Comprar no site» del programa en portugués abre `https://optimax.lat/?codigo=…#comprar`. No sacarlo mientras el programa use esa dirección.
- Selector con banderas SVG (España y Brasil; los emojis de banderas no se ven en Windows): `ES` · `PT` en la barra y nombres completos en el pie. Hasta 1023 px el menú se oculta para que entren selector y botón. La página pt enlaza «Ajuda» a `../ayuda/pt/`.
- Píxel: es el mismo en las dos páginas. Todos los eventos llevan `idioma` (`es` / `pt-BR`) para medir Brasil aparte.
- Glosario y nombres de módulos en portugués: los mismos del programa (Criar peça, Guilhotina, Grades e portões, Planificações, chapa, sobra…). Portugués de Brasil, sin «ecrã» ni «ficheiro».

**Ayuda del programa** (`ayuda/`): 10 páginas estáticas, sin JavaScript ni píxel, que abren el botón «?» y la tecla F1 de cada ventana de optiMAX. **No se editan a mano**: se generan desde el repo del programa (`nesting-cnc`) con `python NO_DISTRIBUIR/generar_ayuda.py RUTA/weboptimax/ayuda` (textos en `desarrollos/` → `Param.ayuda` y en `ayuda_textos.py`). No cambiar nombres de páginas ni anclas: el programa abre esas direcciones (`ayuda.py`). Las imágenes de las figuras salen de `img/fig/`; las que faltan se dibujan en `ayuda/fig/`.

## Página de optiMAX Taller (`taller/`)

`taller/index.html` = https://optimax.lat/taller/, la página de **optiMAX Taller**, la app del celular (la app vive en
https://app.optimax.lat, repo `optimax-pwa`; esta es solo su página). Solo en español por ahora. Usa `../comun.css` (letras,
colores, barra, botones y pie) + su propio `<style>` (clases `tl-…`; colores de cada oficio iguales a los de la app); **no**
usa `comun.js` (que es del programa de Windows: descarga y pagos). Su propio script al final: precio de la PRO **250 Bs en
Bolivia / 20 USDT afuera** (zona horaria `America/La_Paz`, como el sitio y la app; `.js-precio`, `.js-precio-pc` = 590 Bs /
49 USDT) y eventos del píxel (`TallerAbrirApp` con `modulo`, `TallerConsulta`; con `idioma: "es"` y `pagina: "taller"`).
Mismo píxel y `ox_eid` que el sitio. **La PRO se compra solo desde la app** (26-nov, Max): la página muestra el precio y
dice que se compra en la app («Comprar PRO»), sin enlace de compra ni WhatsApp a ventas (la compra queda atada al
equipo); por eso ya no hay `js-comprar` ni los eventos `Contact` / `TallerComprarPRO`.
Imágenes en `taller/img/`: capturas reales de la app (`3d-*.webp` = vistas 3D, `cel-*.webp` = pantallas del celular,
`og.jpg` = imagen para compartir) y las 12 figuras en `taller/img/fig/`. Las capturas 3D de portones (`3d-porton`,
`3d-corredizo`, `3d-reja`, `3d-panos`, `og.jpg`) se sacan con `python _herramientas/capturas_taller.py --app RUTA/optimax-pwa`
(Playwright sobre la PWA con `?pro=1`; `pro/` = el repo privado); si cambia la app, se vuelven a sacar. Las de chapa y
`cel-*` no están en ese guion (se sacaron a mano el 25-nov). Datos de DEMO / PRO = los de la app (ver
`estado-pwa.md` en el Project de la PWA): si cambian allá, cambiarlos acá. El enlace desde el sitio es `/taller/`
(absoluto, así sirve también en `pt/`).

## Versiones marcadas

Cada versión importante queda guardada en una rama `version-*` que apunta a ese commit. **No borrar estas ramas ni hacerles commits.** Se usan ramas y no tags porque el entorno de Claude no puede subir tags a GitHub.

| Rama | Commit | Qué es |
|---|---|---|
| `version-antes-modo-claro` | `85be41d` | Última versión en modo oscuro (17 nov 2026). Encabezado "Software para talleres metalúrgicos", módulos en tarjetas, 6 funciones explicadas una debajo de la otra. |
| `version-antes-ayuda` | `89cd541` | Antes de agregar la carpeta `ayuda/` y el enlace «Ayuda» en el menú y el pie (18 nov 2026). |
| `version-modo-claro-v1` | `8ae20a0` | Primera versión publicada en modo claro (17 nov 2026): diagrama de módulos con optiMAX al centro, video de YouTube, favicon "M" blanca sobre rojo. |
| `version-antes-carteles` | `9229890` | Antes de agregar Letras y carteles y Logos, y de cambiar el diagrama de módulos por tarjetas con detalle emergente (19 nov 2026). |
| `version-antes-portugues` | `90820b3` | Antes de la versión en portugués (`/pt/`) y de separar `comun.css` / `comun.js` (22 nov 2026). Todo en un solo `index.html`. |
| `version-antes-taller` | `5a7e8e1` | Antes de la página `taller/` (optiMAX Taller, la app del celular) y del enlace «App Taller» en el menú y el pie (25 nov 2026). |

## Cómo volver a una versión anterior

No usar `git push --force`. Revertir con un commit nuevo, que conserva el historial:

```
git checkout main
git pull
git fetch origin version-antes-modo-claro
git revert --no-commit FETCH_HEAD..HEAD
git commit -m "Volver a la versión antes-modo-claro"
git push origin main
```

GitHub Pages publica el cambio en 1 o 2 minutos. Para volver a otra versión, cambiar el nombre de la rama. Para deshacer la vuelta atrás, revertir ese último commit.

Si la versión a la que se vuelve no incluye este `CLAUDE.md`, el revert también lo borra: después de volver, recuperarlo con `git checkout HEAD~1 -- CLAUDE.md`, actualizar la tabla y commitear.

Antes de cada cambio grande en producción, crear una rama marcador sobre `main` (`git push origin main:refs/heads/version-NOMBRE`) y agregarla a la tabla de arriba.

## Cosas a no romper

- Pixel de Meta (`fbq`), con los eventos personalizados `VerVideo`, `VerModulo` (al abrir o pasar de módulo en el detalle de Funciones) y `DescargaDesdeModulo` (botón de descarga dentro del detalle).
- Funciones: tarjetas `.mod` (data-mod = id del artículo) que abren el diálogo `#mod-detalle`; el contenido de cada módulo son los `<article class="hub-panel">` guardados en `.mod-fuente`. Los enlaces `#f-…` del menú abren el detalle de ese módulo.
- Lógica de descarga (`.js-descarga`) y de pago (pestañas, QR, mensaje de WhatsApp), en `comun.js`.
- Precio en Bs para visitantes de Bolivia (detección por zona horaria; `.js-precio-pro`).
- Para probar en local hace falta un servidor (`python -m http.server 8000`): abierto como archivo, el video de YouTube da error 153.

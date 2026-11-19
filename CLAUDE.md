# weboptimax: notas para Claude

Sitio estático de optiMAX (software de nesting y corte para talleres metalúrgicos), publicado con GitHub Pages desde la rama `main` en https://optimax.lat (archivo `CNAME`). Todo está en `index.html` (HTML, CSS y JS en un solo archivo), con imágenes en `img/` y videos en `video/`.

**Ayuda del programa** (`ayuda/`): 10 páginas estáticas, sin JavaScript ni píxel, que abren el botón «?» y la tecla F1 de cada ventana de optiMAX. **No se editan a mano**: se generan desde el repo del programa (`nesting-cnc`) con `python NO_DISTRIBUIR/generar_ayuda.py RUTA/weboptimax/ayuda` (textos en `desarrollos/` → `Param.ayuda` y en `ayuda_textos.py`). No cambiar nombres de páginas ni anclas: el programa abre esas direcciones (`ayuda.py`). Las imágenes de las figuras salen de `img/fig/`; las que faltan se dibujan en `ayuda/fig/`.

## Versiones marcadas

Cada versión importante queda guardada en una rama `version-*` que apunta a ese commit. **No borrar estas ramas ni hacerles commits.** Se usan ramas y no tags porque el entorno de Claude no puede subir tags a GitHub.

| Rama | Commit | Qué es |
|---|---|---|
| `version-antes-modo-claro` | `85be41d` | Última versión en modo oscuro (17 nov 2026). Encabezado "Software para talleres metalúrgicos", módulos en tarjetas, 6 funciones explicadas una debajo de la otra. |
| `version-antes-ayuda` | `89cd541` | Antes de agregar la carpeta `ayuda/` y el enlace «Ayuda» en el menú y el pie (18 nov 2026). |
| `version-modo-claro-v1` | `8ae20a0` | Primera versión publicada en modo claro (17 nov 2026): diagrama de módulos con optiMAX al centro, video de YouTube, favicon "M" blanca sobre rojo. |

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

- Pixel de Meta (`fbq`), con los eventos personalizados `VerVideo` y `VerModulo`.
- Lógica de descarga (`.js-descarga`) y de pago (pestañas, QR, mensaje de WhatsApp).
- Precio en Bs para visitantes de Bolivia (detección por zona horaria; `.js-precio-pro`).
- Para probar en local hace falta un servidor (`python -m http.server 8000`): abierto como archivo, el video de YouTube da error 153.

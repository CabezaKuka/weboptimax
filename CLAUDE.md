# weboptimax: notas para Claude

Sitio estático de optiMAX (software de nesting y corte para talleres metalúrgicos), publicado con GitHub Pages desde la rama `main` en https://optimax.lat (archivo `CNAME`). Todo está en `index.html` (HTML, CSS y JS en un solo archivo), con imágenes en `img/` y videos en `video/`.

## Versiones marcadas

Cada versión importante queda guardada en una rama `version-*` que apunta a ese commit. **No borrar estas ramas ni hacerles commits.** Se usan ramas y no tags porque el entorno de Claude no puede subir tags a GitHub.

| Rama | Commit | Qué es |
|---|---|---|
| `version-antes-modo-claro` | `85be41d` | Última versión en modo oscuro (17 nov 2026). Encabezado "Software para talleres metalúrgicos", módulos en tarjetas, 6 funciones explicadas una debajo de la otra. |
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

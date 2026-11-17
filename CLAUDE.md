# weboptimax: notas para Claude

Sitio estático de optiMAX (software de nesting y corte para talleres metalúrgicos), publicado con GitHub Pages desde la rama `main` en https://optimax.lat (archivo `CNAME`). Todo está en `index.html` (HTML, CSS y JS en un solo archivo), con imágenes en `img/` y videos en `video/`.

## Versiones marcadas (tags)

| Tag | Qué es |
|---|---|
| `antes-modo-claro` | Última versión en modo oscuro antes del cambio a modo claro (17 nov 2026). Encabezado "Software para talleres metalúrgicos", módulos en tarjetas, 6 funciones explicadas una debajo de la otra. |
| `modo-claro-v1` | Primera versión publicada en modo claro (17 nov 2026): diagrama de módulos con optiMAX al centro, video de YouTube, favicon "M" blanca sobre rojo. |

## Cómo volver a una versión anterior

No usar `git push --force`. Revertir con un commit nuevo, que conserva el historial:

```
git checkout main
git pull
git revert --no-commit antes-modo-claro..HEAD
git commit -m "Volver a la versión antes-modo-claro"
git push origin main
```

GitHub Pages publica el cambio en 1 o 2 minutos. Para volver a otra versión, cambiar `antes-modo-claro` por el tag que corresponda. Para deshacer la vuelta atrás, revertir ese último commit.

Antes de cada cambio grande en producción, crear un tag nuevo sobre `main` (`git tag -a NOMBRE -m "descripción" && git push origin NOMBRE`) y agregarlo a la tabla de arriba.

## Cosas a no romper

- Pixel de Meta (`fbq`), con los eventos personalizados `VerVideo` y `VerModulo`.
- Lógica de descarga (`.js-descarga`) y de pago (pestañas, QR, mensaje de WhatsApp).
- Precio en Bs para visitantes de Bolivia (detección por zona horaria; `.js-precio-pro`).
- Para probar en local hace falta un servidor (`python -m http.server 8000`): abierto como archivo, el video de YouTube da error 153.

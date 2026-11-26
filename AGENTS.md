# Noticias CIMA

Estas instrucciones se aplican a todo el repositorio.

## Publicación y verificación

- Nunca intentes acceder por internet a `noticiascima.com`, `www.noticiascima.com` ni a sus subdominios para verificar un despliegue. La regla se aplica a navegadores, solicitudes HTTP, herramientas automatizadas y servicios externos de comprobación.
- Publica en `main` cuando el usuario lo pida. Antes de subir un cambio, revisa el diff y el estado de `origin/main`, y conserva los commits que ya estén en la rama remota.
- Verifica el contenido con pruebas locales. Después de un envío, confirma el commit en `origin/main`. Informa por separado del estado en GitHub y del estado del despliegue. Si solo comprobaste GitHub, indica que el despliegue sigue sin confirmar. Usa el estado del proveedor de despliegue si está disponible por una vía independiente del dominio público.

## Trabajo en el sitio

- El sitio es estático. `index.html` es la portada y la plantilla que usa el generador. Las páginas publicadas viven en `noticias/` y `articulos/`. Aplica los cambios de elementos compartidos, como el pie de página, tanto a la plantilla como a las páginas publicadas que los contienen.
- El pie de página vigente termina con «© 2026 Noticias CIMA.».
- Conserva las rutas ya asignadas en `notas-urls.json` aunque cambie un titular. Usa `scripts/build-notas.js` con Node.js y Playwright para regenerar las páginas, el mapa de rutas, el sitemap, el RSS y `robots.txt` cuando el cambio lo requiera. El generador reescribe archivos versionados. Si solo quieres probarlo, ejecútalo en una copia temporal.
- Para probar el sitio, sirve la raíz con `python3 -m http.server PUERTO --bind 127.0.0.1` usando un puerto libre y comprueba las páginas afectadas por HTTP local. Si regeneras contenido, comprueba que el sitemap y el RSS sean XML válidos y que las rutas del sitemap correspondan a páginas generadas. Cuando el entorno incluya un adaptador de Chromium, sigue las instrucciones de arranque del entorno para usarlo.
- En Codex Cloud, trabaja en el checkout existente. Crea un worktree solo si el usuario lo pide. Conserva los cambios ajenos y limita el diff a lo solicitado.

## Reglas editoriales

El [Manual de ética de las comunicaciones](manual-etica-cima.pdf) rige las noticias, opiniones, notas de prensa, Premios CIMA, el Ranking, el directorio, el boletín, las redes sociales y la publicidad. Consulta el manual al editar contenido editorial.

- Verifica cada dato con al menos una fuente confiable y acredita la fuente y la autoría. Señala si un dato solo proviene de la parte interesada. Usa los registros oficiales para Premios CIMA y el Ranking. Reproduce las citas fielmente y atribúyelas a quien las dijo. Excluye rumores, filtraciones sin confirmar e información obtenida de forma engañosa.
- Distingue hechos de opiniones y trata con respeto a personas, marcas, agencias y competidores. En artículos de opinión, conserva la postura del autor e incluye su nombre y cargo. Publica notas de prensa por su valor informativo y usa fotos propias o autorizadas con crédito.
- Identifica todo contenido pagado como «Contenido patrocinado» o «Publicidad» y distínguelo visualmente del editorial. Mantén la independencia frente a anunciantes, patrocinantes, clientes y participantes. Los anunciantes y patrocinantes quedan fuera de la revisión y aprobación editorial. Ninguna relación comercial da ventaja ante el jurado ni influye en el Ranking. Excluye publicidad engañosa, contraria a la dignidad o incompatible con la normativa aplicable.
- Declara al final de la nota cuando trate sobre un cliente de LBM Comunicaciones. El equipo editorial se abstiene de cubrir temas con intereses personales o comerciales y se mantiene al margen de la evaluación del jurado. Respeta los derechos de autor y acredita las imágenes y las piezas creativas con la marca, la agencia y la fuente. Revisa de inmediato las solicitudes de retirada de los titulares de derechos.
- Limita el directorio a datos corporativos. Usa los datos del boletín y de «Sube tu CV» solo para su fin declarado. Tramita las solicitudes de eliminación de datos personales y evita compartirlos o venderlos a terceros. Exige autorización del representante para publicar el nombre o la imagen de una persona menor de edad.
- Usa la IA como apoyo y somete toda publicación a revisión humana. Nunca la uses para crear imágenes de personas reales ni para alterar el sentido de una foto o una declaración.
- Revisa las solicitudes de corrección en un máximo de 48 horas hábiles. Corrige en la misma nota y añade al final qué cambió y en qué fecha. Señala los errores graves también en la portada. Respeta el derecho a réplica con un espacio y una visibilidad razonablemente equivalentes a los de la nota original.

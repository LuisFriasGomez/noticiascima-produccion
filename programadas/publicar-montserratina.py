# Publicación programada: La Montserratina (lunes 23-11-2026, 7:30 a. m.)
# Uso, desde la raíz del repositorio en main actualizado:
#   python3 -I <ruta>/publicar-montserratina.py <ruta a programadas/>
# Inserta la nota con el siguiente id libre, copia la imagen (jpg + webp) y la registra en WP.
import re, sys, shutil, os
from PIL import Image
P=sys.argv[1]
s=open("index.html",encoding="utf-8").read()
assert "La Montserratina renueva sus empaques" not in s, "La nota ya está publicada"
nid="n%d"%(max(int(x) for x in re.findall(r'\{id:"n(\d+)"',s))+1)
img="img/news-%s.jpg"%nid
im=Image.open(os.path.join(P,"montserratina.jpg")).convert("RGB")
im.save(img,quality=85,optimize=True,progressive=True); im.save(img[:-4]+".webp",quality=80,method=6)
s=s.replace("var WP={",'var WP={"%s":1,'%img,1)
note='''  {id:"%s",lz:"Nueva imagen",d:"2026-11-23",img:"%s",cap:"Nuevos empaques de La Montserratina · Imagen: La Montserratina",sec:"Marcas",t:"La Montserratina renueva sus empaques y ordena su portafolio en cuatro categorías",
   dek:"Con una arquitectura de marca desarrollada junto a Scalto Consultores, la marca venezolana de charcutería amplía su propuesta más allá de la parrilla.",
   body:["La Montserratina lanzó el 10 de noviembre la nueva imagen de sus empaques y una nueva arquitectura de portafolio, desarrolladas junto a Scalto Consultores. El proyecto busca ordenar la oferta de la marca, hacer más fácil la elección del consumidor y abrir oportunidades de crecimiento en el mercado venezolano de charcutería y embutidos.",
         "La marca ha construido su posicionamiento alrededor de la cultura de la parrilla. Con la amplitud de su portafolio, ahora apunta a conectar también con otros momentos de consumo sin perder esa esencia.",
         "El portafolio quedó organizado en cuatro categorías: Grilleros, con los productos para la parrilla y el grill; Humo, dedicada a los ahumados; Momentos, para ocasiones especiales y degustación; y Finísimo, con los productos de consumo diario.",
         "Cada familia de productos tiene ahora un territorio propio dentro de una identidad compartida. El nuevo diseño de empaques usa una jerarquía visual que hace más clara la identificación de cada categoría en el punto de venta.",
         "«La Montserratina tiene una asociación muy poderosa con la parrilla, y el reto no era cambiar ese posicionamiento, sino aprovechar su fortaleza para ampliar la conversación de la marca. La arquitectura de portafolio nos permite organizar la oferta y mostrarle al consumidor que La Montserratina también puede acompañarlo en muchas otras ocasiones», explicó Andrés Rincón, socio fundador de Scalto Consultores.",
         "La parrilla sigue siendo el punto de partida de la marca, que con esta evolución busca ganar espacio en nuevas ocasiones de consumo."],
   why:"Ordenar un portafolio amplio en categorías con identidad propia ayuda a una marca muy asociada a un solo uso a entrar en nuevas ocasiones de consumo y a ganar claridad en el anaquel, en una categoría cada vez más competida.",src:"Nota de prensa de Scalto Consultores · 23 de noviembre de 2026",url:""},
'''%(nid,img)
a="var N = [\n"; assert a in s
s=s.replace(a,a+note,1)
open("index.html","w",encoding="utf-8").write(s)
print(nid)

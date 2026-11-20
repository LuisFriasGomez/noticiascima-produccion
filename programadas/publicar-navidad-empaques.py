# Publicación programada: La Navidad vuelve a los empaques (martes 24-11-2026, 7:30 a. m.)
# Uso, desde la raíz del repositorio en main actualizado:
#   python3 -I <ruta>/publicar-navidad-empaques.py <ruta a programadas/>
import re, sys, os
from PIL import Image
P=sys.argv[1]
s=open("index.html",encoding="utf-8").read()
assert "Flipsmas Sweater" not in s, "La nota ya está publicada"
nid="n%d"%(max(int(x) for x in re.findall(r'\{id:"n(\d+)"',s))+1)
img="img/news-%s.jpg"%nid
im=Image.open(os.path.join(P,"navidad-empaques.jpg")).convert("RGB")
im.save(img,quality=85,optimize=True,progressive=True); im.save(img[:-4]+".webp",quality=80,method=6)
s=s.replace("var WP={",'var WP={"%s":1,'%img,1)
note='''  {id:"%s",lz:"Navidad",d:"2026-11-24",img:"%s",cap:"Empaques navideños de Club Social · Imagen: Mondelēz Venezuela / Scalto Consultores",sec:"Campañas y lanzamientos",t:"Flips, Maizina Americana y Club Social estrenan empaques navideños diseñados por Scalto Consultores",
   dek:"Las ediciones de temporada vuelven a los anaqueles venezolanos, y cada marca interpreta la Navidad desde su propia personalidad.",
   body:["Los empaques navideños, una costumbre comercial que perdió presencia en los anaqueles venezolanos durante los años de dificultades económicas, empiezan a regresar. Scalto Consultores presentó tres ediciones de temporada para Flips, Maizina Americana y Club Social, con una premisa común: cada marca debe vivir la Navidad desde su propia personalidad.",
         "Para Flips, de Alfonzo Rivas, la consultora se inspiró en los ugly Christmas sweaters. Bajo el concepto «Flipsmas Sweater», el empaque convierte el clásico suéter navideño en una pieza llena de humor, con patrones tejidos y mensajes como «Diseñado para ser ugly, tejido para ser cool».",
         "La edición especial de Maizina Americana, también de Alfonzo Rivas, conserva los elementos visuales más reconocibles de la marca y les suma detalles festivos que evocan la preparación de recetas, los encuentros familiares y las costumbres de la temporada.",
         "Para Club Social, de Mondelēz, Scalto desarrolló una serie de tres empaques dedicada a la música y los momentos compartidos, con instrumentos musicales, fuegos artificiales y elementos festivos integrados a la identidad visual de la marca.",
         "«Lo interesante de los empaques de temporada es que no se trata simplemente de vestir un producto de Navidad. Se trata de encontrar cómo cada marca puede participar de una celebración cultural desde su propia personalidad. Flips lo hace desde el humor, Maizina Americana desde la tradición y Club Social desde la música y la celebración», comentó Andrés Rincón, socio fundador de Scalto Consultores."],
   why:"El regreso de las ediciones de temporada muestra que las marcas vuelven a invertir en diseño y diferenciación. El empaque funciona como medio propio: renueva la presencia en el anaquel, genera interés en el punto de venta y refuerza el vínculo emocional con el consumidor.",src:"Nota de prensa de Scalto Consultores · 24 de noviembre de 2026",url:""},
'''%(nid,img)
a="var N = [\n"; assert a in s
s=s.replace(a,a+note,1)
open("index.html","w",encoding="utf-8").write(s)
print(nid)

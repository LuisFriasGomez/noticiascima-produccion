# Inserta la nota programada de Ford en index.html (al inicio de N), copia su imagen y la registra en WP.
# Uso, desde la raíz del repositorio en main:  python3 -I publicar-ford.py <carpeta programadas>
import json, os, re, shutil, sys
from PIL import Image

src_dir = sys.argv[1]
nota = json.load(open(os.path.join(src_dir, 'nota-ford.json'), encoding='utf-8'))
s = open('index.html', encoding='utf-8').read()

if nota['t'] in s:
    sys.exit('La nota ya está publicada: no se hizo ningún cambio.')

ids = [int(x) for x in re.findall(r'\{id:"n(\d+)"', s)]
nid = 'n%d' % (max(ids) + 1)
img = 'img/news-%s.jpg' % nid
if os.path.exists(img):
    sys.exit('Ya existe %s: revisar antes de publicar.' % img)

q = lambda v: json.dumps(v, ensure_ascii=False)
body = ',\n         '.join(q(p) for p in nota['body'])
entry = ('  {id:%s,lz:%s,d:%s,img:%s,cap:%s,sec:%s,t:%s,\n   dek:%s,\n   body:[%s],\n   why:%s,src:%s,url:%s},\n'
         % (q(nid), q(nota['lz']), q(nota['d']), q(img), q(nota['cap']), q(nota['sec']), q(nota['t']),
            q(nota['dek']), body, q(nota['why']), q(nota['src']), q(nota['url'])))

m = re.search(r'var N = \[\n', s)
if not m:
    sys.exit('No encontré la lista de noticias (var N) en index.html.')
s = s[:m.end()] + entry + s[m.end():]

if '/*WEBP*/var WP={' not in s:
    sys.exit('No encontré el registro WP en index.html.')
s = s.replace('/*WEBP*/var WP={', '/*WEBP*/var WP={%s:1,' % q(img), 1)

shutil.copyfile(os.path.join(src_dir, 'ford.jpg'), img)
Image.open(img).save(img[:-4] + '.webp', quality=80, method=6)
open('index.html', 'w', encoding='utf-8').write(s)
print('Nota insertada como', nid, '·', img)

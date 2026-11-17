// Noticias CIMA · genera una página propia por nota y artículo, el sitemap y robots.txt.
// Uso: node scripts/build-notas.js   (desde la raíz del repositorio; requiere Playwright)
// Las direcciones ya asignadas se guardan en notas-urls.json y no cambian aunque se edite el titular.
const fs=require('fs'),path=require('path');const {chromium}=require('playwright');
const ROOT=path.resolve(__dirname,'..'), SITE='https://www.noticiascima.com';
const MAPF=path.join(ROOT,'notas-urls.json');
const STOP=/(-(con|la|el|de|del|y|en|a|para|por|su|sus|los|las|un|una|que|al))+$/;
const slugify=t=>t.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase().replace(/ē/g,'e').replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'').split('-').slice(0,8).join('-').replace(STOP,'');
const esc=s=>String(s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
(async()=>{
 let src=fs.readFileSync(path.join(ROOT,'index.html'),'utf8');
 const map=fs.existsSync(MAPF)?JSON.parse(fs.readFileSync(MAPF,'utf8')):{};
 const used=new Set(Object.values(map));
 const b=await chromium.launch();const p=await b.newPage();
 await p.goto('file://'+path.join(ROOT,'index.html'));await p.waitForTimeout(600);
 const items=await p.evaluate(()=>N.map(n=>({id:n.id,kind:n.kind,d:n.d,t:n.t,dek:n.dek,img:n.img,sec:n.sec,by:n.by})));
 for(const n of items){
  if(!map[n.id]){ let base=(n.kind==='art'?'articulos/':'noticias/')+slugify(n.t), s=base, i=2; while(used.has(s)) s=base+'-'+(i++); map[n.id]=s; used.add(s); }
 }
 const ids=new Set(items.map(n=>n.id)), nurl={}; for(const id of Object.keys(map)) if(ids.has(id)) nurl[id]=map[id];
 src=src.replace(/\/\*NURL\*\/[\s\S]*?\/\*\/NURL\*\//,'/*NURL*/var NURL='+JSON.stringify(nurl)+';/*/NURL*/');
 fs.writeFileSync(path.join(ROOT,'index.html'),src);
 await p.reload(); await p.waitForTimeout(600);
 for(const n of items){
  const dir=map[n.id]; const url=SITE+'/'+dir+'/';
  await p.evaluate(id=>{location.hash='#'+id;},n.id); await p.waitForTimeout(120);
  const app=await p.evaluate(()=>document.getElementById('app').innerHTML);
  const img=n.img?SITE+'/'+n.img.replace(/\?.*$/,''):SITE+'/img/og-noticias-cima.png';
  const ld={"@context":"https://schema.org","@type":n.kind==='art'?"Article":"NewsArticle",headline:n.t,description:n.dek,image:[img],datePublished:n.d,dateModified:n.d,mainEntityOfPage:url,articleSection:n.sec,
   author:{"@type":n.by?"Person":"Organization",name:n.by?n.by.replace(/^(Por|Entrevista a) /,'').split(' · ')[0]:"Redacción CIMA"},
   publisher:{"@type":"Organization",name:"Noticias CIMA",logo:{"@type":"ImageObject",url:SITE+'/img/og-noticias-cima.png'}}};
  let h=src
   .replace(/<title>[^<]*<\/title>/,'<title>'+esc(n.t)+' · Noticias CIMA</title>')
   .replace(/<meta name="description"[^>]*>/,'<meta name="description" content="'+esc(n.dek)+'">')
   .replace(/<meta property="og:type"[^>]*>/,'<meta property="og:type" content="article">')
   .replace(/<meta property="og:title"[^>]*>/,'<meta property="og:title" content="'+esc(n.t)+'">')
   .replace(/<meta property="og:description"[^>]*>/,'<meta property="og:description" content="'+esc(n.dek)+'">')
   .replace(/<meta property="og:url"[^>]*>/,'<meta property="og:url" content="'+url+'">')
   .replace(/<meta property="og:image" [^>]*>/,'<meta property="og:image" content="'+img+'">')
   .replace(/<meta property="og:image:width"[^>]*>\s*<meta property="og:image:height"[^>]*>/,'')
   .replace(/<meta name="twitter:image"[^>]*>/,'<meta name="twitter:image" content="'+img+'">')
   .replace(/<head><base href="\/">/,'<head><base href="/"><link rel="canonical" href="'+url+'"><meta property="article:published_time" content="'+n.d+'"><script type="application/ld+json">'+JSON.stringify(ld).replace(/</g,'\\u003c')+'</script><script>window.__NOTA="'+n.id+'";</script>')
   .replace(/<main id="app">/,'<main id="app">'+app);
  fs.mkdirSync(path.join(ROOT,dir),{recursive:true}); fs.writeFileSync(path.join(ROOT,dir,'index.html'),h);
 }
 await b.close();
 fs.writeFileSync(MAPF,JSON.stringify(map,null,1)+'\n');
 const byId=Object.fromEntries(items.map(n=>[n.id,n]));
 const urls=[`<url><loc>${SITE}/</loc><changefreq>daily</changefreq><priority>1.0</priority></url>`]
  .concat(Object.entries(map).filter(([id])=>byId[id]).sort((a,b)=>byId[b[0]].d.localeCompare(byId[a[0]].d)).map(([id,dir])=>`<url><loc>${SITE}/${dir}/</loc><lastmod>${byId[id].d}</lastmod></url>`));
 fs.writeFileSync(path.join(ROOT,'sitemap.xml'),'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+urls.join('\n')+'\n</urlset>\n');
 fs.writeFileSync(path.join(ROOT,'robots.txt'),'User-agent: *\nAllow: /\n\nSitemap: '+SITE+'/sitemap.xml\n');
 console.log(items.length+' páginas · sitemap con '+urls.length+' direcciones');
})();

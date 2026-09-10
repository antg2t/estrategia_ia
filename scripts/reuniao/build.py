"""Build a single, offline-capable HTML. Run: python scripts/reuniao/build.py"""
from pathlib import Path
from html import escape
from urllib.parse import quote
import json
import re
import sys
from bs4 import BeautifulSoup
from content import SLIDES, ROUTES, COMPARE, LAYERS

ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
OUT=ROOT/'outputs/segunda-feira'
STRATEGY=OUT/'ESTRATEGIA_IA_VP_PESSOAS_V2_FORA_PARA_DENTRO.md'

def inline(text):
    tokens=[]
    def stash(markup):
        tokens.append(markup)
        return f'ZZLINKTOKEN{len(tokens)-1}ZZ'
    text=re.sub(r'\[([^\]]+)\]\(([^\s)]+)\)',lambda m:stash('<a target="_blank" rel="noopener noreferrer" href="'+escape(m[2],quote=True)+'">'+escape(m[1])+'</a>'),text)
    text=escape(text)
    text=re.sub(r'`([^`]+)`',r'<code>\1</code>',text)
    text=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',text)
    text=re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)',r'<em>\1</em>',text)
    for i,t in enumerate(tokens):text=text.replace(f'ZZLINKTOKEN{i}ZZ',t)
    return text

def markdown(text):
    """Small renderer for this repository's headings, tables, lists and prose."""
    lines=text.splitlines(); out=[]; i=0
    while i<len(lines):
        line=lines[i].strip()
        if not line:i+=1;continue
        if line.startswith('```'):
            i+=1;code=[]
            while i<len(lines) and not lines[i].strip().startswith('```'):code.append(lines[i]);i+=1
            out.append('<pre><code>'+escape('\n'.join(code))+'</code></pre>');i+=1;continue
        m=re.match(r'^(#{1,6})\s+(.+)$',line)
        if m:
            level=min(4,max(2,len(m[1]))); num=re.match(r'(\d+(?:\.\d+)*)',m[2]); attr=f' data-section="{num[1]}"' if num else ''
            out.append(f'<h{level}{attr}>'+inline(m[2])+f'</h{level}>');i+=1;continue
        if line.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                cells=[s.strip() for s in lines[i].strip().strip('|').split('|')]
                if not all(re.match(r'^:?-+:?$',c) for c in cells):rows.append(cells)
                i+=1
            out.append('<div class="table-wrap"><table><thead><tr>'+''.join('<th scope="col">'+inline(c)+'</th>' for c in rows[0])+'</tr></thead><tbody>')
            for row in rows[1:]:out.append('<tr>'+''.join('<td>'+inline(c)+'</td>' for c in row)+'</tr>')
            out.append('</tbody></table></div>');continue
        if line.startswith('>'):
            q=[]
            while i<len(lines) and lines[i].strip().startswith('>'):q.append(lines[i].strip().lstrip('> '));i+=1
            out.append('<blockquote><p>'+inline(' '.join(q))+'</p></blockquote>');continue
        if re.match(r'^[-*] ',line) or re.match(r'^\d+\. ',line):
            items=[];ordered=bool(re.match(r'^\d+\. ',line));tag='ol' if ordered else 'ul'
            while i<len(lines) and re.match(r'^(?:[-*]|\d+\.) ',lines[i].strip()):
                items.append(re.sub(r'^(?:[-*]|\d+\.) ','',lines[i].strip()));i+=1
            out.append('<'+tag+'>'+''.join('<li>'+inline(s)+'</li>' for s in items)+'</'+tag+'>');continue
        if re.match(r'^-{3,}$',line):out.append('<hr>');i+=1;continue
        para=[line];i+=1
        while i<len(lines) and lines[i].strip() and not re.match(r'^(?:#|\||>|[-*] |\d+\. |```)',lines[i].strip()):para.append(lines[i].strip());i+=1
        out.append('<p>'+inline(' '.join(para))+'</p>')
    return '\n'.join(out)

def read_jsonl(path):return [json.loads(x) for x in path.read_text(encoding='utf-8').splitlines() if x.strip()]
def safe_json(value):return json.dumps(value,ensure_ascii=False,separators=(',',':')).replace('</',r'<\/').replace('\u2028','\\u2028').replace('\u2029','\\u2029')

def build():
    ds=BeautifulSoup((OUT/'design-system.html').read_text(encoding='utf-8'),'html.parser')
    templates={s['data-template']:s for s in ds.select('section[data-copy-ready=true]')}
    backgrounds={k:s.select_one('.vpp-ppt-bg')['src'] for k,s in templates.items()}
    style=ds.style.string
    template_css=style[style.index('/* INLINE_TEMPLATE_LIBRARY_STYLES_BEGIN'):style.index('/* INLINE_TEMPLATE_LIBRARY_STYLES_END')]
    sources={s['source_id']:dict(s,id=s['source_id']) for s in read_jsonl(ROOT/'evidence/public/PUBLIC_MANIFEST.jsonl') if int(s['source_id'].split('-')[-1])>=14}
    personal=read_jsonl(ROOT/'evidence/personal/PERSONAL_MANIFEST.jsonl');kb=read_jsonl(ROOT/'evidence/personal/PERSONAL_KNOWLEDGE_BASE.jsonl')
    titles={'SRC-PER-001':'iFood · conversa de benchmark com uma executiva','SRC-PER-002':'Nubank · resumo do HR Think Tank, agosto de 2026','SRC-PER-005':'Vivo · síntese de status dos projetos e produtos','SRC-PER-007':'VPP · esclarecimentos de escopo e situação atual','SRC-PER-008':'Pesquisa comparativa de plataformas de IA'}
    for source in personal:
        sid=source['source_id']
        if sid not in titles:continue
        chunks=[]
        for k in kb:
            match=next((p for p in k.get('sources',[]) if p.get('source_id')==sid),None)
            if match and not re.search(r'assess?ement|assessment|SRC-037', json.dumps(k, ensure_ascii=False), re.I):
                chunks.append('<p><strong>'+escape(k['statement'])+'</strong></p><p>'+escape(k.get('context',''))+'</p><p class="evidence-note">'+escape(k['id']+' · '+match.get('locator',''))+'</p>')
        sources[sid]=dict(id=sid,title=titles[sid],href='../../'+quote(source['file'],safe='/'),published=source.get('event_date'),description='Síntese disponível no acervo do projeto; os trechos abaixo preservam os localizadores da catalogação.',limitations=source.get('limitations',''),excerpt=''.join(chunks))
    sources['BB']=dict(id='BB',title='Banco do Brasil · AcademIA BB 2026',url='https://imprensa.bb.com.br/bb-engaja-mais-de-36-mil-funcionarios-em-programa-de-capacitacao-para-ia-generativa-e-agentica/',published='2026',description='Formação prática ligada à rotina e mais de 36 mil inscritos informados pelo banco.',limitations='Inscrições medem alcance e interesse; não comprovam conclusão, competência adquirida ou produtividade.')
    external=read_jsonl(ROOT/'evidence/external/CORPUS_MANIFEST.jsonl')
    used_external={sid for slide in SLIDES for sid in slide['sources'] if re.fullmatch(r'SRC-\d{3}',sid)}
    for source in external:
        sid=source['source_id']
        if sid in used_external:
            sources[sid]=dict(id=sid,title='Gartner · '+source['title'],href='../../evidence/external/INTEGRATED_SYNTHESIS.md',published=source.get('published'),description=source.get('abstract',''),limitations='Referencial do acervo catalogado. Aplicação à Vivo é análise e proposta, sem endosso Gartner.',excerpt='<p>'+escape(source.get('abstract',''))+'</p><p>Localizadores específicos nas notas do quadro e na síntese integrada do acervo.</p>')
    raw=STRATEGY.read_text(encoding='utf-8').replace('em uma oficina de quatro dias', 'em uma oficina')
    chapters={}
    for m in re.finditer(r'^## (\d+)\. .+?(?=^## |\Z)',raw,re.M|re.S):chapters[int(m[1])]=markdown(m[0])
    # Make trailing source limitations accessible in the concluding chapter.
    limits=re.search(r'^## Fontes e limites de interpretação[\s\S]+',raw,re.M)
    if limits:chapters[12]+='\n'+markdown(limits[0])
    icons={
      'map':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/></svg>',
      'source':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M4 4h7v16H4zM14 4h6v16h-6zM6 8h3m7 0h2"/></svg>',
      'full':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M8 3H3v5m13-5h5v5M3 16v5h5m13-5v5h-5"/></svg>'}
    short={'BB':'BB · AcademIA','SRC-PER-001':'iFood · benchmark','SRC-PER-002':'Nubank · evento','SRC-PER-005':'Vivo · contexto interno','SRC-PER-007':'VPP · esclarecimentos','SRC-PUB-014':'Vivo · Relato 2025, pp. 37, 73–76','SRC-PUB-015':'Toqan · produto','SRC-PUB-016':'MELI · newsletter jun/2026','SRC-PUB-017':'Verdi · caso publicado','SRC-PUB-018':'Verdi · relato executivo','SRC-PUB-019':'MELI · Q1/2026','SRC-PUB-020':'MELI · 10-K 2025','SRC-PUB-021':'Nubank · AskNu, mai/2025','SRC-PUB-022':'Nubank · skills, set/2026','SRC-PUB-028':'Prosus · agentes','SRC-PUB-029':'Nubank · estratégia'}
    sections=[]
    for n,s in enumerate(SLIDES,1):
        kind=s['kind'];template={'cover':'vp-cover-01','agenda':'vp-agenda-01','transition':'vp-subcover-01','vision':'vp-content-center-white-01','close':'vp-close-purple-01'}.get(kind,'vp-content-white-01')
        ref=[]
        for sid in s['sources']:
            source=sources[sid];label=short.get(sid,('Gartner · '+sid if sid in used_external else source['title']))
            ref.append(f'<a href="{escape(source["url"],quote=True)}" target="_blank" rel="noopener noreferrer">{escape(label)} ↗</a>' if source.get('url') else f'<button data-source="{sid}">{escape(label)} ↗</button>')
        source_html='<span>Fontes</span>'+''.join(ref) if ref else '<span>Base: estratégia V2 · capítulo '+str(s['chapter'])+' · '+('Exemplo ilustrativo / análise' if s['group']=='Trabalho' else 'Proposta para discussão')+'</span>'
        sections.append(f'''<section class="vpp-slide vpp-inline-slide kind-{kind}{' active' if n==1 else ''}" id="{s['id']}" data-slide-surface="{'pink' if kind=='vision' else 'purple' if kind in ['transition','close'] else 'white'}" data-template="{template}" data-ppt-slide="{templates[template]['data-ppt-slide']}" data-meeting-slide="{n}" data-role="{kind}" aria-label="{escape(BeautifulSoup(s['title'].replace('<br>',' '),'html.parser').get_text(),quote=True)}" aria-hidden="{'false' if n==1 else 'true'}">
<div class="vpp-stage"><img class="vpp-ppt-bg" data-background="{template}" alt="" aria-hidden="true"><div class="vpp-content-layer"><div class="slide-meta">{s['group']}<span class="evidence-kind">{s['label']}</span></div><h1 class="screen-title" tabindex="-1">{s['title'].replace('<br>','<br> ')}</h1><p class="screen-sub">{s['sub']}</p><div class="visual-body">{s['body']}</div><div class="slide-sources">{source_html}</div></div></div></section>''')
    # Every source cited on a projected slide must have a catalog entry.
    for s in SLIDES:
        assert s['chapter'] in chapters
        assert all(i in sources for i in s['sources'])
        assert all(i in [x['id'] for x in SLIDES] for i in s['detail'])
    sources={sid:source for sid,source in sources.items() if not re.search(r'assess?ement|assessment|SRC-037', json.dumps(source, ensure_ascii=False), re.I)}
    data=dict(slides=[{k:v for k,v in s.items() if k!='body'} for s in SLIDES],routes=ROUTES,sources=sources,chapters=chapters,compare=COMPARE,layers=LAYERS,backgrounds=backgrounds)
    html='''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"><title>Estratégia de IA · VP Pessoas · Vivo</title><link rel="icon" href="data:,"><style>'''+template_css+'\n'+(HERE/'meeting.css').read_text(encoding='utf-8')+'''</style></head><body>
<a class="skip-link" href="#deck">Ir para o quadro da apresentação</a>
<header class="topbar"><div class="brand"><span class="brand-mark" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"><circle cx="12" cy="5" r="2"/><path d="M12 8v7m-6-4h12m-6 4-4 5m4-5 4 5"/></svg></span><span>VP Pessoas<small>Estratégia de IA</small></span></div><nav class="mode-picker" aria-label="Modo de visualização"><button data-mode="executivo" aria-pressed="true">Executivo</button><button data-mode="estendido" aria-pressed="false">Estendido</button></nav><div class="tools"><button class="plain-btn" id="btn-map" title="Mapa da conversa (M)">'''+icons['map']+'''<span class="tool-label">Mapa</span><span class="sr-only">Mapa da conversa</span></button><button class="plain-btn" data-open-sources="all" title="Biblioteca de fontes">'''+icons['source']+'''<span class="tool-label">Fontes</span><span class="sr-only">Biblioteca de fontes</span></button><button class="plain-btn icon-only mobile-hide" data-fullscreen title="Tela cheia (F)" aria-label="Tela cheia">'''+icons['full']+'''</button><button class="plain-btn icon-only" id="btn-help" title="Como navegar (?)" aria-label="Como navegar">?</button></div></header>
<button class="return-strip" id="return-strip" hidden></button>
<main id="deck" class="vpp-deck" aria-label="Apresentação de estratégia de IA">'''+''.join(sections)+'''</main>
<footer class="bottom-bar"><div class="route-progress" aria-hidden="true"><i id="progress-fill"></i></div><div class="bottom-context"><span class="slide-position" id="slide-position"></span><div class="context-text"><strong id="context-title"></strong><span id="context-bridge"></span></div></div><nav class="slide-actions" aria-label="Navegar e aprofundar"><button class="plain-btn" id="btn-read">Aprofundar ↗</button><button class="plain-btn" id="btn-notes">Discussão</button><button class="plain-btn" id="btn-prev" aria-label="Quadro anterior">←</button><button class="primary-btn next-btn" id="btn-next">Próximo →</button></nav></footer>
<dialog id="workspace-dialog" aria-labelledby="dialog-title"><div class="dialog-shell"><div class="dialog-head"><h2 id="dialog-title"></h2><button class="plain-btn dialog-close" aria-label="Fechar painel">×</button></div><div class="dialog-body" id="dialog-body"></div></div></dialog>
<div class="toast" id="toast" role="status" hidden></div><div class="sr-only" id="live-status" aria-live="polite" aria-atomic="true"></div>
<noscript><style>.topbar,.bottom-bar,.vpp-deck{display:none}</style><p style="padding:32px">Ative o JavaScript para usar os percursos interativos. A apresentação funciona localmente, sem servidor ou bibliotecas externas.</p></noscript>
<script id="meeting-data" type="application/json">'''+safe_json(data)+'''</script><script>const DATA=JSON.parse(document.getElementById('meeting-data').textContent);
'''+(HERE/'meeting.js').read_text(encoding='utf-8')+'''</script></body></html>'''
    dest=OUT/'REUNIAO_ESTRATEGIA_IA_VP_PESSOAS.html';dest.write_text(html,encoding='utf-8')
    print(json.dumps(dict(file=str(dest),bytes=dest.stat().st_size,slides=len(SLIDES),routes={k:len(v) for k,v in ROUTES.items()},chapters=len(chapters),sources=len(sources)),ensure_ascii=False))
    return dest

if __name__=='__main__':build()

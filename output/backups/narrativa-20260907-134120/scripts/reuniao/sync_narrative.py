"""Keep speaker narrative synchronized with the actual presentation."""
from pathlib import Path
from bs4 import BeautifulSoup
from content import SLIDES, ROUTES

def plain(text):
    return BeautifulSoup('<div>'+text.replace('<br>', ' ')+'</div>', 'html.parser').get_text(' ', strip=True)

lines = [
    '# Roteiro narrativo — Estratégia de IA da VP Pessoas', '',
    f'Revisão de 07/09/2026, sincronizada com o Markdown e o HTML. Executivo: {len(ROUTES["executivo"])} quadros; Estendido: {len(SLIDES)} quadros.', '',
    '## Mapa narrativo', '',
    'Mudança no trabalho → referenciais Gartner → mercado → Vivo → responsabilidades e visão → cinco big bets como meios → execução e valor → mapa executivo com os três resultados.', '',
    'As cinco big bets contribuem em conjunto para alcançar os três resultados. Não utilizar um exemplo ou uma associação exclusiva entre uma big bet e um resultado para explicar essa conexão.', '',
    '## Quadros', '',
]
for i,s in enumerate(SLIDES,1):
    lines += [f'### {i:02} — {plain(s["title"])}', '',
              f'**Ideia central:** {plain(s["sub"])}', '',
              f'**Conteúdo visual:** {plain(s["body"])}', '',
              f'**Base:** capítulo {s["chapter"]}'+(' · '+', '.join(s['sources']) if s['sources'] else ' · análise/proposta')+'.', '',
              f'**Passagem:** {s["bridge"]}', '']
    if s['note']:
        lines += [f'**Nota de fala:** {s["note"]}', '']
    for mode, bridge in s.get('route_bridges', {}).items():
        lines += [f'**Passagem no {mode}:** {bridge}', '']
(Path(__file__).resolve().parents[2]/'outputs/segunda-feira/ROTEIRO_NARRATIVO_V2_FORA_PARA_DENTRO.md').write_text('\n'.join(lines), encoding='utf-8')

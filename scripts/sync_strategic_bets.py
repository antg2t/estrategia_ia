from pathlib import Path
import re,json
R=Path(__file__).resolve().parents[1]; O=R/'outputs/segunda-feira'
def read(p): return p.read_text(encoding='utf-8-sig')
def write(p,s): p.write_text(s.rstrip()+'\n',encoding='utf-8')
p=O/'ESTRATEGIA_IA_VP_PESSOAS_V2_FORA_PARA_DENTRO.md'
write(p,read(p).replace('fala da CHRO','apresentação da executiva'))
p=O/'ROTEIRO_NARRATIVO_V2_FORA_PARA_DENTRO.md'
old=read(p); write(O/'historico/ROTEIRO_V2_ANTES_GRANDES_APOSTAS.md',old)
blocks=re.findall(r'^### \d{2} —.*?(?=^### \d{2} —|^## Corte editorial|\Z)',old,re.M|re.S)
updates={
11:('iFood: a direção antecede a organização das demandas','evidência','2.5','O planejamento orienta os produtos e os PMs organizam sua evolução.','Explique o direcionamento funcional e estratégico, a alocação seletiva e o papel dos PMs. Necessidades chegam de diferentes origens; a organização do trabalho tem responsável. O caso continua tendo decisões de roadmap.','Direção estratégica → produtos e capacidade → escolhas do PM. Fonte: SRC-PER-001, 24:57–27:40.'),
12:('Toqan: conversa, dados e criação na mesma experiência','evidência','2.6','A camada acessível converte capacidade técnica em autonomia.','Explique a experiência relatada: o usuário pergunta e a solução consulta os dados conectados dentro de seu acesso. Inclua criação em linguagem natural e o trabalho de definições e sustentação. Separe produto público e configuração do benchmark.','Pessoa → conversa → dados e recursos conectados. Fontes: SRC-PER-001, 12:49–18:48; SRC-PUB-015.'),
13:('O que levamos do mercado','síntese','3','A estratégia conecta preparação, redesenho, direção de produto e autonomia.','Reúna aprendizagem e competências; transformação do trabalho; direção e PMs; experiência integrada; conhecimento e continuidade. Relacione cada eixo ao caso correspondente.','Cinco eixos conectados, com suas fontes.'),
16:('A Vivo já constrói bases de transformação','diagnóstico','4.2','Os projetos ganham força quando participam de uma direção comum.','Situe Eu Vivo IA, Data Mesh, Violeta, COMP e Jeito de Produtar. COMP é reconstrução a partir de base zero com IA no centro. Violeta é base técnica; no contexto informado da VPP falta experiência acessível integrada.','Cinco movimentos e seu significado estratégico. Fontes: SRC-PER-005 e 007.'),
17:('A diferença começa antes da fila','comparação','4.3','Metas e planejamento devem orientar o trabalho antes de cada pedido.','Compare direção estratégica e organização por PMs no iFood com pedidos de diferentes áreas e reconstrução de valor no qualifying Vivo. A hipótese de origem nas metas deve aparecer como interpretação; não afirmar ausência de planejamento na Vivo.','Planejamento → produto → escolhas; ao lado, pedido → reconstrução de valor e prioridade.'),
18:('Jeito de Produtar pode mudar a origem da demanda','comparação','4.3','A formação precisa se traduzir em metas, responsabilidades e decisões de capacidade.','Todas as áreas identificam necessidades; PMs organizam sua tradução em produto. A mudança proposta reduz a indefinição anterior à fila. Complete com a diferença entre base técnica e experiência integrada de IA.','Meta → produto → carteira → capacidade. Mostrar a experiência integrada como condição de autonomia.'),
21:('Visão 2028: resultado do conhecimento acumulado','solução','6','Trabalho mais simples, pessoas mais preparadas e entregas melhores.','Derive os compromissos de redesenho/COMP, aprendizagem/Skills e direção de produto/experiência integrada. Apresente o enunciado da visão e a necessidade de capacidades transversais.','Três resultados com os aprendizados e bases Vivo que os originaram.'),
22:('Quais grandes apostas sustentam essa visão?','transição','6–7','A VP precisa de compromissos estruturais que sirvam a diferentes jornadas.','Anuncie as cinco apostas: estratégia e metas; experiência integrada; conhecimento reutilizável; preparação da organização; reinvenção permanente. Produtos e jornadas são desdobramentos posteriores.','Cinco apostas sobre a cor primária do tema.'),
23:('Aposta 1 — Estratégia e metas na origem do trabalho','escolha','7.1','Objetivos claros orientam produtos, escolhas e capacidade.','Ligue iFood à evolução do Jeito de Produtar. Explique a responsabilidade dos PMs por consolidar necessidades em uma direção anterior aos pedidos. Explicite o resultado esperado: menos reconstrução de prioridade.','Objetivo → meta → produto → investimento e evolução.'),
24:('Aposta 2 — Uma experiência integrada de IA','escolha','7.2 e 8','As pessoas usam dados e agentes e criam recursos por uma experiência acessível.','Retome Toqan. Mostre conversa, entendimento da intenção e acionamento de dados/ferramentas. Data Mesh e Violeta podem sustentar a experiência, mas ela inclui capacidades adicionais. Não definir fornecedor nem plataforma como decisão tomada.','Experiência do usuário acima das capacidades compartilhadas de dados, conhecimento e agentes.'),
25:('Aposta 3 — Conhecimento reutilizável de Pessoas','escolha','7.3','Informações e definições confiáveis precisam servir a diferentes produtos e agentes.','Conecte Data Mesh a políticas, critérios e conhecimento com responsáveis. Explique por que a mesma pergunta deve preservar o significado do indicador em diferentes canais.','Dados + definições + conhecimento → múltiplos usos com consistência.'),
26:('Aposta 4 — Preparar a organização para o trabalho que muda','escolha','7.4','Aprendizagem, liderança e práticas de talento evoluem junto com a execução.','Conecte BB, Mercado Livre, Nubank e iFood a Eu Vivo IA e às necessidades da Vivo. Situe seleção, desenvolvimento, mobilidade e desempenho como práticas que precisam acompanhar competências e papéis.','Mudança no trabalho → competências e liderança → práticas de talento.'),
27:('Aposta 5 — Reinvenção permanente dos serviços','escolha','7.5–7.6','Redesenhar com IA desde a origem precisa ser uma capacidade da VP.','Apresente COMP como movimento de reconstrução, aproximando sua abordagem do Nubank. O aprendizado permanece na VPP e fortalece outras transformações. Feche mostrando como as cinco apostas se reforçam.','Experiência desejada → redesenho → aprendizado que permanece e pode ser reutilizado.'),
28:('O modelo operativo sustenta as apostas','solução','9','Metas orientam produtos; PMs organizam necessidades; capacidades compartilhadas ampliam autonomia.','Distingua origem da necessidade e responsabilidade por organizar trabalho de produto. Preserve contribuição funcional e técnica. Explique a hipótese de velocidade pela menor reconstrução de prioridade e contexto.','Estratégia/metas → gestão de produto ↔ especialidades e capacidades compartilhadas.'),
29:('Evoluir com valor demonstrado','solução','10–11','Conectar, incorporar e ampliar deve produzir simplicidade, preparação e melhores entregas.','Apresente movimentos estratégicos e resultados. Metas derivam do ponto de partida e incluem qualidade e custo total. As jornadas materializam a estratégia; sua escolha pertence ao desdobramento das apostas.','Três movimentos associados aos três resultados da visão.'),
30:('A estratégia de IA da VPP','fechamento','12','Preparar a Vivo e reinventar Pessoas com direção, autonomia e capacidade de transformação.','Reúna a visão e as cinco apostas. Retome o percurso: mudança na tarefa, casos, realidade Vivo, contribuição da VP e capacidades estruturais. Encerre com os resultados para 2028.','Visão 2028 sustentada pelas cinco apostas; produtos e jornadas como expressão da estratégia.')}
for i,t in updates.items():
 title,fn,base,point,note,visual=t
 surface='theme-primary-transition' if fn=='transição' else 'white/default'
 blocks[i-1]=f'### {i:02} — {title}\n\n**Function:** {fn}. **Surface:** {surface}.\n\n**Ideia central:** {point}\n\n**Nota de fala:** {note}\n\n**Visual Direction:** {visual}\n\n**Base:** capítulo {base} da estratégia.\n\n**Bridge:** pendente\n\n'
for i,b in enumerate(blocks):
 b=b.replace('da CHRO','da executiva de Pessoas').replace('Clarisse','executiva do iFood')
 next_point=re.search(r'\*\*Ideia central:\*\* (.*)',blocks[i+1]).group(1) if i+1<len(blocks) else 'A visão e as cinco apostas concluem a estratégia, com jornadas e produtos como seus desdobramentos.'
 blocks[i]=re.sub(r'\*\*Bridge:\*\*[^\n]*','**Bridge:** '+next_point,b)
header=old[:old.index('### 01')].replace(' Público inicial: diretora e CHRO.','')
header=re.sub(r'Trabalho e responsabilidade \(01–04\).*?\n\n','Trabalho e responsabilidade (01–04) → mercado (05–12) → síntese (13) → contexto e comparação Vivo (14–18) → contribuição de Pessoas (19) → visão derivada (20–21) → cinco grandes apostas (22–27) → modelo operativo (28) → evolução e valor (29) → estratégia consolidada (30).\n\n',header,flags=re.S)
write(p,header+''.join(blocks)+'''## Corte editorial

Versão completa: 30 quadros. Composição compacta: 24 quadros, fundindo 01–02, 03–04, 08–09, 15–16, 17–18 e 20–21. Preservar o desenvolvimento das cinco apostas e sua conexão com a visão. Nas fusões que envolvem transição, manter a direção visual de transição e retomar white/default no quadro seguinte.
''')

# Catalog the verified public product description separately from the conversation.
pub=R/'evidence/public'
for filename,row in [
 ('PUBLIC_MANIFEST.jsonl',dict(source_id='SRC-PUB-015',title='Toqan — Your AI workspace',url='https://toqan.ai/',published=None,accessed='2026-09-06',kind='official_product_description',locator='Everything in one place; Everyone becomes a builder; Good to know',limitations='Descrição comercial do produto da Prosus. Não comprova a configuração implantada no iFood nem disponibilidade equivalente na Vivo.')),
 ('PUBLIC_KNOWLEDGE_BASE.jsonl',dict(id='KU-PUB-015',type='product_capability',statement='Toqan se apresenta como ambiente de IA da Prosus para conversar, analisar e criar aplicações e fluxos em linguagem natural com conexão a ferramentas e dados.',context='Página oficial; distinguir capacidade declarada do produto de configuração e uso interno relatados no benchmark.',epistemic_status='declaração pública do fornecedor',validation_needed=True,sources=[dict(source_id='SRC-PUB-015',locator='Everyone becomes a builder; Good to know',url='https://toqan.ai/')]))]:
 p=pub/filename; write(p,read(p)+'\n'+json.dumps(row,ensure_ascii=False))

personal=R/'evidence/personal'
p=personal/'README.md';s=read(p).replace('seis fontes e 52 unidades','sete fontes e 55 unidades')
s+='''

## Esclarecimentos estratégicos — 06/09/2026

[SRC-PER-007](../../sources/personal/outras%20fontes%20pessoais/esclarecimentos_estrategicos_vpp_2026-09-06.md) registra os esclarecimentos da usuária sobre COMP, planejamento e PMs, lacuna de experiência integrada na VPP e grandes apostas. KU-PER-053–055 complementam a leitura anterior; não alteram os anexos originais. O registro é uma síntese editorial, com interpretação e limitações explícitas.

A descrição oficial do Toqan está catalogada separadamente como SRC-PUB-015/KU-PUB-015. O produto público não é tratado como prova de todos os detalhes da configuração interna relatada no iFood.
''';write(p,s)
p=personal/'INTEGRATED_SYNTHESIS.md';s=read(p);pos=s.index('\n')+1
update='''
## Atualização vigente — grandes apostas e experiência integrada

Sete fontes pessoais e 55 unidades. Os esclarecimentos de SRC-PER-007, KU-PER-053–055, qualificam a leitura: COMP é redesenho de jornadas desde a origem, com IA no centro; a diferença iFood/Vivo envolve a conexão anterior entre planejamento, metas e organização por PMs; falta, no contexto relatado da VPP, uma camada acessível que conecte conversa, dados e agentes.

A transcrição iFood registra decisões de roadmap e necessidades de origens diversas. Portanto, a análise é sobre onde e com que referência se prioriza, e sobre quem organiza o trabalho, sem concluir que não exista priorização no iFood. A percepção de que o problema nasce parcialmente nas metas é interpretação estratégica; Jeito de Produtar pode corrigir essa origem, mas sua eficácia ainda não está demonstrada.

A narrativa atual substitui o salto da visão para escolha de jornadas por cinco apostas: estratégia e metas; experiência integrada; conhecimento reutilizável; preparação da organização; reinvenção permanente dos serviços. Jornadas e produtos desdobram essas escolhas. Fonte pública de identidade e proposta do Toqan: SRC-PUB-015. A descrição de uso interno continua atribuída ao benchmark.

Os trechos seguintes preservam revisões anteriores; em conflito, prevalece esta atualização.

''';write(p,s[:pos]+update+s[pos:])
for name in ['CLAUDE.md','START_HERE.md','docs/PROJECT_STATUS.md']:
 p=R/name;s=read(p);pos=s.index('\n')+1
 update='''
## Direção vigente — grandes apostas, revisão adicional de 06/09/2026

- Estratégia V2 e roteiro narrativo atualizados. Após a visão, desenvolver cinco apostas estruturais: metas e produtos; experiência integrada de IA; conhecimento reutilizável; preparação da organização; reinvenção dos serviços. Removido o salto para selecionar duas jornadas.
- COMP é reconstrução desde a origem com IA no centro; RI e offboarding exemplificam o movimento. iFood é atribuído a uma executiva, sem nome. O documento estratégico e o roteiro não identificam sua audiência.
- Bloco 4.3 compara constatações: direção e metas anteriores à fila, organização por PMs, demandas de diferentes áreas na Vivo e evolução possível pelo Jeito de Produtar. Não afirmar que iFood não prioriza.
- Toqan torna explícita a experiência conversacional ligada a dados e criação. Violeta é base por código no contexto relatado da VPP; camada acessível integrada é capacidade a construir, sem afirmar limitação permanente ou ausência em toda a corporação.
- Capítulo 6: visão; 7: cinco apostas; 8: experiência integrada; 9: modelo por metas e produtos; 10: trajetória estratégica; 11: valor; 12: consolidação.
- Fontes pessoais: sete/55 unidades, com esclarecimentos em SRC-PER-007. Fontes públicas: 15/15 unidades, com página oficial Toqan em SRC-PUB-015. Roteiro: 30 quadros sincronizados. Original dos anexos preservado.
- Estas decisões substituem descrições de versões anteriores abaixo. Scripts de revisões antigas registram transformações históricas e não devem ser reexecutados sobre a versão vigente.

''';write(p,s[:pos]+update+s[pos:])
p=O/'README.md';s=read(p).replace('seis fontes e 52 unidades','sete fontes e 55 unidades')
s=s.replace('visão derivada para 2028, escolhas, modelo operativo e execução','visão derivada para 2028, cinco grandes apostas, experiência integrada, modelo operativo e valor')
s=s.replace('o modelo operativo proposto, no capítulo 9.', 'as cinco apostas, no capítulo 7; a experiência integrada de IA, no capítulo 8; e o modelo operativo, no capítulo 9.')
write(p,s)

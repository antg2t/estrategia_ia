from pathlib import Path
import re,json
R=Path(__file__).resolve().parents[1];O=R/'outputs/segunda-feira'
def read(p):return p.read_text(encoding='utf-8-sig')
def write(p,s):p.write_text(s.rstrip()+'\n',encoding='utf-8')
p=O/'ROTEIRO_NARRATIVO_V2_FORA_PARA_DENTRO.md';hist=O/'historico/ROTEIRO_V2_ANTES_TRIANGULACAO_PLATAFORMAS.md'
if not hist.exists():write(hist,read(p))
s=read(hist);blocks=re.findall(r'^### \d{2} —.*?(?=^### \d{2} —|^## Corte editorial|\Z)',s,re.M|re.S)
def block(title,fn,base,point,note,visual):
 return f'### 00 — {title}\n\n**Function:** {fn}. **Surface:** white/default.\n\n**Ideia central:** {point}\n\n**Nota de fala:** {note}\n\n**Visual Direction:** {visual}\n\n**Base:** capítulo {base} da estratégia.\n\n**Bridge:** a definir\n\n'
blocks[6]=block('Mercado Livre: experiência e plataforma são capacidades diferentes','evidência','2.2','Uma base compartilhada permite que pessoas e produtos ampliem sua atuação.','Apresente Cowork distribuído a 31 mil funcionários, Verdi para construção, serviços horizontais e Fury como base. Maxwell exemplifica atendimento. Não desenhar ligação Cowork–Verdi como fato. Preserve a consequência para competências e Pessoas.','Camadas lado a lado, com limite de integração explícito. Fontes: SRC-PUB-016–020.')
blocks[12]=block('O que levamos do mercado','síntese','3','Preparação, redesenho, experiência e reuso precisam evoluir juntos.','Retome aprendizagem no BB; plataforma e experiência no Mercado Livre; estratégia e governança no Nubank; organização por PMs e autonomia no iFood. A síntese define critérios, sem escolher um produto a copiar.','Aprendizados com sua origem e contribuição para a estratégia.')
blocks[20]=blocks[20].replace('direção de produto/experiência integrada','direção de produto e a triangulação entre experiência, plataforma e reuso')
blocks[23]=block('Aposta 2 — Experiência acessível, capacidades compartilhadas','escolha','7.2 e 8','Plataforma e experiência têm responsabilidades próprias e precisam se integrar.','Use quatro camadas: fundação; conhecimento e ações reutilizáveis; construção/orquestração; experiência. Toqan, Mercado Livre e Nubank fundamentam mecanismos complementares. Data Mesh e Violeta atendem partes a verificar, sem pressupor um único produto para toda a arquitetura.','Quatro camadas da proposta VPP, identificadas como desenho recomendado.')
blocks[24]=blocks[24].replace('Conecte Data Mesh a políticas, critérios e conhecimento com responsáveis.', 'Conecte Data Mesh a políticas, critérios e conhecimento com responsáveis. Inclua capacidades de ação reutilizáveis, com avaliação e manutenção; o marketplace Nubank é referência de engenharia, não serviço de RH já implantado.')
newnu=block('Nubank: busca e componentes reutilizáveis, em estágios distintos','evidência','2.7','Uma arquitetura modular pode atender diferentes experiências sem uma porta universal comprovada.','AskNu documenta busca; ações estavam no roadmap de maio de 2025. Marketplace documenta avaliação antes de distribuição a desenvolvedores. Vagas apontam construção de contexto e orquestração, sem comprovar implantação completa.','Operação documentada, roadmap e direção de construção em três grupos. Fontes: SRC-PUB-021–026.')
comparison=block('Três referências, uma distinção estratégica','comparação','3.1','Experiência do usuário e plataforma de agentes são problemas complementares.','Toqan torna a experiência visível; Mercado Livre documenta recursos horizontais; Nubank acrescenta reuso e governança. Compare entrada, conhecimento, ações, construção, reuso e controles sem ranking de sofisticação.','Três empresas e suas contribuições; matriz detalhada como apoio no capítulo 3.1.')
out=[]
for i,b in enumerate(blocks,1):
 out.append(b)
 if i==10:out.append(newnu)
 if i==13:out.append(comparison)
for i,b in enumerate(out):
 b=re.sub(r'^### \d{2}',f'### {i+1:02}',b)
 nextpoint=re.search(r'\*\*Ideia central:\*\* (.*)',out[i+1]).group(1) if i+1<len(out) else 'A visão e as cinco apostas concluem a estratégia; produtos e jornadas são seus desdobramentos.'
 out[i]=re.sub(r'\*\*Bridge:\*\*[^\n]*','**Bridge:** '+nextpoint,b)
head=s[:s.index('### 01')]
head=re.sub(r'Trabalho e responsabilidade \(01–04\).*?\n\n','Trabalho e responsabilidade (01–04) → mercado e capacidades (05–13) → síntese e comparação (14–15) → Vivo e modelo operativo (16–20) → contribuição e visão (21–23) → cinco apostas (24–29) → modelo, evolução e valor (30–31) → estratégia consolidada (32).\n\n',head,flags=re.S)
write(p,head+''.join(out)+'''## Corte editorial

Versão completa: 32 quadros. Composição compacta: 26 quadros, fundindo 01–02, 03–04, 08–09, 17–18, 19–20 e 22–23. Preservar a distinção experiência/plataforma, os estágios do Nubank e as cinco apostas. Nas fusões com transição, manter a cor primária do tema e retornar a white/default no quadro seguinte.
''')
update='''## Atualização vigente — experiência, plataforma e capacidades reutilizáveis

A pesquisa fornecida foi registrada como SRC-PER-008, KU-PER-056–060. Camada pessoal: oito fontes/60 unidades. Acrescentadas 12 fontes públicas, SRC-PUB-016–027 e KU-PUB-016–027; camada pública: 27 fontes/27 unidades. A compilação fornecida e as fontes consultadas permanecem separadas.

Mercado Livre foi ampliado para Cowork, Verdi, serviços horizontais, Fury e Maxwell, preservando sua contribuição a Pessoas. A newsletter de junho de 2026 foi reaberta com sucesso; a limitação de acesso da rodada anterior está superada para essa fonte. O comunicado Q1 diz 31 mil funcionários; distribuição não é uso ativo e não comprova conexão Cowork–Verdi. O trecho oficial indexado do 10-K informa adoção de ferramentas de IA, sem restringir a GenAI; a abertura integral excedeu o limite do leitor.

Nubank: AskNu documenta busca no Slack (maio de 2025), com ações ainda como próximos passos naquela publicação; marketplace documenta avaliação de skills para desenvolvedores (setembro de 2026). Vagas descrevem Productivity Systems, GenAI Platform, DXP e AIDE como escopos de trabalho/construção. Não tratar vagas como comprovação de implantação universal nem comparar automaticamente o Vector da vaga com o termo usado no resumo do evento.

A estratégia compara seis capacidades no capítulo 3.1 e separa quatro camadas no 8.2: fundação de IA, capacidades reutilizáveis, construção/orquestração e experiência. Violeta e Data Mesh devem ser avaliados por cobertura, sem objetivo presumido de reproduzir Toqan. Aposta 2 reforçada por triangulação; aposta 3 ampliada para componentes e ações reutilizáveis. Preservadas cinco grandes apostas antes das jornadas, modelo por metas/PMs e COMP como redesenho com IA desde a origem.

Números Toqan de 25 mil usuários/22 empresas, 5 mil agentes e 747 mil ações ficaram como alegações fornecidas não confirmadas. Não foram usados como fundamento executivo. Não há ranking de sofisticação nem porta universal Nubank comprovada.

Estratégia e roteiro sincronizados: 12 capítulos e 32 quadros. Fontes originais anteriores preservadas. Esta atualização prevalece sobre contagens e descrições históricas abaixo.

'''
for name in ['CLAUDE.md','START_HERE.md','docs/PROJECT_STATUS.md','evidence/personal/INTEGRATED_SYNTHESIS.md','evidence/public/INTEGRATED_SYNTHESIS.md']:
 p=R/name;s=read(p);pos=s.index('\n')+1;write(p,s[:pos]+'\n'+update+s[pos:])
for name in ['evidence/personal/README.md','outputs/segunda-feira/README.md']:
 p=R/name;s=read(p).replace('sete fontes e 55 unidades','oito fontes e 60 unidades').replace('30 quadros','32 quadros')
 if 'personal' in name:s+='''

## Pesquisa comparativa adicional

[SRC-PER-008 — plataformas e experiências de IA](../../sources/personal/outras%20fontes%20pessoais/pesquisa_plataformas_agenticas_2026-09-06.md): registro editorial da pesquisa fornecida, alegações, correções e links; KU-PER-056–060. Fontes públicas verificadas em SRC-PUB-016–027. A compilação não é prova independente.
'''
 write(p,s)
p=R/'evidence/public/README.md';s=read(p);pos=s.index('\n')+1;write(p,s[:pos]+'\n'+update+s[pos:])
write(R/'docs/REVISAO_PLATAFORMAS_2026-09-06.md','''# Revisão — plataformas e experiência integrada, 06/09/2026

'''+update+'''## Mudanças no material

- Caso Mercado Livre ampliado no 2.2: plataforma e experiência, mantendo relação com trabalho e Pessoas.
- Caso Nubank acrescido do 2.7: AskNu, marketplace e sinais de arquitetura em construção; preservado o conteúdo do evento.
- Matriz de seis capacidades no 3.1: sem equivalência integral entre empresas.
- Visão e apostas conectadas à nova evidência; quatro camadas no 8.2 e reuso de capacidades no 8.3.
- Roteiro com 32 quadros e continuidade revista. Mantidos limites editoriais anteriores: sem nomes de interlocutores do iFood, identificação da audiência, agenda temporal ou escolha prematura de jornadas.

## Verificação

Conferência local de capítulos, cinco apostas, campos narrativos, links, IDs e contagens dos catálogos realizada após a sincronização. As limitações de consulta e de estágio estão nas fontes, no registro da pesquisa fornecida e na estratégia. Verificação documental não equivale a auditoria das operações das empresas.
''')

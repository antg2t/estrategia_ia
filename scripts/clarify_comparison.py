from pathlib import Path
import re,json
R=Path(__file__).resolve().parents[1];O=R/'outputs/segunda-feira'
def read(p):return p.read_text(encoding='utf-8-sig')
def write(p,s):
 p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s.rstrip()+'\n',encoding='utf-8')
p=O/'ESTRATEGIA_IA_VP_PESSOAS_V2_FORA_PARA_DENTRO.md';s=read(p)
hist=O/'historico/ESTRATEGIA_V2_ANTES_COMPARACAO_DIDATICA.md'
if not hist.exists():write(hist,s)
a=s.index('### 3.1');b=s.index('## 4.',a)
section='''### 3.1 O que as pessoas conseguem fazer com IA — e o que a empresa organiza por trás

Os três casos ajudam a entender duas partes da mesma transformação. A primeira é a experiência de quem trabalha: fazer uma pergunta, receber ajuda ou criar uma solução. A segunda é o trabalho da empresa para conectar informações, reaproveitar recursos e manter a qualidade. Separar essas partes permite comparar empresas que usam ferramentas diferentes.

**Na experiência de quem trabalha:**

| Situação concreta | Prosus / Toqan | Mercado Livre | Nubank |
|---|---|---|---|
| **Como a pessoa começa a usar IA?** | Conversa com o Toqan para pesquisar, analisar informações ou criar recursos para sua rotina. | A empresa disponibilizou Cowork, ferramenta de trabalho com IA, a 31 mil funcionários. | Pode fazer perguntas ao AskNu dentro do Slack, aplicativo de comunicação interna. O banco também informa que todos os funcionários têm acesso a ferramentas de IA. |
| **Como encontra informação da empresa?** | Pode perguntar sobre dados em linguagem comum. A Prosus descreve um agente que identifica os dados necessários, faz a análise e devolve a resposta. | Os times dispõem de um serviço comum para buscar informação em documentos e bancos de dados e utilizá-la em aplicações de IA. | O AskNu procura a resposta no Confluence, onde a empresa mantém documentos internos, e mostra os links usados. |
| **Que trabalho pode ser feito com esse apoio?** | No iFood, a Prosus relata um agente que analisa o desempenho de restaurantes e prepara informações para quem atende esses parceiros. | O Verdi, plataforma de criação de agentes, permite construir soluções que combinam informações e acionam sistemas; o caso publicado descreve seu uso na mediação de devoluções. | A função descrita do AskNu é responder dúvidas. Pedir férias, contracheques e acessos aparecia como ampliação planejada no artigo de maio de 2025. |

Esses exemplos têm públicos diferentes: Cowork é uma ferramenta distribuída aos funcionários; a mediação de devoluções é um processo de negócio; AskNu é um serviço de informação interna. Eles mostram possibilidades de uso, sem pressupor que cada ferramenta faça todas as atividades das demais.

**Para que essas experiências possam crescer:**

| Capacidade da empresa | Prosus / Toqan | Mercado Livre | Nubank |
|---|---|---|---|
| **Permitir que mais pessoas criem soluções** | O Toqan permite descrever em linguagem comum o recurso desejado. A Prosus relata aprendizagem prática com equipes sem formação técnica. | O Verdi permite criar agentes com linguagem natural e regras simples; um executivo da empresa descreve seu uso por técnicos e não técnicos. | As fontes consultadas detalham construção por equipes de engenharia. Elas não esclarecem se existe uma ferramenta equivalente disponível para qualquer funcionário criar agentes sem programar. |
| **Evitar reconstruir a mesma capacidade** | O agente de análise de dados pode atender pessoas e também ser acionado por outros agentes. | Os times compartilham ferramentas prontas; uma capacidade de devolução pode acionar outra de logística. | Desenvolvedores encontram em um catálogo interno pacotes de instruções e ferramentas, chamados skills, para reutilizar em seus agentes. |
| **Definir acesso e verificar riscos** | No relato do iFood, as respostas baseadas em dados respeitam as permissões do usuário. | A plataforma incorpora controles de segurança e regras de uso dos modelos e ferramentas. | Antes de uma skill entrar no catálogo, um verificador chamado Skill Vetter examina riscos e pode exigir correções ou impedir sua distribuição. |

**O que a pesquisa esclareceu — e o que permanece sem resposta pública:** no Nubank, há acesso geral a ferramentas de IA e há um assistente identificado para buscar informação, o AskNu. As publicações consultadas não dizem se todos usam um mesmo aplicativo para conversar, criar agentes e executar tarefas. Também não localizamos uma atualização que confirme a entrega dos pedidos de férias pelo AskNu. No Mercado Livre, Cowork e Verdi estão documentados, mas não há descrição suficiente para afirmar que um pedido no Cowork consiga acionar diretamente os agentes criados no Verdi. Essas dúvidas se referem a conexões específicas entre ferramentas; não significam ausência de IA nas empresas.

**Fontes:** [Toqan, descrição do produto](https://toqan.ai/); [Prosus, exemplos de agentes em uso](https://www.prosus.com/news-insights/2025/building-an-agentic-workforce-what-we-have-learned-from-30000-ai-agents); [Mercado Livre, distribuição de Cowork](https://www.sec.gov/Archives/edgar/data/1099590/000109959026000014/meli-20260507xex991.htm); [Verdi, construção e combinação de capacidades](https://openai.com/index/mercado-libre/); [Nubank, funcionamento do AskNu](https://building.nubank.com/pt-br/solucao-de-ia-para-busca/); [Nubank, acesso dos funcionários à IA](https://international.nubank.com.br/pt-br/companhia/nubank-detalha-estrategia-de-transformacao-com-ia-baseada-em-dados-modelos-fundacionais-e-aconselhamento-financeiro-democratizado/); [Nubank, avaliação de skills](https://building.nubank.com/when-ai-skills-become-supply-chain-dependencies-2/). Complementos: newsletter Mercado Livre, SRC-PUB-016; relato de criação por não técnicos, SRC-PUB-018; conversa iFood, SRC-PER-001; materiais de contratação Nubank, SRC-PUB-023–026. Pesquisa atualizada em 06/09/2026.

**A conclusão para a Vivo é concreta:** a pessoa precisa conseguir expressar sua necessidade e receber uma ajuda útil; a empresa precisa conectar dados, ferramentas e responsáveis para entregar essa ajuda com qualidade. O aplicativo usado na conversa e os recursos que trabalham por trás devem ser pensados juntos. É com essa distinção que podemos avaliar o papel do Data Mesh, do Violeta e da experiência a construir para a VPP.

'''
s=s[:a]+section+s[b:]
s=s.replace('Vagas oficiais acrescentam sinais de direção: plataforma de inferência e orquestração; DXP para desenvolvimento de produtos; NuContext e Vector no trabalho de engenharia. São evidências de escopo e construção, sem comprovar um workspace universal para todos os funcionários.', 'As descrições de contratação explicam também o que as equipes técnicas estão construindo: serviços para executar modelos de IA; meios de coordenar agentes; a DXP, para apoiar o desenvolvimento de produtos; o NuContext, para organizar conhecimento usado pela IA; e o Vector, voltado ao trabalho de programação. Essas descrições mostram a atuação da engenharia. Não informam qual aplicativo um funcionário de outra área usaria para criar seus próprios agentes.')
s=s.replace('**O que aprendemos:** uma experiência coerente pode se apoiar em capacidades compartilhadas distribuídas por diferentes produtos. Nossa leitura é de uma composição modular, com integração e maturidade heterogêneas. O caso não demonstra um único equivalente ao Toqan nem que todo o roadmap esteja implantado.', '**O que aprendemos:** ferramentas diferentes podem aproveitar o mesmo conhecimento e as mesmas capacidades. No Nubank, o AskNu ajuda a encontrar informação, enquanto o catálogo de skills ajuda desenvolvedores a construir agentes. São contribuições diferentes. As fontes não descrevem uma conexão completa entre essas peças; por isso, cada uma é apresentada com sua função e com o estágio informado.')
s=s.replace('modelos, APIs e componentes de código, com controles embutidos e comunicação entre skills — capacidades que agentes podem acionar.', 'modelos de IA, conexões com outros sistemas e componentes de código. Também oferece controles e permite combinar skills — conjuntos de instruções e recursos que um agente pode acionar.')
s=s.replace('situa a plataforma sobre gateway de IA, dados e Fury, sua base de engenharia.', 'situa a plataforma sobre uma camada comum de acesso aos modelos de IA, serviços de dados e Fury, a base usada pelos times para desenvolver e operar software.')
write(p,s)

p=O/'ROTEIRO_NARRATIVO_V2_FORA_PARA_DENTRO.md';t=read(p)
t=t.replace('Uma arquitetura modular pode atender diferentes experiências sem uma porta universal comprovada.', 'AskNu ajuda funcionários a encontrar informação; o catálogo de skills ajuda desenvolvedores a construir agentes.')
t=t.replace('Toqan torna a experiência visível; Mercado Livre documenta recursos horizontais; Nubank acrescenta reuso e governança. Compare entrada, conhecimento, ações, construção, reuso e controles sem ranking de sofisticação.', 'Explique primeiro o que a pessoa faz: conversar com Toqan, usar Cowork ou perguntar ao AskNu no Slack. Depois, mostre como a empresa sustenta o uso: criação, reaproveitamento de capacidades e controles. Use o agente de dados acionado por pessoas e outros agentes como exemplo de reuso. As dúvidas são específicas: entrega das ações do AskNu, criação sem programação no Nubank e conexão Cowork–Verdi.')
t=t.replace('Três empresas e suas contribuições; matriz detalhada como apoio no capítulo 3.1.', 'Duas comparações: experiência da pessoa e capacidades da empresa. Tabelas completas no capítulo 3.1; no quadro, destaque um exemplo concreto de cada empresa.')
write(p,t)

pub=R/'evidence/public'
new=[(28,'Prosus — Building an agentic workforce','https://www.prosus.com/news-insights/2025/building-an-agentic-workforce-what-we-have-learned-from-30000-ai-agents','Three agents in action; The inflection point','Prosus descreve agente de análise de dados utilizado por pessoas e outros agentes, agente para análise de restaurantes e aprendizagem com equipes não técnicas.','Exemplos autorreportados. Data exata não confirmada; o texto mistura referências temporais. Contagens e equivalentes de produtividade não foram usados na revisão.'),(29,'Nubank — acesso dos funcionários a ferramentas de IA','https://international.nubank.com.br/pt-br/companhia/nubank-detalha-estrategia-de-transformacao-com-ia-baseada-em-dados-modelos-fundacionais-e-aconselhamento-financeiro-democratizado/','Três vantagens estruturais: dados, talento e cultura','Nubank afirma que todos os funcionários têm acesso a ferramentas de IA e que acompanha uso e impacto em todas as funções.','Publicação de 11/06/2026. Não identifica um aplicativo único nem diz que todo funcionário pode criar agentes sem programar.')]
for n,title,url,loc,st,limit in new:
 for file,row,key in [('PUBLIC_MANIFEST.jsonl',dict(source_id=f'SRC-PUB-{n:03}',title=title,url=url,published='2026-06-11' if n==29 else None,accessed='2026-09-06',kind='corporate_publication',locator=loc,limitations=limit),'source_id'),('PUBLIC_KNOWLEDGE_BASE.jsonl',dict(id=f'KU-PUB-{n:03}',type='concrete_capability_example',statement=st,context=limit,epistemic_status='declaração pública consultada',validation_needed=True,sources=[dict(source_id=f'SRC-PUB-{n:03}',locator=loc,url=url)]),'id')]:
  p=pub/file;rows=[json.loads(x) for x in read(p).splitlines() if x.strip()];rows=[x for x in rows if x[key]!=row[key]]+[row];write(p,'\n'.join(json.dumps(x,ensure_ascii=False) for x in rows))
note='''## Revisão vigente — comparação autocontida, 06/09/2026

O bloco 3.1 foi reescrito em duas tabelas: o que a pessoa consegue fazer e o que a empresa organiza para permitir esse uso. Removidas expressões vagas como “entrada universal não comprovada” e “outras experiências”. Cada ferramenta tem função concreta e as dúvidas restantes foram formuladas por extenso.

Pesquisa adicional: Prosus documenta agente de análise de dados usado por funcionários e outros agentes (SRC-PUB-028). Nubank confirma acesso de todos os funcionários a ferramentas de IA (SRC-PUB-029); isso não identifica aplicativo único ou criação sem programação. Não localizada confirmação pública posterior de pedidos de férias executados pelo AskNu ou de conexão direta Cowork–Verdi. A busca não comprova inexistência dessas funções. O artigo AskNu continua separando busca e execução futura.

Catálogo público: 29 fontes/29 unidades. Camada pessoal permanece oito fontes/60 unidades. Roteiro mantém 32 quadros, com notas da comparação e do caso Nubank sincronizadas. Não usar “integração heterogênea”, “reuso” ou “orquestração” como substitutos de explicação concreta ao leitor.

'''
for file in ['docs/PROJECT_STATUS.md','CLAUDE.md','START_HERE.md','evidence/public/INTEGRATED_SYNTHESIS.md','evidence/public/README.md']:
 p=R/file;t=read(p);pos=t.index('\n')+1;write(p,t[:pos]+'\n'+note+t[pos:])
write(R/'docs/PESQUISA_COMPARACAO_DIDATICA_2026-09-06.md','# Pesquisa e clareza da comparação de IA\n\n'+note+'''## Perguntas verificadas

| Dúvida | Resultado e tratamento |
|---|---|
| O que significa “entrada” no Nubank? | Funcionário pergunta no Slack ao AskNu; comunicado de junho de 2026 confirma acesso geral a ferramentas de IA, sem listar um aplicativo para todas as atividades. |
| AskNu já pede férias? | Busca por AskNu, férias, actions e atualizações de 2026 retornou a publicação de maio de 2025, que descreve execução como próximo passo. Mantido o estágio daquela fonte, sem concluir o estado atual por ausência de publicação. |
| Qualquer funcionário Nubank cria agentes? | Materiais consultados detalham engenharia e catálogo para desenvolvedores. Não localizada descrição equivalente para criação sem programação por toda a empresa. |
| Cowork aciona Verdi? | Comunicado Q1 e materiais de Verdi documentam as peças. Busca adicional encontrou menções conjuntas em recrutamento, insuficientes para provar integração. Nenhuma seta foi inferida. |
| Qual exemplo torna reuso compreensível? | Prosus descreve agente de dados que atende pessoas e é chamado por outros agentes. Incorporado com fonte específica, sem importar números de produtividade. |

## Critério editorial aplicado

Cada célula identifica uma pessoa ou equipe, uma ferramenta ou recurso e uma ação compreensível. Termos necessários foram explicados. O leitor pode entender o argumento sem abrir as fontes. Links servem para conferência, não para preencher partes ausentes da explicação.
''')

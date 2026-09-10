from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1];O=R/'outputs/segunda-feira'; E=R/'evidence'
def read(p):return p.read_text(encoding='utf-8-sig')
def write(p,s):
 p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s.rstrip()+'\n',encoding='utf-8')
def add(p,row,key):
 rows=[json.loads(x) for x in read(p).splitlines() if x.strip()]
 rows=[x for x in rows if x[key]!=row[key]]+[row]
 write(p,'\n'.join(json.dumps(x,ensure_ascii=False) for x in rows))
p=O/'ESTRATEGIA_IA_VP_PESSOAS_V2_FORA_PARA_DENTRO.md';s=read(p)
archive=O/'historico/ESTRATEGIA_V2_ANTES_TRIANGULACAO_PLATAFORMAS.md'
if not archive.exists():write(archive,s)
newsletter=re.search(r'https://investor\.mercadolibre\.com/open-file\?file=[^)\s]+',s).group()
urls={16:newsletter,17:'https://openai.com/index/mercado-libre/',18:'https://www.linkedin.com/posts/oscarmullin_ai-generativeai-ecommerce-activity-7285470574787596288-Ips2',19:'https://www.sec.gov/Archives/edgar/data/1099590/000109959026000014/meli-20260507xex991.htm',20:'https://www.sec.gov/Archives/edgar/data/1099590/000109959026000006/meli-20251231.htm',21:'https://building.nubank.com/pt-br/solucao-de-ia-para-busca/',22:'https://building.nubank.com/when-ai-skills-become-supply-chain-dependencies-2/',23:'https://jobs.ashbyhq.com/nubank/396b15fb-99a7-46ab-a687-214413586a01',24:'https://jobs.ashbyhq.com/nubank/038071ac-4c89-4ba3-aee9-f3f48c92ee41',25:'https://jobs.ashbyhq.com/nubank/c5d9d4bf-ed51-4fdc-b658-58056b3fec19',26:'https://jobs.ashbyhq.com/nubank/268e385a-35a4-442b-8078-2bd36d5491ab',27:'https://www.anthropic.com/webinars/future-of-ai-at-work-introducing-cowork'}
sources=[
(16,'Mercado Livre — Investor Newsletter June 2026','2026-06','corporate_newsletter','p. 1, GenAI Is Just as Embedded in the Business; platform; hiring','Plataforma compartilhada com roteamento único, catálogo, RAG sobre documentos e bases, memória e controles; Maxwell suporta agentes de atendimento.','Declarações da empresa. Disponibilidade superior a 99,99% autorreportada, sem método auditado; não prova integração Cowork–Verdi.'),
(17,'Mercado Libre introduces Verdi',None,'vendor_customer_case','Saving millions; Delivering a new standard; Building Verdi','Verdi combina modelos, APIs e nós Python, criação em linguagem natural e controles embutidos; skills podem interagir.','Caso publicado pelo fornecedor com declarações do cliente; não prova autonomia irrestrita nem ganhos universais.'),
(18,'Verdi e a base GenAI — relato público de executivo',None,'executive_public_post','parágrafos Verdi e GenAI tech stack','Post descreve criação por técnicos e não técnicos em linguagem natural/DSL; Verdi sobre GenAI Gateway, Data/ML Platform e Fury.','Declaração pública individual; criação acessível não equivale a uso comprovado por todos. Data não confirmada nesta leitura.'),
(19,'MercadoLibre — Q1 2026 results','2026-05-07','corporate_results_release','parágrafo More broadly, we have rolled out Claude Cowork','A empresa informa distribuição de Claude Cowork a 31.000 funcionários.','O texto diz 31.000, não mais de 31.000. Distribuição não mede usuários ativos ou benefício; não documenta conexão com Verdi.'),
(20,'MercadoLibre — Form 10-K 2025','2026-02-25','annual_filing','Human Capital — adoção de IA, Talent Acquisition e Employee Support','Relata aproximadamente 95% de adoção de ferramentas de IA e bot de Employee Support com mais de 1,4 milhão de consultas anuais, self-service de 70% a 93%; screening autônomo em experimentação.','Exercício 2025. Trecho recuperado no índice de busca da própria SEC; abertura integral excedeu limite do leitor. Não foi realizada auditoria completa do filing; 95% refere-se a AI tools, não especificamente GenAI.'),
(21,'AskNu — solução RAG para funcionários','2025-05-28','company_engineering_article','A Solução; Métricas; Conclusão / Próximos Passos','AskNu no Slack consulta Confluence e retorna fontes; artigo separa busca em operação e ações em sistemas no roadmap.','Seis meses após lançamento: 5 mil usuários, 280 mil mensagens, 80% feedback positivo com resposta de 6%, 70% retorno em 30 dias, 96% redução reportada de tickets nos domínios internos e 74% das respostas auditadas classificadas como precisas. Não extrapolar domínios nem tratar feedback como acurácia.'),
(22,'When AI skills become supply-chain dependencies','2026-09-02','company_engineering_article','Review before distribution; How Skill Vetter works','Nubank relata mais de 2.000 skills avaliadas antes da distribuição; Skill Vetter avalia riscos antes de ingresso no marketplace interno para desenvolvedores.','Escopo de desenvolvimento. Skills analisadas não são agentes ativos, skills aprovadas ou cobertura de toda a empresa; controle não garante ausência de risco.'),
(23,'Lead AI Engineer — Productivity Systems',None,'job_description','responsabilidades — AI stack e Golden Paths','Vaga descreve agentes, tool calling, MCP, RAG e orquestração multiagente, além de referências para outros times construírem workflows.','Texto oficial indexado; URL equivalente localizada após URL informada retornar página sem corpo. Responsabilidades de contratação indicam direção e escopo, não implantação integral.'),
(24,'Lead Software Engineer — AI Agents & Orchestration',None,'job_description','About the Role; Responsibilities','Vaga menciona GenAI Platform com inferência, avaliação e orquestração para workflows e RAG.','Texto oficial indexado. Foco inclui experiências financeiras para clientes; não implica workspace universal de funcionários.'),
(25,'Staff Software Engineer — Digital Experience Platform',None,'job_description','About the role; quatro produtos DXP','DXP é descrita em construção: Studio, Dictionary, Spec Protocol e Workflow, para acelerar desenvolvimento de produtos.','Texto oficial indexado. Não comprova implantação completa ou experiência horizontal para toda a força de trabalho.'),
(26,'AI Developer Experience — mandato e workstreams',None,'job_description','Core workstreams; Longer term','Vaga descreve NuContext, Vector, revisão de código, AI SRE e roteamento; AI Enablement Platform aparece no horizonte.','Texto oficial indexado. Escopo de engenharia; maturidade heterogênea. Não equiparar automaticamente Vector desta vaga à camada de abstração descrita no evento pessoal.'),
(27,'The Future of AI at Work — Introducing Cowork',None,'vendor_product_webinar','apresentação do produto','Fonte do fornecedor caracteriza Cowork como experiência de trabalho com IA.','Página de produto/evento, não prova da configuração nem resultados no Mercado Livre; a distribuição é documentada por SRC-PUB-019.')]
for num,title,date,kind,loc,statement,limits in sources:
 sid=f'SRC-PUB-{num:03}'
 add(E/'public/PUBLIC_MANIFEST.jsonl',dict(source_id=sid,title=title,url=urls[num],published=date,accessed='2026-09-06',kind=kind,locator=loc,limitations=limits),'source_id')
 add(E/'public/PUBLIC_KNOWLEDGE_BASE.jsonl',dict(id=f'KU-PUB-{num:03}',type='horizontal_ai_evidence',statement=statement,context=limits,epistemic_status='declaração pública consultada; escopo e estágio delimitados',validation_needed=True,sources=[dict(source_id=sid,locator=loc,url=urls[num])]),'id')

provided=R/'sources/personal/outras fontes pessoais/pesquisa_plataformas_agenticas_2026-09-06.md'
text='''# Pesquisa fornecida — plataformas e experiências de IA

Recebida na conversa em 06/09/2026. Registro editorial do conteúdo fornecido, com seus argumentos, fontes e alegações; não é cópia literal da mensagem. As correções de verificação estão separadas abaixo.

## Tese e régua propostas

A pesquisa compara Toqan, Mercado Livre e Nubank por seis capacidades: entrada comum, conhecimento/dados, ações em ferramentas, criação de agentes/fluxos, reuso e governança. Propõe separar experiência horizontal e plataforma e definir lacunas Vivo por capacidade, em vez de procurar um equivalente único de Toqan.

## Mercado Livre

Arquitetura sugerida: Cowork como experiência de funcionário; Verdi para construir agentes; Maxwell para atendimento; roteamento, catálogo, RAG e memória como serviços horizontais; Fury como base; agentes especializados sobre essas capacidades. A pesquisa não demonstra conexão direta de Cowork com Verdi/gateway. Aponta criação por não técnicos no post público e no caso Verdi. Relata disponibilidade acima de 99,99%, distribuição de Cowork a mais de 31 mil, adoção próxima de 95% e Employee Support com 1,4 milhão de consultas e self-service de 70% para 93%.

## Nubank

AskNu: busca corporativa no Slack, com Confluence, fontes e roteamento por domínio; ações como contracheques, férias e acessos aparecem como próximos passos. A pesquisa relata 5 mil usuários, 280 mil mensagens, 80% feedback positivo, 70% retorno em 30 dias, 96% redução de tickets nos domínios cobertos e 74% de respostas internas auditadas precisas.

Marketplace: skills, contexto, workflows e ferramentas reutilizáveis; fluxo criador, PR, Skill Vetter, marketplace, desenvolvedores; mais de 2 mil skills avaliadas. Vagas apontam Productivity Systems, GenAI Platform, DXP (Studio, Dictionary, Spec Protocol, Workflow) e AI Developer Experience (NuContext, Vector, Code Review, AI SRE, routing e plataforma de enablement no horizonte). A pesquisa ressalva foco em desenvolvimento e maturidade heterogênea, sem comprovar um único workspace universal.

## Prosus / Toqan

A pesquisa enfatiza experiência simples de conversa, criação e ações conectadas a sistemas. Informa 25 mil usuários em 22 empresas, 5 mil agentes ativos diariamente e 747 mil ações mensais. Esses números não foram confirmados nesta revisão e não foram promovidos a fatos na estratégia. A identidade e a proposta do produto já estão em SRC-PUB-015.

## Implicação proposta para a Vivo

Quatro decisões: fundação de IA; capacidades reutilizáveis de conhecimento e ações; construção/orquestração; experiência horizontal. Violeta e Data Mesh podem atender partes distintas, conforme validação técnica. Integração não exige que todas as capacidades sejam um único produto. Reuso pode permitir que diferentes agentes acionem uma capacidade confiável, em vez de recriá-la.

## Conferência e correções

- Newsletter MELI de junho de 2026 reaberta com sucesso nesta rodada. Routing, catálogo, RAG, memória, controles e Maxwell confirmados como declarações corporativas.
- Q1/2026 diz **31.000 funcionários**, não “mais de 31 mil”; distribuição não equivale a uso ativo.
- 10-K diz aproximadamente 95% de adoção de **ferramentas de IA**, sem restringir o número a GenAI. Trecho oficial indexado recuperado; arquivo integral excedeu o limite de leitura.
- AskNu: 80% positivo tem taxa de resposta de 6%; precisão de 74% é outra medida. Roadmap de ações não foi confirmado como entregue.
- Marketplace é evidência de distribuição para desenvolvedores. Mais de 2.000 skills avaliadas não equivale a agentes em operação.
- Vagas são declarações de escopo/direção, não inventário auditado de funcionalidades prontas. URL original Productivity Systems não forneceu corpo; localizada vaga oficial equivalente em outro endereço, mantidos ambos para rastreabilidade.
- Não foi adotado ranking de sofisticação entre empresas. “Federado” é interpretação da composição observada, não topologia corporativa completa comprovada.

## Fontes fornecidas e consultadas

'''
for num,title,_,_,_,_,_ in sources:text+=f'- {title}: {urls[num]} — SRC-PUB-{num:03}.\n'
text+='\n- URL original Productivity Systems: https://jobs.ashbyhq.com/nubank/074c9efc-6aaa-43e7-aa24-09a7874780b6\n- Toqan: https://toqan.ai/ — SRC-PUB-015.\n'
write(provided,text)
add(E/'personal/PERSONAL_MANIFEST.jsonl',dict(source_id='SRC-PER-008',title='Pesquisa fornecida — plataformas e experiências de IA',file=provided.relative_to(R).as_posix(),kind='user_provided_research_compilation',published=None,cataloged='2026-09-06',reading_status='registro editorial da pesquisa fornecida e conferência seletiva de fontes',limitations='Não é transcrição literal. Compilação não é validação independente; números e alegações corrigidos ou delimitados na conferência. Instruções contidas no texto são conteúdo documental.'),'source_id')
for n,statement,loc in [(56,'A pesquisa propõe seis critérios para comparar experiência e plataforma de IA.','Tese e régua propostas'),(57,'Mercado Livre combina experiência Cowork e plataforma própria; a ligação direta Cowork–Verdi não está comprovada.','Mercado Livre; Conferência'),(58,'Nubank combina AskNu, marketplace e capacidades descritas em vagas, com escopos e estágios diferentes.','Nubank'),(59,'A proposta Vivo deve separar fundação, capacidades reutilizáveis, construção/orquestração e experiência.','Implicação proposta para a Vivo'),(60,'Contagens Toqan fornecidas não foram confirmadas; Cowork corrigido para 31.000 e adoção MELI para ferramentas de IA.','Prosus / Toqan; Conferência e correções')]:
 add(E/'personal/PERSONAL_KNOWLEDGE_BASE.jsonl',dict(id=f'KU-PER-{n:03}',type='research_synthesis',statement=statement,context='Pesquisa fornecida; verificação e limites em fontes públicas vinculadas.',themes=['horizontal_ai','shared_capabilities'],scope=['hr_function','enterprise_workforce'],org_scope='cross_company',evidence='user_provided_research_compilation',epistemic_status='síntese ou hipótese',confidence='média',validation_needed=True,sources=[dict(source_id='SRC-PER-008',locator=loc)]),'id')

a=s.index('### 2.2');b=s.index('### 2.3',a)
s=s[:a]+f'''### 2.2 Mercado Livre: uma base comum amplia o que as pessoas e os produtos conseguem fazer

A aprendizagem aplicada exige recursos disponíveis no trabalho. O Mercado Livre mostra como essa condição pode ser construída em escala, combinando ferramentas para funcionários e capacidades técnicas compartilhadas.

Na newsletter de junho de 2026, a empresa descreve um roteamento comum que conecta aplicações e agentes a modelos, um catálogo de ferramentas, busca em documentos e bases corporativas, memória entre interações e controles compartilhados. A mesma publicação apresenta Maxwell como plataforma de agentes de atendimento. São recursos que diferentes produtos podem aproveitar sem reconstruir cada integração. [Mercado Livre, newsletter de junho de 2026]({newsletter}), p. 1; SRC-PUB-016.

O **Verdi** acrescenta construção de aplicações e agentes com linguagem natural, modelos, APIs e componentes de código, com controles embutidos e comunicação entre skills — capacidades que agentes podem acionar. [Caso Verdi publicado pela OpenAI]({urls[17]}), SRC-PUB-017. Um relato público de executivo explicita criação por técnicos e não técnicos e situa a plataforma sobre gateway de IA, dados e Fury, sua base de engenharia. [Relato sobre Verdi]({urls[18]}), SRC-PUB-018.

Em outra camada, o resultado do primeiro trimestre de 2026 informa a distribuição de **Claude Cowork a 31 mil funcionários**. Isso documenta alcance de disponibilização, sem demonstrar uso ativo de todos. [Mercado Livre, resultado Q1/2026]({urls[19]}), SRC-PUB-019.

| Capacidade | Peça documentada | O que o caso permite distinguir |
|---|---|---|
| Experiência do funcionário | Cowork | Acesso a uma ferramenta de trabalho com IA. |
| Construção de soluções | Verdi | Meios para criar e compor aplicações e agentes. |
| Recursos compartilhados | Roteamento, catálogo, busca e memória | Capacidades reutilizáveis entre produtos. |
| Base tecnológica | Fury e plataformas de dados/IA | Suporte técnico à construção e operação. |

Essas peças coexistem. As fontes não demonstram uma conexão direta entre Cowork e todo o catálogo do Verdi; a comparação não presume essa integração.

A transformação também chega a Pessoas. O relatório anual de 2025 registra um bot de Employee Support com mais de 1,4 milhão de consultas anuais e elevação do self-service de 70% para 93%, além de experimentação de screening autônomo. São resultados e estágios declarados pela empresa. [Form 10-K 2025]({urls[20]}), SRC-PUB-020. A newsletter de junho acrescenta avaliação de desenvolvedores trabalhando com IA: recursos disponíveis e competências esperadas evoluem juntos.

**O que aprendemos:** experiência de uso e plataforma compartilhada são capacidades diferentes e complementares. A primeira aproxima IA das pessoas; a segunda permite que os produtos evoluam sem reconstruir sua base a cada iniciativa. O próximo caso mostra como essa transformação se conecta a trabalho, talento e organização.

'''+s[b:]
a=s.index('## 3.')
s=s[:a]+f'''### 2.7 Nubank: diferentes experiências podem reutilizar capacidades comuns

A estratégia apresentada no evento também pode ser lida à luz de evidências públicas de produtos e engenharia. Elas mostram peças complementares, com estágios distintos.

Em maio de 2025, o Nubank descreveu o **AskNu**, assistente no Slack que busca conhecimento no Confluence e retorna fontes. O artigo reporta redução de tickets nos domínios cobertos, mas classifica apenas 74% das respostas internas auditadas como precisas naquele momento. Solicitar férias, contracheques e acessos aparece como próximo passo de integração, não como entrega concluída. [Nubank, AskNu]({urls[21]}), SRC-PUB-021.

Em setembro de 2026, outra publicação descreve um **marketplace interno de skills para desenvolvedores**. Antes da distribuição, o Skill Vetter avalia riscos; mais de 2 mil skills haviam sido analisadas. A unidade de reuso é uma capacidade que diferentes agentes podem utilizar. [Nubank, governança de skills]({urls[22]}), SRC-PUB-022.

Vagas oficiais acrescentam sinais de direção: plataforma de inferência e orquestração; DXP para desenvolvimento de produtos; NuContext e Vector no trabalho de engenharia. São evidências de escopo e construção, sem comprovar um workspace universal para todos os funcionários. As fontes e seus estágios estão no [catálogo público](../../evidence/public/README.md), SRC-PUB-023–026.

**O que aprendemos:** uma experiência coerente pode se apoiar em capacidades compartilhadas distribuídas por diferentes produtos. Nossa leitura é de uma composição modular, com integração e maturidade heterogêneas. O caso não demonstra um único equivalente ao Toqan nem que todo o roadmap esteja implantado.

**Podemos agora separar o que o usuário experimenta, o que os produtos reutilizam e como essa reutilização é governada. Essa distinção fortalece os critérios para a Vivo.**

'''+s[a:]
s=s.replace('| Atualizar competências | Mercado Livre: seleção observa trabalho com IA. | Critérios de desenvolvimento e talento precisam acompanhar as atividades que mudam. |','| Ampliar capacidade de atuação | Mercado Livre: experiência Cowork, construção Verdi e serviços compartilhados; seleção acompanha o trabalho com IA. | Preparação, experiência do usuário e plataforma devem evoluir de forma conectada. |')
a=s.index('## 4.')
s=s[:a]+'''### 3.1 Três referências complementares, seis capacidades para comparar

Prosus/Toqan torna visível a experiência acessível; Mercado Livre documenta a base horizontal e a distribuição de uma ferramenta generalista; Nubank acrescenta evidências de busca, reuso e avaliação de componentes. A combinação reforça a aposta sem depender de reproduzir um produto específico.

| Capacidade | Prosus / Toqan | Mercado Livre | Nubank |
|---|---|---|---|
| **Entrada para o usuário** | Workspace de conversa, criação e ações. | Cowork distribuído; integração com plataforma própria não demonstrada. | AskNu e outras experiências; entrada universal não comprovada. |
| **Conhecimento e dados** | Conexões descritas pelo produto e pelo benchmark. | Busca corporativa compartilhada e contexto entre interações. | AskNu documentado; contexto adicional em iniciativas de engenharia. |
| **Ações em ferramentas** | Capacidade declarada do produto. | Agentes e skills com APIs. | Capacidades descritas em iniciativas; ações do AskNu eram roadmap na publicação. |
| **Construção** | Criação acessível declarada. | Verdi; relato explícito de criação por não técnicos. | Vagas descrevem construção/orquestração; democratização ampla não comprovada. |
| **Reuso** | Recursos compartilháveis. | Catálogo comum e composição de skills. | Marketplace documentado no escopo de desenvolvimento. |
| **Governança** | Controles de acesso e uso no relato. | Controles comuns de plataforma. | Avaliação antes da distribuição de skills; outros controles descritos por iniciativa. |

**Fontes:** SRC-PUB-015–026 e SRC-PER-001. A tabela compara capacidades e evidências, não classifica qual empresa é mais sofisticada. Vagas indicam direção e responsabilidades; relatos de produto e resultados indicam outros níveis de evidência.

**Uma plataforma para construir agentes não assegura, por si só, uma experiência integrada para quem trabalha. Uma boa interface também depende de capacidades confiáveis por trás.** Essa separação orienta a leitura dos projetos da Vivo a seguir.

'''+s[a:]
s=s.replace('O Violeta pode participar da fundação técnica; o desenho de uma camada integrada para o usuário ainda precisa ser estabelecido no contexto da VPP.', 'A participação do Violeta deve ser avaliada por capacidade: fundação, construção e orquestração podem ter cobertura distinta da experiência do usuário. Essa última ainda precisa ser estabelecida no contexto relatado da VPP.')
s=s.replace('| Direção estratégica, PMs e uma camada acessível de IA conectam intenção e capacidade de agir no iFood. |','| iFood conecta direção e PMs à atuação; Toqan, Mercado Livre e Nubank mostram experiência, plataforma e reuso como capacidades complementares. |')
s=s.replace('O Toqan torna visível essa possibilidade. O ponto de partida da pessoa é sua pergunta ou intenção; a solução aciona as capacidades disponíveis por trás. Para a VPP, o objetivo é que a infraestrutura de dados e agentes se converta em autonomia cotidiana, com apoio para quem usa e cria.', 'Três referências sustentam a aposta: Toqan torna a experiência visível; Mercado Livre documenta serviços horizontais e uma ferramenta distribuída aos funcionários; Nubank mostra conhecimento e componentes reutilizáveis em experiências distintas. Para a VPP, o objetivo é autonomia cotidiana apoiada em uma base comum. A experiência pode atravessar canais e produtos, preservando coerência para quem usa.')
s=s.replace('Essa aposta orienta uma experiência comum, cuja solução tecnológica deve aproveitar o ecossistema corporativo. O Violeta pode ser parte da base; a experiência de uso, as integrações e a criação acessível são capacidades adicionais a desenvolver ou incorporar.', 'Essa aposta separa duas responsabilidades: construir capacidades compartilhadas de IA e oferecer uma experiência acessível que as mobilize. A cobertura do Violeta e do Data Mesh deve ser avaliada nesse conjunto, aproveitando o ecossistema corporativo.')
s=s.replace('O investimento se acumula: cada produto de dados e cada conjunto de conhecimento bem mantido pode servir a mais de uma necessidade.', 'O investimento se acumula: cada produto de dados, conjunto de conhecimento e capacidade de ação bem mantidos pode servir a mais de uma necessidade. O marketplace do Nubank amplia essa lógica para componentes avaliados antes da distribuição. Na VPP, uma capacidade como consultar uma informação de férias poderia ser mantida uma vez e acionada por diferentes agentes, sempre com as permissões e regras apropriadas. Esse é um exemplo de desenho proposto, não uma integração existente.')
a=s.index('### 8.2');b=s.index('## 9.',a)
s=s[:a]+'''### 8.2 Quatro camadas, quatro decisões de capacidade

A experiência pretendida requer escolhas distintas. A arquitetura abaixo é uma proposta de referência para a VPP, derivada dos mecanismos observados; não reproduz uma arquitetura completa de qualquer benchmark.

| Camada | Capacidade a assegurar | Decisão estratégica |
|---|---|---|
| **Fundação de IA** | Acesso a modelos, roteamento, identidade, segurança e acompanhamento da operação. | Quais serviços corporativos atenderão aos produtos de Pessoas e com quais condições de continuidade. |
| **Capacidades reutilizáveis** | Conhecimento, produtos de dados, busca, ferramentas e ações com definições e responsáveis. | O que deve ser mantido como capacidade comum e como será publicado, atualizado e avaliado. |
| **Construção e orquestração** | Criar agentes, combinar etapas e coordenar ferramentas e intervenção humana. | Como especialistas e outros criadores poderão construir, testar e sustentar soluções. |
| **Experiência do usuário** | Conversar, encontrar informação, criar recursos e solicitar ações com clareza. | Como oferecer uma experiência coerente nos canais de trabalho, sem exigir conhecimento da estrutura técnica. |

Data Mesh participa da organização dos produtos de dados. Violeta pode atender partes da construção e de outras camadas conforme sua cobertura real. A situação relatada da VPP indica uma base por código e a falta da experiência acessível integrada. Isso não permite concluir que um único componente deva preencher todas as lacunas.

O referencial para desenvolver, adquirir ou combinar soluções passa a ser a cobertura dessas capacidades. A experiência pode ter mais de uma interface e ainda compartilhar identidade, conhecimento e ferramentas. Uma entrada visual única também pode esconder integrações fragmentadas; sua aparência não demonstra integração operacional.

### 8.3 Reutilizar capacidades para que a autonomia possa crescer

A construção distribuída funciona melhor quando as pessoas podem aproveitar recursos conhecidos e avaliados. Uma capacidade de consulta deve ter significado claro, permissões, responsável e condições de manutenção. Diferentes agentes podem compor essas capacidades para atender a necessidades distintas.

Isso muda a unidade de investimento: além de soluções finais, a VP precisa manter componentes que várias soluções utilizem. Um catálogo torna essas capacidades encontráveis; a avaliação antes da distribuição reduz a propagação de falhas; a manutenção preserva sua utilidade. A aplicação dessa lógica a Pessoas é uma recomendação inspirada no marketplace de desenvolvimento do Nubank, com controles adequados ao impacto de cada uso.

**O alvo estratégico é uma experiência acessível sustentada por capacidades compartilhadas e governadas.** A organização dos produtos e das responsabilidades deve tornar essa combinação possível.

'''+s[b:]
s=s.replace('| **Capacidades compartilhadas** | Sustentar dados, conhecimento, experiência de IA e condições técnicas de entrega. | Acumular reuso e ampliar autonomia com qualidade. |', '| **Capacidades compartilhadas** | Sustentar as quatro camadas, com responsáveis pela experiência, pelos componentes reutilizáveis e pela operação técnica. | Acumular reuso e ampliar autonomia com qualidade, mantendo as responsabilidades de cada camada explícitas. |')
s=s.replace('SRC-PER-007, os esclarecimentos desta revisão.', 'SRC-PER-007, os esclarecimentos anteriores; SRC-PER-008, a nova pesquisa comparativa e sua conferência. As fontes primárias adicionais estão em SRC-PUB-016–027, no catálogo público.')
s=s.replace('a descrição pública do Toqan', 'a descrição pública do Toqan')
s=s.replace('O [roteiro narrativo]', 'A distribuição de Cowork não comprova uso ativo nem integração com Verdi. As vagas Nubank indicam escopo e direção; AskNu e o marketplace têm publicações próprias, com limites de estágio e público. Números de escala adicionais do Toqan fornecidos na pesquisa não foram confirmados e não sustentam o argumento principal.\n\nO [roteiro narrativo]')
write(p,s)

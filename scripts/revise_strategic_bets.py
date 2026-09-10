from pathlib import Path
import re, json

R=Path(__file__).resolve().parents[1]
O=R/'outputs/segunda-feira'
P=O/'ESTRATEGIA_IA_VP_PESSOAS_V2_FORA_PARA_DENTRO.md'
def read(p): return p.read_text(encoding='utf-8-sig')
def write(p,s):
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(s.rstrip()+'\n',encoding='utf-8')

s=read(P)
write(O/'historico/ESTRATEGIA_V2_ANTES_GRANDES_APOSTAS.md',s)
s=s.replace(' O texto se dirige inicialmente à diretora e ao CHRO, com os conceitos explicados no próprio percurso.','')
s=s.replace('As escolhas, o modelo operativo e a execução desdobram essa visão.', 'As grandes apostas da VP, a experiência integrada de IA e o modelo operativo desdobram essa visão.')
s=s.replace('visão 2028 → escolhas e modelo operativo → execução e resultado.', 'visão 2028 → grandes apostas → experiência integrada e modelo operativo → evolução e valor.')
s=s.replace('Suzana Kubric apresentou, como CHRO,', 'uma executiva de Pessoas apresentou')
a=s.index('### 2.5 iFood:'); b=s.index('## 3.',a)
s=s[:a]+'''### 2.5 iFood: o planejamento orienta os produtos e os PMs organizam a entrega

Na conversa com uma executiva do iFood, People aparece participando da transformação empresarial por cultura, redesenho da força de trabalho e desenvolvimento de competências. A agenda combina atuação multidisciplinar com capacidades de produto, tecnologia e dados.

Uma diferença relevante está na origem das prioridades. Segundo o relato, o direcionamento estratégico orienta quais produtos recebem capacidade de gestão. A liderança funcional define a direção do tema; os **PMs, profissionais de gestão de produto**, organizam demandas, fazem escolhas sobre a evolução do produto e articulam a capacidade técnica. As necessidades podem vir de diferentes áreas, mas sua tradução em trabalho de produto tem uma função responsável.

O planejamento estabelece um campo de atuação antes da chegada de cada solicitação. O PM ainda decide o que cabe, o que deve esperar e como organizar o caminho; essas escolhas têm uma referência anterior de direção e alocação. A contribuição do caso é mostrar como estratégia e metas podem reduzir a necessidade de reconstruir a justificativa de prioridade a cada pedido.

**Fonte:** [benchmark iFood catalogado — SRC-PER-001](../../evidence/personal/README.md), Participante 2, 05:32–09:59 e 24:57–27:40. A data da conversa não está confirmada. O relato descreve decisões de roadmap e alocação; não demonstra ausência de priorização.

**Definir quem organiza o produto resolve uma parte da coordenação. Outra parte depende de tornar a tecnologia utilizável por quem conhece o trabalho.**

### 2.6 iFood: uma camada de IA aproxima as pessoas dos dados e da criação

A executiva descreve o **Toqan**, plataforma da Prosus, como uma interface conversacional conectada aos recursos da empresa. Na experiência relatada, a pessoa faz sua pergunta; a solução ajuda a esclarecer a intenção e consulta a base de dados conforme as conexões e permissões disponíveis. O usuário não precisa navegar pelo ambiente de dados nem montar manualmente a consulta a cada interação.

Isso muda o significado de democratizar dados. A pessoa passa a interagir com a necessidade de negócio, enquanto a solução cuida do acesso técnico por trás. Essa experiência depende de uma camada de definições de negócio — que explica o significado dos dados — e de regras de acesso. A interface simples se apoia num trabalho estruturante que continua necessário.

O relato também descreve criação e experimentação de recursos pelos próprios usuários, com pessoas de referência em dados apoiando as áreas. A [apresentação oficial do Toqan](https://toqan.ai/) o caracteriza como um ambiente de IA da Prosus para conversar, analisar e criar aplicações e fluxos em linguagem natural, conectado a ferramentas e dados. A descrição pública confirma a proposta do produto; o funcionamento específico com dados de Pessoas vem da conversa de benchmark.

**O que aprendemos:** uma camada conversacional e agêntica pode aproximar consumo de dados, uso de soluções e criação pelo usuário. “Agêntica” significa que a solução pode acionar ferramentas e etapas para atender ao pedido, dentro das permissões e integrações configuradas. A pessoa não precisa conhecer essas conexões para usar o serviço.

O próprio caso evidencia o trabalho necessário para sustentar essa autonomia: definições de dados, apoio à aprendizagem, revisão e manutenção. A executiva relata baixa adesão em alguns usos, análises imprecisas e esforço crescente de revisão. Uma experiência acessível amplia a capacidade de usar e criar; qualidade e continuidade precisam crescer junto.

**Fonte:** SRC-PER-001, Participante 2, 12:02–18:48, 19:52–20:24 e 33:23–38:47; Toqan, página oficial consultada em 06/09/2026. A conversa descreve integração com Databricks; a conexão com Data Mesh é a leitura arquitetural discutida neste material, não uma afirmação de acesso irrestrito a qualquer dado.

**Os dois mecanismos se complementam: direção e gestão de produto organizam onde investir; uma experiência integrada permite que essa capacidade chegue às pessoas.**

'''+s[b:]
s=s.replace('| Sustentar a entrega | iFood: gestão de produto, responsáveis pelos dados, capacidade técnica e manutenção. | O resultado precisa de um responsável que acompanhe sua evolução. |', '| Conectar estratégia e entrega | iFood: direção funcional e alocação orientam o trabalho organizado pelos PMs. | Metas e escolhas estratégicas devem orientar a carteira antes da chegada dos pedidos. |\n| Ampliar a autonomia | iFood: Toqan conecta conversa, dados e criação, com apoio e manutenção. | A base técnica precisa chegar ao usuário por uma experiência integrada e acessível. |')
a=s.index('### 4.2');b=s.index('## 5.',a)
s=s[:a]+'''### 4.2 Os projetos da Vivo já apontam para uma transformação mais ampla

A análise dos projetos e dos registros disponíveis da Vivo mostra movimentos complementares: desenvolver pessoas, estruturar dados, criar uma base de agentes, reinventar serviços e evoluir a gestão de produtos. O desafio é conectar esses movimentos numa capacidade comum da VP.

| Movimento | O que está sendo construído | Significado estratégico |
|---|---|---|
| **Eu Vivo IA** | Formação e mobilização de líderes, com demanda por aplicação e apoio às áreas. | Preparar a organização para incorporar IA ao trabalho. |
| **Data Mesh de Pessoas** | Produtos de dados, incluindo Headcount e Skills, com expansão e validações em andamento nos registros consultados. | Criar informação confiável e reutilizável para decisões e serviços. |
| **Violeta e Tech Product de agentes** | Base de desenvolvimento de agentes por código; proposta de componentes reutilizáveis. No contexto relatado da VPP, falta a camada acessível que conecte essa base à criação e ao uso cotidiano por não especialistas. | Evoluir da disponibilidade técnica para uma experiência integrada de IA. |
| **COMP** | Reconstrução de jornadas a partir de uma base zero, com IA no centro do desenho. Recrutamento interno e offboarding são manifestações concretas desse movimento. | Redefinir a experiência e a lógica do serviço, com abordagem de redesenho comparável à apresentada no caso Nubank. |
| **Jeito de Produtar** | Evolução da conexão entre visão, metas, portfólio, gestão de produto e capacidade. | Fazer o trabalho nascer de resultados estratégicos claros e reduzir a reconstrução de prioridade a cada demanda. |

A COMP representa mais que capacidade adicional de construção. Seu papel é ajudar a conceber como as jornadas deveriam funcionar com IA desde o início, revendo etapas, interações e responsabilidades. A proximidade com o Nubank está nessa abordagem de redesenho; os projetos têm contextos, escopos e estágios próprios. Os avanços de integração relatados não equivalem à conclusão dessa transformação.

No caso do Violeta, há uma distinção importante: uma base para especialistas construírem agentes e uma experiência em que as pessoas conversam, acessam dados e criam recursos são capacidades diferentes. O Violeta pode participar da fundação técnica; o desenho de uma camada integrada para o usuário ainda precisa ser estabelecido no contexto da VPP.

**Base da análise:** registros de projetos e evolução de produtos, SRC-PER-005, KU-PER-036–044, complementados pelos esclarecimentos de escopo e situação atual registrados em SRC-PER-007. Os registros internos de origem foram examinados por meio da síntese disponível. O Tech Product permanece uma proposta nas evidências consultadas.

Esses movimentos oferecem uma base real para a estratégia. A comparação com o iFood ajuda a localizar duas diferenças que precisam ser enfrentadas: como a direção se transforma em trabalho e como a tecnologia se transforma em autonomia.

### 4.3 iFood e Vivo: a diferença começa antes da fila de desenvolvimento

**Modelo operativo** é a forma de distribuir decisões, trabalho e recursos para realizar a estratégia. No recorte analisado, a diferença mais relevante entre iFood e Vivo está na ligação entre planejamento, metas e entrada de trabalho.

No iFood, o relato associa a alocação de produto ao direcionamento estratégico e coloca os PMs na organização das demandas. Na Vivo, áreas diversas podem originar solicitações, e parte do esforço de qualificação e priorização precisa reconstruir o problema, o valor e sua conexão com os objetivos. Nossa leitura é que uma parcela da dificuldade percebida na fila nasce antes dela: na tradução da estratégia em metas e responsabilidades de produto.

| Dimensão | iFood — mecanismo relatado | Vivo — situação descrita | Diferença relevante |
|---|---|---|---|
| **Origem da prioridade** | Direção estratégica e funcional orienta produtos e alocação de PMs. | Há planejamento e fóruns, mas pedidos ainda exigem reconstrução recorrente de valor e alinhamento. | A prioridade precisa chegar mais definida ao produto, apoiada em metas claras. |
| **Quem organiza o trabalho** | PMs consolidam necessidades de diferentes origens, organizam o roadmap e articulam desenvolvimento. | Diferentes áreas apresentam solicitações; qualifying e comitês absorvem parte da organização e da disputa de capacidade. | A tradução de necessidade em trabalho de produto é mais explicitamente concentrada nos PMs no relato do iFood. |
| **Função da qualificação** | As escolhas de produto ocorrem dentro de uma direção e de uma capacidade orientadas pelo planejamento. | A qualificação pode acumular esclarecimento do problema, definição de valor e discussão de prioridade. | Quando a meta não orienta suficientemente a demanda, a entrada precisa compensar essa indefinição. |
| **Experiência de acesso à IA** | Toqan oferece uma camada conversacional conectada aos dados e recursos disponíveis, com possibilidade de criação pelos usuários. | Data Mesh e base de agentes avançam; falta, no contexto relatado da VPP, uma experiência acessível que conecte essas capacidades. | Disponibilizar infraestrutura e disponibilizar autonomia para o usuário são patamares distintos de capacidade. |
| **Papel dos especialistas** | PMs, referências de dados e tecnologia sustentam produtos e a autonomia na ponta. | Parte da demanda ainda exige mediação para qualificar, conectar recursos e viabilizar a solução. | A base compartilhada pode deslocar esforço de atendimento repetido para evolução de produtos, dados e qualidade. |

**A implicação é fortalecer o vínculo entre meta, produto e capacidade.** O Jeito de Produtar pode corrigir parte dessa origem ao tornar explícitos o resultado esperado, o responsável e as escolhas de alocação. Para produzir esse efeito, seus conceitos precisam aparecer no planejamento e nos direitos de decisão sobre a carteira. Acrescentar formulários à entrada, por si só, não resolve a indefinição anterior.

Isso preserva a contribuição de todas as áreas na identificação de necessidades. A responsabilidade de consolidar essas necessidades e convertê-las em evolução de produto passa a ter um papel definido. No relato do iFood, esse trabalho cabe aos PMs, em conexão com a liderança funcional.

O iFood continua fazendo escolhas de prioridade: a executiva menciona o que cabe no roadmap e a alocação seletiva. A diferença observada é onde e com que referência essas escolhas acontecem. As fontes sustentam essa distinção de funcionamento; não fornecem uma medida comparável de velocidade entre as empresas.

**Fontes:** SRC-PER-001, 24:57–27:40, para planejamento e PMs, e 12:49–18:48, para interface e dados; SRC-PER-005, segunda parte, seções 2–6, para fluxo Vivo; SRC-PER-007, para esclarecimentos atuais. A relação entre indefinição de metas e esforço de qualificação é uma interpretação estratégica apoiada nesses relatos, a ser acompanhada na evolução do modelo.

Essa comparação amplia a resposta necessária: a VPP precisa de direção que organize o trabalho e de capacidades comuns que tornem a IA utilizável. Antes de definir essas apostas, cabe explicitar sua contribuição para a Vivo.

'''+s[b:]
a=s.index('## 6.')
s=s[:a]+'''## 6. Visão 2028: a conclusão do percurso

O mercado mostrou que IA conecta aprendizagem, competências, redesenho e organização. Os projetos da Vivo mostram que já existem movimentos nessas direções. A comparação de modelo operativo acrescentou duas condições: objetivos que orientem os produtos e uma experiência que conecte as pessoas às capacidades de IA.

| Aprendizado acumulado | Base ou necessidade na Vivo | Resultado que a visão deve expressar |
|---|---|---|
| O redesenho do trabalho aproxima a tecnologia do resultado; o Nubank torna esse mecanismo concreto. | COMP reconstrói jornadas com IA no centro; a VP pode ampliar essa forma de conceber seus serviços. | **Trabalho mais simples**, com serviços concebidos para resolver necessidades de ponta a ponta. |
| Aprendizagem e competências precisam acompanhar novas formas de trabalhar. | Eu Vivo IA e dados de Skills oferecem bases para desenvolver pessoas e orientar a transformação. | **Pessoas mais preparadas**, capazes de aplicar IA, exercer julgamento e adaptar o trabalho. |
| Direção estratégica, PMs e uma camada acessível de IA conectam intenção e capacidade de agir no iFood. | Jeito de Produtar, Data Mesh e Violeta precisam convergir em direção, responsabilidade e experiência integrada. | **Entregas melhores**, com mais autonomia, coerência e capacidade de evolução. |

> **Em 2028, a VP Pessoas terá integrado IA à forma de preparar a organização e de prestar seus serviços: trabalho mais simples, pessoas capazes de aprender e adaptar sua atuação e entregas melhores, sustentadas por objetivos claros, conhecimento confiável e uma experiência de IA acessível.**

A visão combina os dois papéis de Pessoas: preparar a Vivo para a mudança do trabalho e transformar a própria função. Sua realização exige construir capacidades que sirvam a diferentes serviços e necessidades ao longo do tempo.

**As grandes apostas da VP devem definir essas capacidades e o modo de operá-las. As jornadas serão os lugares em que essa estratégia se materializa.**

## 7. As cinco grandes apostas da VP Pessoas

As apostas abaixo são compromissos estruturais da estratégia. Cada uma responde a um aprendizado do percurso e vale para diferentes jornadas. Juntas, definem onde concentrar investimento, atenção e desenvolvimento organizacional.

### 7.1 Estratégia e metas como origem do trabalho de produto

**Aposta:** organizar o portfólio de Pessoas a partir de resultados estratégicos claros, com responsabilidade de produto e capacidade associada.

A comparação com o iFood mostrou que a direção anterior ao pedido muda o papel da priorização. Para a VPP, o Jeito de Produtar pode estabelecer a ligação entre objetivo, meta, produto e investimento. Os PMs consolidam necessidades e organizam a evolução dos produtos; as áreas contribuem com contexto, especialidade e problemas reais.

O efeito esperado é reduzir a reconstrução recorrente de valor e prioridade na entrada. Isso exige metas que expressem mudança de resultado e orientem escolhas de capacidade. A evolução será percebida quando a carteira puder ser explicada pela estratégia e quando novos pedidos forem analisados dentro dessa direção.

### 7.2 Uma experiência integrada de IA para usar, criar e agir

**Aposta:** oferecer uma camada acessível que conecte conversa, dados, conhecimento e agentes, permitindo às pessoas resolver necessidades e criar recursos dentro de seu campo de atuação.

O Toqan torna visível essa possibilidade. O ponto de partida da pessoa é sua pergunta ou intenção; a solução aciona as capacidades disponíveis por trás. Para a VPP, o objetivo é que a infraestrutura de dados e agentes se converta em autonomia cotidiana, com apoio para quem usa e cria.

Essa aposta orienta uma experiência comum, cuja solução tecnológica deve aproveitar o ecossistema corporativo. O Violeta pode ser parte da base; a experiência de uso, as integrações e a criação acessível são capacidades adicionais a desenvolver ou incorporar. A escolha de plataforma depende dessa avaliação, sem pressupor um fornecedor ou uma construção integral própria.

### 7.3 Conhecimento e dados como patrimônio reutilizável de Pessoas

**Aposta:** organizar dados, definições e conhecimento de Pessoas para que possam ser compreendidos e reutilizados por profissionais, produtos e agentes.

O Data Mesh fornece uma base relevante. Para a experiência integrada funcionar, também é necessário que os dados tenham significado consistente e que políticas, critérios e orientações estejam atualizados, com responsáveis claros. Uma pergunta sobre um indicador precisa levar à mesma definição, independentemente do canal ou do agente utilizado.

O investimento se acumula: cada produto de dados e cada conjunto de conhecimento bem mantido pode servir a mais de uma necessidade. O resultado esperado é menos reconstrução de contexto e maior confiança nas respostas e decisões.

### 7.4 Preparação da organização e evolução das práticas de talento

**Aposta:** conectar aprendizagem, liderança e gestão de talento às mudanças reais no trabalho da Vivo.

BB e Mercado Livre mostram que aprender e reconhecer competência precisam acompanhar a execução. Nubank e iFood ampliam essa discussão para funções, equipes e organização. A contribuição de Pessoas inclui identificar capacidades que mudam, preparar líderes e profissionais e fazer seleção, desenvolvimento, mobilidade e gestão de desempenho acompanharem essas mudanças.

Eu Vivo IA pode sustentar essa evolução ao conectar formação e aplicação, com experiências adequadas a cada contexto. A ambição é ampliar a capacidade da empresa de se adaptar, observando competência aplicada e mudanças na forma de trabalhar.

### 7.5 Reinvenção dos serviços de Pessoas como capacidade permanente

**Aposta:** incorporar o redesenho com IA desde a origem à forma de conceber e evoluir os serviços de Pessoas.

A COMP já expressa esse movimento ao reconstruir jornadas com IA no centro. O caso Nubank reforça a importância de definir a experiência, as decisões e o papel humano antes da solução. A aposta consiste em tornar essa abordagem uma capacidade da VP, com conhecimento que permanece e pode ser reaproveitado além de um projeto ou parceiro.

O resultado esperado é uma função que consegue rever suas próprias regras, interações e responsabilidades conforme as necessidades mudam. Produtos passam a evoluir pela resolução que oferecem; tecnologia, dados e parceiros entram como meios de realizar esse desenho.

### 7.6 Como as apostas se reforçam

**Objetivos orientam o trabalho; pessoas preparadas usam e transformam esse trabalho; uma experiência integrada lhes dá acesso às capacidades; conhecimento confiável sustenta essa experiência; o redesenho converte essas condições em serviços melhores.**

Responsabilidade, qualidade e acompanhamento de valor atravessam as cinco apostas. Uma camada de IA sem dados confiáveis amplia respostas frágeis. Dados disponíveis sem experiência acessível mantêm dependência de especialistas. Formação sem mudança do trabalho limita a aplicação. Produtos sem direção clara reproduzem a disputa por pedidos. A estratégia depende da conexão entre essas escolhas.

## 8. A experiência integrada que queremos construir

A aposta em uma camada acessível merece explicitação porque representa uma diferença de capacidade em relação à base técnica hoje relatada na VPP. O alvo é uma experiência em que a pessoa consiga expressar uma necessidade e mobilizar informação e recursos sem conhecer a estrutura dos sistemas.

### 8.1 Da intenção à resposta ou ação

| Na experiência da pessoa | O que a capacidade compartilhada precisa oferecer |
|---|---|
| Fazer uma pergunta em linguagem comum. | Compreender a intenção e esclarecer ambiguidades. |
| Receber informação coerente com sua necessidade. | Consultar dados e conhecimento com definições consistentes e acesso adequado. |
| Pedir apoio para executar uma atividade. | Acionar ferramentas e agentes conectados, com os limites e confirmações cabíveis. |
| Criar um recurso para sua rotina e compartilhar o que funciona. | Oferecer meios acessíveis de criação, avaliação e manutenção. |
| Entender e conferir o resultado. | Tornar fontes, limitações e responsabilidades reconhecíveis. |

Na experiência pretendida, uma pergunta que dependa de dados de Pessoas pode levar a uma consulta ao produto de dados pertinente, respeitando o acesso do usuário. Ele não precisa escolher manualmente a base ou refazer a conexão a cada pergunta. Essa simplicidade resulta de integrações, definições e permissões construídas e mantidas por trás.

### 8.2 Como Data Mesh e Violeta participam

O Data Mesh organiza produtos de dados; o Violeta oferece uma base para desenvolver agentes; a camada integrada aproxima essas capacidades de quem trabalha. A interface é uma parte dessa experiência: também são necessários entendimento do contexto, acionamento dos recursos e continuidade de operação.

No contexto atual informado da VPP, o Violeta exige desenvolvimento por código e ainda não entrega essa experiência acessível de ponta a ponta. Essa constatação delimita a necessidade a atender; não define uma limitação permanente da tecnologia nem uma avaliação de todo o ecossistema corporativo da Vivo.

**A decisão estratégica é construir a capacidade de acesso e criação integrada.** A avaliação de soluções deve considerar a experiência, a cobertura de integrações, o aproveitamento das bases existentes e o custo de evolução. Esse é o referencial para desenvolver, adquirir ou combinar recursos.

Uma experiência comum amplia a autonomia. Para que ela se converta em valor, a organização também precisa definir quem orienta os produtos e assume sua evolução.

## 9. Um modelo operativo orientado por metas e produtos

A primeira aposta redefine o vínculo entre planejamento e execução. A direção estratégica deve estabelecer resultados e escolhas de investimento; a gestão de produto deve traduzi-los em evolução contínua. Assim, a capacidade compartilhada de IA atende a uma intenção clara e o conhecimento das áreas se converte em produtos coerentes.

### 9.1 Onde cada decisão passa a acontecer

| Nível | Responsabilidade proposta | Efeito no funcionamento |
|---|---|---|
| **Estratégia e metas** | Definir os resultados que a VP precisa produzir e as escolhas de capacidade que os sustentam. | Dar uma referência anterior à chegada dos pedidos. |
| **Gestão de produto** | Consolidar necessidades, organizar evolução e decidir a sequência de trabalho dentro da direção e da capacidade estabelecidas. | Tornar explícito o papel dos PMs na organização da demanda. |
| **Especialidades de Pessoas** | Contribuir com necessidades, critérios, políticas e conhecimento do trabalho. | Preservar profundidade funcional na concepção e avaliação dos produtos. |
| **Capacidades compartilhadas** | Sustentar dados, conhecimento, experiência de IA e condições técnicas de entrega. | Acumular reuso e ampliar autonomia com qualidade. |

A distinção relevante é entre a origem de uma necessidade e a responsabilidade de transformá-la em trabalho de produto. Todas as áreas podem identificar problemas e oportunidades. Os PMs organizam esse conjunto em relação às metas e à capacidade, articulando escolhas com os responsáveis funcionais e técnicos.

O **Jeito de Produtar** pode institucionalizar essa mudança: metas orientam produtos, produtos orientam a carteira e a carteira orienta o uso da capacidade. A qualificação continua necessária para aprofundar incertezas; sua função deixa de acumular, a cada pedido, toda a discussão de direção estratégica.

### 9.2 Autonomia que cresce com responsabilidade

A camada acessível de IA permite distribuir uso e criação. A gestão de produto identifica o que deve se tornar capacidade compartilhada, o que permanece apoio local e o que precisa ser incorporado a um serviço sustentado. Especialistas cuidam das definições, da qualidade e das consequências do uso.

Ownership significa acompanhar o resultado e a evolução do produto ao longo do tempo, articulando as responsabilidades necessárias. Parceiros participam desse modelo com capacidade de redesenho e construção, enquanto a VPP preserva direção, conhecimento e responsabilidade pelos serviços.

### 9.3 A velocidade que esse modelo deve produzir

A hipótese é reduzir o tempo consumido para reconstruir prioridade, transferir contexto e conectar recursos a cada necessidade. Direção clara reduz rediscussão; gestão de produto consolida escolhas; a base compartilhada reduz reconstrução; a experiência acessível amplia a capacidade de ação das pessoas.

A velocidade será avaliada pelo tempo até produzir uma melhora útil, considerando espera, retrabalho e qualidade. O modelo precisa tornar a VPP mais capaz de transformar intenção em resultado e de adaptar seus produtos quando a necessidade muda.

Esse funcionamento traduz as apostas em uma organização capaz de sustentá-las. A evolução deve preservar a conexão entre as cinco, mesmo quando avancem em ritmos diferentes.

## 10. A trajetória estratégica: conectar, incorporar e ampliar

A evolução combina movimentos que se reforçam. O planejamento detalhado virá do desdobramento das apostas, com metas e capacidade explícitas. A sequência abaixo mantém o foco na construção da capacidade da VP.

| Movimento | Mudança estrutural pretendida | Sinal de que a estratégia está avançando |
|---|---|---|
| **Conectar direção e bases existentes** | Ligar metas, produtos, Eu Vivo IA, Data Mesh, Violeta e redesenho de serviços numa mesma direção. | A carteira e os investimentos podem ser explicados pelas cinco apostas e pelos resultados esperados. |
| **Incorporar novas formas de operar** | Fazer gestão de produto, experiência integrada de IA e preparação das pessoas participarem do trabalho cotidiano. | As áreas usam capacidades comuns e organizam evolução com referências claras de resultado. |
| **Ampliar e renovar a capacidade** | Reutilizar conhecimento, dados e recursos; revisar serviços e práticas de talento conforme o trabalho evolui. | O aprendizado de uma transformação fortalece outras e a VP consegue adaptar sua atuação com qualidade. |

As jornadas materializam esses movimentos e permitem observar seus efeitos. A definição de quais avançam em cada momento decorre das metas, da relevância e da capacidade. Isso preserva a ordem da estratégia: primeiro a direção e as grandes apostas; depois seu desdobramento em produtos, jornadas e entregas.

## 11. O valor que a estratégia deve produzir

O acompanhamento precisa demonstrar os resultados da visão e a contribuição das apostas para alcançá-los. Contagem de ferramentas, agentes ou participantes informa atividade; o valor aparece na mudança do trabalho e na capacidade da organização.

| Resultado da visão | Evidência de mudança | Apostas que contribuem diretamente |
|---|---|---|
| **Trabalho mais simples** | Necessidades resolvidas com menos esforço, repetição e passagens dispensáveis, preservando qualidade. | Experiência integrada, conhecimento reutilizável e reinvenção dos serviços. |
| **Pessoas mais preparadas** | Profissionais e líderes aplicam competências, exercem julgamento e adaptam a forma de trabalhar. | Preparação da organização, experiência acessível e dados confiáveis. |
| **Entregas melhores** | Produtos realizam objetivos estratégicos, evoluem com menos espera e mantêm utilidade e qualidade. | Metas como origem do trabalho, gestão de produto e capacidades compartilhadas. |

Os objetivos se desdobram em medidas e metas a partir da situação inicial. A avaliação considera custo total, esforço de revisão e sustentação, além de como a capacidade liberada é aproveitada. Ganhos de tempo não se convertem automaticamente em redução de despesa.

Essa disciplina também permite revisar as apostas: se o acesso cresce sem aplicação, é necessário melhorar experiência e preparação; se a criação cresce sem qualidade, a base de conhecimento e a sustentação precisam evoluir; se a entrega continua fragmentada, a ligação entre metas, produtos e capacidade precisa ser fortalecida.

## 12. A estratégia de IA da VPP que resulta desse percurso

A mudança começou na tarefa e alcançou processos, competências e organização. Os casos mostraram mecanismos para coordenar essa transformação. A Vivo já reúne iniciativas de aprendizagem, dados, agentes, redesenho de serviços e evolução da gestão de produtos. A estratégia conecta essas bases para construir uma capacidade duradoura.

> **Preparar a Vivo para o trabalho com IA e reinventar os serviços de Pessoas, orientando os produtos por metas e ampliando a autonomia por meio de uma experiência integrada, conhecimento confiável e capacidade contínua de transformação.**

| Grande aposta | Compromisso estrutural da VP |
|---|---|
| **Estratégia e metas na origem** | Fazer os objetivos orientarem produtos, escolhas e capacidade. |
| **Experiência integrada de IA** | Conectar uso, dados, agentes e criação numa experiência acessível. |
| **Conhecimento reutilizável** | Manter informação e definições confiáveis que sirvam a diferentes necessidades. |
| **Preparação da organização** | Evoluir competências, liderança e práticas de talento com o trabalho. |
| **Reinvenção permanente dos serviços** | Incorporar IA ao desenho de Pessoas desde a concepção, acumulando aprendizado e capacidade. |

**Trabalho mais simples, pessoas mais preparadas e entregas melhores** são os resultados que essas apostas devem produzir até 2028. A visão sintetiza o percurso; as apostas sustentam sua realização; os produtos e jornadas expressam essa estratégia no trabalho real.

## Fontes e limites de interpretação

A rastreabilidade está no [catálogo de conhecimento](../../evidence/personal/README.md). SRC-PER-001 registra a conversa com uma executiva do iFood; SRC-PER-002, o resumo do HR Think Tank Nubank de agosto de 2026; SRC-PER-005, a síntese dos registros de projetos e gestão de produtos da Vivo; SRC-PER-006, o mapa de pesquisa pública; SRC-PER-007, os esclarecimentos desta revisão.

O estudo dos projetos internos se baseia na síntese disponível e nos esclarecimentos recebidos; não representa reabertura de todos os registros originais. O resumo Nubank é derivado de transcrição e fotos. A data da conversa iFood continua não confirmada. A descrição pública do Toqan foi consultada para confirmar sua identidade e proposta; não substitui a evidência do benchmark sobre a configuração interna do iFood.

A comparação de modelo operativo distingue mecanismos relatados, situação interna informada e recomendação. Não demonstra superioridade mensurada de velocidade entre empresas. A ausência da camada acessível foi informada para o contexto atual da VPP; o potencial papel do Violeta nessa experiência exige avaliação de capacidades e integração.

O [roteiro narrativo](ROTEIRO_NARRATIVO_V2_FORA_PARA_DENTRO.md) acompanha esta versão. Os registros anteriores preservam o histórico e não definem a sequência vigente.
'''
write(P,s)

# Preserve explicit clarifications as a source instead of retroactively editing attachments.
source=R/'sources/personal/outras fontes pessoais/esclarecimentos_estrategicos_vpp_2026-09-06.md'
write(source,'''# Esclarecimentos estratégicos da usuária — 06/09/2026

Registro editorial fiel ao sentido da solicitação, não transcrição literal. Origem: mensagem da usuária nesta conversa.

1. COMP: o projeto é reconstrução de jornadas a partir de uma base zero, com IA no centro; recrutamento interno e offboarding não esgotam sua natureza estratégica. A usuária aproxima a abordagem do caso Nubank.
2. iFood e planejamento: a percepção da usuária é que as prioridades já vêm orientadas pelo planejamento estratégico, enquanto a Vivo destina esforço recorrente a qualificação e priorização; a hipótese é que parte da origem esteja nas metas. Jeito de Produtar é apontado como possível correção, não resultado já comprovado.
3. Organização das demandas: no relato percebido do iFood, PMs organizam e articulam pedidos; na Vivo, diferentes áreas podem apresentar solicitações. A transcrição registra necessidades de múltiplas origens também no iFood e decisões de roadmap pelos PMs; não sustenta ausência de priorização naquela empresa.
4. Experiência de IA: a usuária destaca a camada conversacional do Toqan ligada aos dados e à criação por usuários. Na VPP, relata Violeta como base que exige desenvolvimento por código, sem a camada acessível que integre essas capacidades para não especialistas. Possível evolução do Violeta é hipótese; não houve avaliação técnica de todo o ecossistema Vivo.
5. Direção editorial: após a visão, desenvolver grandes apostas estruturais da VP antes de jornadas. Remover nomes de interlocutores do iFood, identificação da audiência e o nome do anexo no bloco 4.2.

Limites: informação interna e interpretações fornecidas pela usuária; fatos internos não auditados. A grafia Toqan foi conferida na página oficial https://toqan.ai/ em 06/09/2026. Seu produto público e a implantação descrita no benchmark não são tratados como equivalentes em todos os detalhes.
''')
base=R/'evidence/personal'
mp=base/'PERSONAL_MANIFEST.jsonl'; rows=[json.loads(x) for x in read(mp).splitlines() if x]
rows.append(dict(source_id='SRC-PER-007',title='Esclarecimentos estratégicos da usuária — 06/09/2026',file=str(source.relative_to(R)).replace('\\','/'),kind='user_provided_clarifications',published='2026-09-06',cataloged='2026-09-06',reading_status='registro editorial dos esclarecimentos da solicitação',limitations='Relato e interpretação da usuária; não auditoria operacional. Documento não é transcrição literal.'))
write(mp,'\n'.join(json.dumps(x,ensure_ascii=False) for x in rows))
kp=base/'PERSONAL_KNOWLEDGE_BASE.jsonl'; units=[json.loads(x) for x in read(kp).splitlines() if x]
for num,statement,locator,theme in [
 (53,'COMP é esclarecida como reconstrução de jornadas a partir de base zero, com IA no centro; RI e offboarding são aplicações desse movimento.','item 1','work_redesign'),
 (54,'A usuária interpreta a diferença iFood/Vivo como conexão mais anterior de prioridades com planejamento e metas; Jeito de Produtar pode apoiar essa evolução.','itens 2–3','operating_model'),
 (55,'No contexto atual relatado da VPP, Violeta requer código e falta uma camada acessível que integre conversa, dados e agentes; sua evolução é hipótese.','item 4','shared_platform')]:
 units.append(dict(id=f'KU-PER-{num:03}',type='internal_clarification',statement=statement,context='Esclarecimento da usuária, com escopo e limites preservados.',themes=[theme],scope=['hr_function'],org_scope='Vivo',evidence='user_provided_clarification',epistemic_status='relato ou interpretação da usuária',confidence='média',validation_needed=True,sources=[dict(source_id='SRC-PER-007',locator=locator)]))
write(kp,'\n'.join(json.dumps(x,ensure_ascii=False) for x in units))

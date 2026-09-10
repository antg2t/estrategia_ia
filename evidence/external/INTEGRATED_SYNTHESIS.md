# Síntese integrada do corpus — IA em Pessoas e RH

## Adendo — assessment recebido em 05/09/2026

Após a síntese original foi acrescentado `SRC-037`, o arquivo `assessement - IA no RH.xlsx`. A leitura visual das sete capturas disponíveis gerou `GARTNER_AI_MATURITY_ASSESSMENT_TRANSCRICAO.md` e as unidades `KU-122` a `KU-131`.

O assessment cobre AI Strategy, AI Value, AI Organization, AI People and Culture, AI Governance, AI Engineering e AI Data: 25 atividades, cada uma avaliada em maturidade atual, alvo em 12 meses e importância. A oitava aba está vazia; não há respostas preenchidas nem fórmula de resultado agregado. O escopo textual é enterprise, apesar do nome local mencionar RH. A aplicação à VP Pessoas deve explicitar escopo e capacidades compartilhadas.

O catálogo passa a conter 37 fontes lógicas. Os números e a descrição de cobertura nas seções originais abaixo se referem ao acervo anterior, de 36 fontes.

## 1. Status epistemológico

Este documento é uma síntese derivada de 36 documentos lógicos: 30 PDFs, quatro PPTXs locais e dois PPTXs dentro de um ZIP. Descontadas uma duplicidade textual e uma duplicidade de formato, há 34 conteúdos semanticamente distintos. Destes, 33 são fontes externas Gartner ou ferramentas baseadas em pesquisa Gartner; o outro é um deck customizado e não validado.

Não há dados internos confirmados da Vivo neste pacote. Consequentemente, esta síntese descreve **o conhecimento contido no acervo**, e não a situação atual, as prioridades ou a estratégia recomendada para a empresa.

As referências usam `[SRC-###, p. X]` para páginas de PDF e `[SRC-###, s. X]` para slides de PPTX. Unidades atômicas correspondentes estão em `KNOWLEDGE_BASE.jsonl`.

## 2. Tese organizadora do corpus

O acervo converge para dois mandatos diferentes e complementares da liderança de Pessoas:

### Mandato A — AI_TRANSFORMATION_OF_HR

Usar IA para transformar a própria função Pessoas/RH: proposta de valor, serviços, processos, decisões, papéis, estrutura, tecnologia, dados e economics da função. A questão é “como RH passa a operar e criar valor em um ambiente AI-first?”. [SRC-018, p. 1-7] [SRC-026, p. 2-14]

### Mandato B — HR_ENABLES_ENTERPRISE_AI

Usar as competências de Pessoas/RH para habilitar a transformação de IA da empresa: redesenho do trabalho, organização, competências, workforce planning, cultura, adoção, confiança, liderança e processos de talento. A questão é “como a força de trabalho e a organização capturam valor da IA de forma sustentável?”. [SRC-019, p. 1-9] [SRC-030, p. 2-8]

Confundir os mandatos tende a produzir um de dois resultados incompletos: um portfólio de automações de RH sem transformação do negócio ou uma agenda ampla de capacitação da força de trabalho sem reinventar a própria função. A fonte central recomenda que o CHRO trate ambos como prioridades explícitas. [SRC-030, p. 1-4]

## 3. Sinais de contexto presentes no acervo

Os números abaixo são benchmarks ou premissas Gartner, não fatos universais:

- Em dezembro de 2025, 95% dos CHROs pesquisados relatavam uma ou mais iniciativas de IA, mas apenas 36% se diziam preparados ou já incorporando IA ao operating model; apenas 23% dos conselheiros avaliavam que o CHRO integrava IA efetivamente à estratégia de RH. [SRC-001, p. 2]
- Na mesma base de pesquisa, um terço relatava valor nulo ou mínimo, 49% valor moderado e apenas 18% valor significativo ou transformacional. [SRC-030, p. 3]
- As mudanças esperadas para RH nos 12 meses seguintes concentravam-se em augmentação de workflows (54%), seguidas por reengenharia (31%) e criação de serviços inteiramente novos (14%). [SRC-030, p. 3]
- Em 2025, somente um em quatro CHROs dizia ter substituído empregados por IA ou automação no ano anterior; eram mais frequentes redeployment (37%), redesign de equipes (48%) e redefinição de jobs (40%). [SRC-030, p. 2]
- A Gartner apresenta como premissa estratégica que, até 2030, IA poderá executar ou automatizar 50% das atividades atuais de RH e augmentar 100% delas. Essa é uma previsão para planejamento, não uma medição atual. [SRC-001, p. 3] [SRC-026, p. 2]
- O padrão recorrente é alta atividade e valor ainda limitado: implementações isoladas, pouca reengenharia, foundations frágeis, baixa adoção e mensuração incompleta impedem escala e valor transformacional. [SRC-001, p. 2-5] [SRC-011, p. 2-4] [SRC-030, p. 3, 7]

## 4. Arquitetura conceitual integrada

Os documentos podem ser reorganizados em sete capacidades interdependentes:

1. **Direção e alinhamento estratégico** — mandato, ambição, visão, princípios e conexão com estratégia empresarial, de RH, de tecnologia e de IA.
2. **Valor e portfólio** — outcomes, casos de uso, priorização, funding, balanceamento e realização de valor.
3. **Trabalho e operating model** — workflows, tarefas, jobs, equipes, estruturas, value streams, produtos e interação humano-IA.
4. **Pessoas, capacidades e cultura** — literacy, skills, managers, aprendizagem, sentimento, confiança e experimentação.
5. **Governança e risco** — direitos decisórios, políticas, riscos específicos de RH, transparência, terceiros, monitoramento e exceções.
6. **Dados e tecnologia** — dados estruturados e não estruturados, metadados, arquitetura, integrações, runtime, observabilidade e portfólio de fornecedores.
7. **Medição e evolução** — baselines, ROI, experiência, qualidade, prontidão futura, cadências e gatilhos de revisão.

Essas capacidades aparecem como seis workstreams no roadmap Gartner: estratégia; valor; impacto no trabalho; pessoas e cultura; governança; dados e sistemas. O operating model e a mensuração atravessam todos os workstreams. [SRC-027, p. 3-9]

## 5. Direção e alinhamento estratégico

### 5.1 IA como variável de estratégia, não apenas como tecnologia

O corpus sustenta que IA muda simultaneamente:

- o que o negócio precisa de RH;
- como o trabalho da empresa é executado;
- como RH entrega serviços;
- quais produtos e decisões RH passa a oferecer;
- quais riscos e capacidades se tornam materiais.

Por isso, IA deve influenciar visão, objetivos e métricas desde o início do planejamento de RH. Ainda pode existir uma estratégia de IA detalhada para RH, mas ela precisa estar integrada à estratégia funcional e alinhada à estratégia empresarial de IA. [SRC-003, p. 1-7] [SRC-032, s. 2-6, 31-34]

### 5.2 Cinco componentes da estratégia de IA focada em RH

A ferramenta `Develop an HR-Focused AI Strategy` organiza o conteúdo em cinco componentes, que não precisam ser sequenciais: [SRC-032, s. 6-34]

1. **Visão** — papel e prioridade da IA, outcomes aspirados e princípios orientadores.
2. **Valor** — goals, exemplos de casos, métricas e nível de ambição.
3. **Risco** — categorias de risco, avaliação, ações e owners.
4. **Adoção** — fusion team, estágio de adoção, impacto sobre a função e plano de literacy/skills.
5. **Alinhamento** — relação com estratégias empresarial, de IA, de RH e de HR Technology.

Pré-condições: owner dedicado de produto/programa de IA em RH, stakeholders de todas as áreas de RH, IT, jurídico e compliance, acesso às estratégias relevantes e revisão pelo menos anual ou diante de mudanças significativas. A ferramenta recomenda não começar pela escolha de casos de uso antes de esclarecer a direção. [SRC-032, s. 2-4, 35]

### 5.3 Ambição

Ambição define quão agressivamente a função pretende usar IA, considerando outcomes, risco, tecnologia existente, customização e capacidade de mudança. Os materiais usam três posturas ilustrativas para relacionar ambição empresarial e visão de RH: liderar o mercado, ser fast follower ou buscar ganhos incrementais. A visão de RH deveria preparar a função e a workforce ligeiramente à frente da velocidade de transformação pretendida pela empresa. [SRC-003, p. 3-5] [SRC-032, s. 19]

### 5.4 Cinco passos do mandato de transformação de RH

O overview de prioridade CHRO reúne cinco passos: [SRC-001, p. 3-5]

1. Criar e implantar estratégia de RH compatível com a transformação de IA e os objetivos empresariais.
2. Redesenhar operating model e papéis de RH.
3. Identificar casos de IA e tecnologia de alto valor.
4. Analisar o landscape de fornecedores e capacidades existentes.
5. Construir governança que permita medir e evoluir a estratégia.

## 6. Os dois mapas de transformação

### 6.1 Mapa para transformar a função RH

O `HR Strategy on a Page: AI Transformation of HR` organiza a jornada em três fases não necessariamente lineares. [SRC-018, p. 1-8]

**Fase 1 — Estabelecer foundations**

- instalar um HR Innovation Command responsável pela transformação e evolução contínua;
- diagnosticar custo, performance, valor percebido, processos, tecnologia, dados, roles e AI maturity;
- formular ambição e proposta de valor futuras;
- priorizar onde agir primeiro entre HR Operations, HRBPs e COEs, combinando impacto e viabilidade.

**Fase 2 — Adaptar o operating model**

- elevar HR Operations por automação, agentes, experiência digital e agile delivery;
- reposicionar HRBPs como strategic talent leaders e consultores de transformação do trabalho;
- converter COEs de silos de processo para designers/owners de produtos e value streams.

**Fase 3 — Supervisionar a transformação**

- estabelecer governança de IA específica para RH e conectada à governança empresarial;
- operar change management, comunicação e upskilling como atividades contínuas;
- revisar métricas, papéis, processos e estrutura com base em outcomes e novos gatilhos.

### 6.2 Mapa para RH habilitar a transformação empresarial

O `HR Strategy on a Page: Enable Enterprise AI Transformation` define quatro fases também não lineares. [SRC-019, p. 1-9]

**Fase 1 — Foundations empresariais**

- coalizão cross-functional com autoridade sobre prioridades, riscos, treinamento e comunicação;
- princípios human-first e linguagem executiva consistente;
- medidas comuns de valor e thresholds;
- avaliação conjunta de maturidade técnica, readiness de pessoas e cultura.

**Fase 2 — Transformar trabalho e desenho organizacional**

- mapear processos, tarefas, fricções e oportunidades de augmentação, reengenharia ou automação;
- criar mecanismos de employee voice para originar e validar oportunidades;
- revisar jobs, competências, métricas, reporting lines, estruturas e decision rights;
- formar fusion teams e métodos repetíveis de work redesign.

**Fase 3 — Equipar a workforce**

- remover barreiras de adoção, conectar learning ao trabalho e sustentar experimentação;
- segmentar apoio conforme impacto e readiness, evitando programa único para todos;
- preparar managers como multiplicadores da mudança;
- tratar confiança, motivação, identidade profissional e resistência como variáveis de valor.

**Fase 4 — Renovar processos de talento**

- adaptar performance management a outcomes, aprendizagem e trabalho augmentado;
- reconhecer contribuições de IA sem premiar volume de baixa qualidade;
- incorporar hipóteses realistas sobre IA em strategic workforce planning;
- planejar hiring, redeployment, reskilling e riscos de segunda ordem;
- monitorar continuamente skills atrophy, confiança, ética e impactos sobre carreiras.

## 7. Operating model AI-infused

### 7.1 Definição e princípios

Um operating model AI-infused é descrito como um estado em que IA é intencionalmente embutida em toda plataforma, processo e interação em que seu uso seja viável e desejável. O desenho deve permitir parceria humano-máquina, e não apenas adicionar ferramentas aos fluxos existentes. [SRC-022, p. 4-6] [SRC-026, p. 15-16]

Princípios: AI by default, human-first design, customer centricity, inovação contínua e deployment dinâmico. “AI by default” não elimina judgment humano; significa considerar IA sistematicamente e preservar participação humana onde risco, empatia, confiança ou impacto exigirem. [SRC-022, p. 5]

### 7.2 Quatro blocos estruturais

O modelo de referência contém quatro blocos. [SRC-026, p. 4-14] [SRC-022, p. 5, 17-19]

1. **HR Innovation Command** — pequena estrutura estratégica e permanente que define proposta de valor futura, conduz transformação, acompanha tecnologia, orienta work/role redesign e monitora outcomes e sentimento.
2. **Strategic Talent Leader Pod** — evolução do HRBP; agentes atendem demandas rotineiras, especialistas humanos são alocados dinamicamente para problemas estratégicos e relações executivas permanecem high-touch.
3. **Custom HR Product Designers** — evolução dos COEs; organizam trabalho por produtos e value streams, com product owners, experiência, personalização e gestão de portfólio.
4. **Digital HR Solutions & Delivery** — evolução de HR Operations; reúne HR Tech, human capital intelligence, people relations, agile delivery hub/PMO e resolução de problemas, enquanto agentes absorvem Tier 0/1.

O modelo não deve ser copiado literalmente. É uma hipótese de desenho a calibrar conforme tamanho, estratégia, tecnologia, skills, relações trabalhistas, maturidade e opções de shared services/GBS/outsourcing.

### 7.3 Mudanças de papéis

- **HRBP:** perde tarefas de consulta a políticas, drafting e sumarização; cresce em work redesign, strategic workforce planning, reskilling, change, human-machine collaboration, ethics e conflitos complexos. [SRC-026, p. 4-5]
- **HR Operations:** perde administração e respostas padrão; cresce em experiência digital, qualidade, inovação do serviço, analytics, governança, simulação e casos complexos. [SRC-026, p. 6-9]
- **COEs:** perdem execução repetitiva e análise manual; crescem em product management, user experience, personalização, portfólio e value streams horizontais. [SRC-026, p. 10-12]
- **Instructional designer:** o exemplo de L&D mostra migração de criador de curso para orquestrador de aprendizagem, product designer, supervisor de agentes e guardião de qualidade pedagógica. [SRC-015, p. 8-12]

### 7.4 Método geral de work/job redesign

O caso de instructional design fornece um método transferível: [SRC-015, p. 3-13]

1. Identificar sinais de mudança de demanda, tecnologia, volume, personalização, ROI e qualidade.
2. Decompor o job em workflows core, contextuais e compartilhados.
3. Avaliar cada tarefa por regras versus judgment, risco do erro, valor humano e impacto no usuário.
4. Definir nível de autonomia: assistente desconectado, helper embutido, automação de tarefa, colaborador operacional ou ambiente multiagente.
5. Redefinir o valor humano pelas lentes “job to be done”, “quem faz” e “formas de trabalhar”.
6. Classificar competências em humanas fundamentais, duradouras, novas, atrofia aceitável e atrofia arriscada.
7. Atualizar expectativas, sourcing, reskilling e suporte à transição emocional.

O corpus recomenda avaliar tarefas e workflows, não eliminar jobs a partir de rótulos genéricos. O monitoramento deve capturar consequências comportamentais como overreliance, perda de contexto, redução de colaboração, curiosidade, craftsmanship e skills atrophy. [SRC-006, s. 14-20, 24-30]

## 8. AI People Strategy

O `Blueprint for Building Your AI People Strategy` define AI People Strategy como escolhas intencionais que alinham talento, capacidade organizacional e cultura para embutir IA na empresa. Os três componentes são interdependentes. [SRC-007, p. 2-4]

### 8.1 AI-ready workforce

Objetivo: compor o mix de builders, translators e users necessário hoje e no futuro. Alavancas: [SRC-007, p. 6, 10]

- sourcing: quando comprar, desenvolver ou acessar temporariamente talento;
- pipeline: oferta de talentos desde early career até liderança;
- mobilidade: caminhos visíveis para roles augmentados ou novos;
- literacy e enablement baseados no papel e em casos práticos.

### 8.2 Capacidade organizacional

Objetivo: tornar IA uma capacidade repetível. Alavancas: [SRC-007, p. 7, 11]

- governança e decision rights claros, com representação de RH;
- work redesign e operating models que incorporem IA ao fluxo normal;
- process excellence, quality management, modelagem e validação de dados;
- infraestrutura para capturar, compartilhar e reutilizar casos, decisões e lições.

### 8.3 Cultura de confiança e segurança

Objetivo: permitir adoção sem resistência, desengajamento ou risco oculto. Alavancas: [SRC-007, p. 8, 12]

- normas explícitas de colaboração humano-IA, ética, privacidade e accountability;
- managers equipados para liderar equipes augmentadas e sustentar psychological safety;
- medição contínua de confiança, fairness e sentimento;
- experimentação protegida por guardrails, aprendizagem pública e reconhecimento.

## 9. AI literacy, aprendizagem e adoção

### 9.1 Definição

AI literacy é a capacidade de usar IA efetiva e responsavelmente em contexto empresarial e social, entendendo princípios, aplicações, dados, métodos, valor, implicações, riscos e ética. A profundidade necessária varia por papel. [SRC-012, p. 4]

### 9.2 Roadmap em cinco etapas

1. Comunicar a importância e construir buy-in.
2. Conectar learning a outcomes por narrativas “learning to earning”.
3. Identificar personas e suas necessidades de proficiência.
4. Desenhar e entregar aprendizagem ágil e contextual.
5. Medir impacto, iterar, adaptar e expandir. [SRC-012, p. 3-15]

Personas-base: executivos que decidem investimentos, SMEs que participam de design/teste, especialistas que constroem e operam IA e empregados que utilizam as capacidades. O currículo cobre quatro categorias: foundations, value, engineering e governance. A intensidade varia por persona. [SRC-012, p. 8-12]

O padrão recomendado combina aproximadamente 10% aprendizagem formal, 20% social e 70% aplicação/experiência, ajustado ao caso. Microbursts just-in-time, comunidades de prática, coaching, peer learning, experimentos, proofs of concept e hackathons conectam conhecimento a resultado. [SRC-012, p. 13-15]

### 9.3 Práticas de adoção observadas

Os casos mostram padrões convergentes: [SRC-005, s. 4-34] [SRC-008, s. 18-29]

- começar por fricções reais do trabalho, e não por treinamento genérico;
- misturar participantes com diferentes níveis de maturidade;
- usar experimentação em equipe e compartilhamento de soluções;
- reservar tempo explícito para aprendizagem e prática;
- formar champions, digital coaches e comunidades;
- preparar managers para traduzir valor, acolher resistência e co-criar mudanças;
- comunicar impactos operacionais e emocionais, não apenas benefícios tecnológicos;
- medir mudança de comportamento e outcomes, além de conclusão de cursos.

No caso McDermott, a abordagem de aprendizagem baseada no trabalho reportou aumento de maturidade, compreensão de aplicação em workflows e apoio entre pares. São resultados de caso, não benchmarks universais. [SRC-005, s. 14-21]

## 10. Casos de uso e gestão de portfólio

### 10.1 Domínios cobertos

A biblioteca contém exemplos em: [SRC-009, p. 3-34]

- HR Operations: assistentes de políticas, benefícios, total rewards, onboarding e knowledge services;
- Talent Management: succession, engagement action planning, career paths, performance, skills intelligence e workforce planning;
- Recruiting: interview intelligence, scheduling, high-volume apply, sourcing, matching, assessments e voice interviews;
- L&D e mobilidade: adaptive/personalized learning, learning experience platforms, internal talent marketplaces, gigs e mentoring.

O guia dos cinco usos mais implementados em 2026 destaca candidate sourcing, candidate matching, employee/manager self-service agents Tier 0/1, personalized learning e workforce planning. [SRC-021, p. 4-18]

### 10.2 Priorizar processo antes de solução

O `AI Impact-Value Navigator` cruza três dimensões de impacto potencial — transformação do processo, decision intelligence e disponibilidade de use cases — com valor estratégico e performance atual do processo. A priorização deve ser validada contra os problemas reais da função e sua ambição; quick wins sem relação com issues materiais ou uso de IA onde automação simples basta são falsos positivos. [SRC-028, p. 2-5] [SRC-018, p. 4-5]

O workshop de ideação usa três fases: inspiração, geração de ideias e priorização por valor e viabilidade. O output pretendido é um conjunto pequeno de três a cinco casos para aprofundar, não uma lista extensa sem owner. [SRC-031, s. 14-37]

### 10.3 Três tipos de investimento

O framework de portfólio classifica cada caso de uso: [SRC-016, p. 2-9]

- **Within boundaries:** impacto do workflow conhecido, adoção comprovada, vendor maduro e benchmark disponível. Deve ter business case completo, ROI comprometido e plano de escala.
- **Pushing boundaries:** hipótese de valor crível, mas magnitude, comportamento ou efeitos downstream incertos. Deve usar piloto time-boxed, quantificar somente benefícios defensáveis e decidir scale/refine/stop.
- **Breaking boundaries:** valor ou viabilidade muito incertos e dependentes de novas foundations, operating model ou readiness. Deve limitar investimento, medir leading indicators e readiness e definir critérios explícitos de stop/scale, sem prometer ROI prematuro.

O scoring usa escala 1–5 em oito critérios: benchmarkability, data readiness, technology readiness, integration simplicity, adoption readiness, risk profile, vendor maturity e time to impact. Regras indicativas: média igual ou superior a 4 e nenhum score crítico baixo para within; média entre 3 e 4 ou poucos gaps tratáveis para pushing; média abaixo de 3 ou múltiplos gaps críticos para breaking. [SRC-016, p. 6-7]

Arquétipos de portfólio: conservative, balanced, disruptor e FOMO. O mix deve refletir estratégia, risco, maturidade técnica/data e change capacity, com rebalanceamento pelo menos semestral. [SRC-016, p. 8-10]

### 10.4 Exemplos e resultados reportados

Resultados de case studies demonstram possibilidade, não causalidade ou replicabilidade:

- Mercado Libre: assistente conversacional reportou resolução de 95% das perguntas, cerca de 1,4 milhão de consultas e US$ 2,7 milhões de economia. [SRC-009, p. 5]
- Moderna: GPTs especializados cobriram benefícios, equity, self-review e job leveling; a empresa reportou tratamento de 80% das perguntas nos domínios cobertos. [SRC-009, p. 6]
- HSBC: skills intelligence consolidou milhares de skills em pacotes, inferiu parte relevante dos perfis e alimentou workforce planning, learning e marketplace. [SRC-009, p. 12]
- Campbell's: scheduling automatizado reduziu mediana de cinco dias para 32 minutos e elevou conversão do career site. [SRC-009, p. 17]
- GM: assistant de recruiting reportou queda de mais de cinco dias para 29 minutos em scheduling e aproximadamente US$ 2 milhões anuais de economia. [SRC-009, p. 21]
- BT Group: personalized learning integrado a SuccessFactors e Teams elevou alcance e engagement; é um exemplo no setor de telecomunicações. [SRC-009, p. 29]
- Schneider Electric: marketplace interno exigiu também mudanças de políticas, como retirar tempo mínimo no cargo e aprovação prévia do manager. [SRC-009, p. 32]
- Hitachi: agente de onboarding privado reduziu dias de processo e horas de envolvimento de RH, apoiado por conteúdo corporativo e integrações. [SRC-009, p. 34]

O insight transversal é que tecnologia, process redesign, conteúdo/dados, integrações, mudança de políticas, treinamento, human oversight e métricas formam o use case; a ferramenta isolada não é o caso de uso completo.

## 11. Agentes e self-service

### 11.1 Sweet spot de agentes

Agentes são mais adequados a tarefas de complexidade média: o ambiente é dinâmico demais para automação rígida, mas custo e risco do erro permanecem gerenciáveis. [SRC-014, p. 1-5, 11-12]

- **Agente é overkill:** sequência fixa e baixa complexidade; automação tradicional tende a ser mais eficiente.
- **Sweet spot:** onboarding tracking, ausência rotineira, atualização de dados, perguntas complexas multietapas, coaching customizado e análise de entrevistas com supervisão.
- **Ainda não pronto/risco alto:** employee relations sensível, disciplina, decisões finais de hiring/promotion/termination e aconselhamento jurídico/compliance.

Pilotos devem começar com problema e outcome bem definidos, baseline, riscos, usuários e gestores envolvidos, cross-functional fusion team, feedback e decisão explícita de scale/refine/stop. A seleção de tecnologia deve seguir o caso — prebuilt, no-code/low-code ou desenvolvimento — e não a sofisticação disponível. [SRC-014, p. 5-9]

### 11.2 HR Operations

Casos de alta aderência incluem knowledge retrieval, policy guidance, transactional self-service, data changes, case triage, benefícios/payroll enrollment, case summarization, knowledge capture e sentiment detection. Compliance detection, complex case management e leave administration autônoma aparecem como aderência menor ou maior risco. [SRC-002, p. 4-7, 9-13]

Outcomes relacionados: employee experience, eficiência, suporte escalável 24/7, liberação de tempo estratégico e melhor decision intelligence. [SRC-002, p. 12-13]

### 11.3 Evolução multiagente

A trajetória proposta é: multiagentes dentro de uma plataforma; depois colaboração cross-platform mediada por protocolos; eventualmente uma rede ampla de agentes. Os estágios cross-platform e “Internet of Agents” dependem de standards e maturidade que o documento de 2025 ainda considera insuficientes para a maioria das organizações. [SRC-023, p. 4-5]

Seis foundations: competências para configurar e gerir agentes, workflow redesign, experimentação, governança, integrações/APIs e RAG/contexto confiável. [SRC-023, p. 6-7]

### 11.4 Self-service

Self-service eficaz exige quatro condições: [SRC-024, p. 2-9]

1. dados e conteúdo AI-ready;
2. tecnologia ajustada a indústria, segmentos e necessidades dos usuários;
3. mensuração e melhoria contínua;
4. skills e mentalidade de product management em RH.

Dados não estruturados merecem atenção especial: políticas duplicadas, conflitantes ou expiradas geram respostas incorretas. Metadados, owners, datas de vigência e regras de expiração precisam fazer parte do operating process, não apenas de uma limpeza inicial. [SRC-024, p. 4-5]

Métricas de self-service devem cobrir adoção, experiência, outcomes funcionais e qualidade: usage, satisfação, containment, custo por resolução, tentativas por usuário, erro, acurácia e first-contact resolution. Deve haver canal de escalonamento humano. [SRC-024, p. 7-9]

## 12. Dados e tecnologia

### 12.1 Estratégia de HR Technology em quatro fases

1. Definir business outcomes, visão e princípios.
2. Capturar gaps e distinctive requirements usando business capability model, maturity model e persona journey maps.
3. Definir future state combinando requisitos internos e landscape de HCM suite, extensões e point solutions.
4. Criar roadmap de transformação com iniciativas estratégicas, readiness, procurement, implementação, sustainment e decommissioning. [SRC-017, p. 1-9]

A tecnologia não deve ser mapeada somente pela estrutura organizacional atual. Business capabilities fornecem visão independente de people/process/technology; persona journeys capturam necessidades que cruzam silos. [SRC-017, p. 5-7]

### 12.2 Foundations de dados e sistemas para IA

O roadmap de dados contém estas capacidades: [SRC-027, p. 20-23]

- requisitos de dados definidos por use case;
- aprovação, ownership, limpeza, anonimização, padronização e integração;
- catálogo/dicionário de metadados;
- provenance, lineage, versionamento e logs;
- governança de acesso, retenção, privacidade, segurança e qualidade;
- observação de distribuição, bias, drift e labeling accuracy;
- arquitetura, integrations e control boundaries;
- runtime com regras para agir, recomendar, escalar e parar;
- observabilidade, incident management, ownership operacional e rollback;
- separação entre lógica do workflow e ferramenta do fornecedor;
- inventário e gestão do portfólio de features de IA.

O corpus alerta que 60% dos HR Tech leaders pesquisados relatavam governança de dados insuficiente e apenas 14% dos IT leaders se diziam muito confiantes na prontidão de conteúdo e dados para interações humanas e de IA. [SRC-024, p. 1]

### 12.3 Employee experience e tecnologia

O Bullseye Report sugere preferência dos empregados por interfaces agregadas e workflows consolidados, personalized learning, internal mobility, ferramentas assíncronas e listening que resulte em ação. Também registra sinais de baixa confiança em AI-based performance ratings e queda de valor percebido quando pesquisas de momentos importantes não produzem resposta visível. [SRC-020, p. 1-19]

O relatório recomenda avaliar tecnologia pela experiência real de personas, e não apenas pela feature list. Ele é uma fonte de tendência, não um ranking automaticamente transferível.

## 13. Governança e risco

### 13.1 Princípio estrutural

Governança empresarial central é necessária, mas insuficiente para RH. Pessoas envolve dados sensíveis e decisões sobre candidatos, performance, remuneração, mobilidade, disciplina e desligamento; por isso, princípios corporativos devem ser traduzidos em controles e decision rights específicos por use case. [SRC-025, p. 1-6]

O modelo equilibra inovação/agilidade com controle, accountability, compliance e confiança.

### 13.2 Três níveis de maturidade

**Iniciar**

- formar HR AI governance team;
- representar RH no enterprise AI governance council;
- definir mandato, membros, cadence, reporting e feedback bilateral.

**Formalizar**

- traduzir ethics, risk, security e safety para RH;
- classificar riscos e usos aceitáveis;
- definir decision rights, workflows, documentação e escalation;
- incorporar jurídico/regulatório a design, seleção de fornecedor e deployment;
- treinar públicos diferentes.

**Otimizar**

- monitorar sistemas e vendors continuamente;
- auditar bias, fairness, data quality, segurança e comportamento;
- documentar exceções, ações corretivas e escalonamentos;
- manter transparência para empregados e candidatos. [SRC-025, p. 3-9]

### 13.3 Transparência

Transparência inclui explicar quais dados são coletados, como são processados, que decisões a IA apoia, rights de acesso/correção/objeção/apelação, propósito e escopo do uso e canais para dúvidas e denúncias. [SRC-025, p. 9] Esses elementos devem ser validados contra legislação, relações trabalhistas e políticas internas aplicáveis; o corpus não substitui aconselhamento jurídico.

### 13.4 Riscos recorrentes

- bias e discriminação em decisões de talento;
- falta de explainability e contestabilidade;
- privacidade e acesso indevido a employee data;
- conteúdo incorreto, desatualizado ou sem provenance;
- leakage, misuse, hallucination e drift;
- vendor lock-in, agentic washing e features imaturas;
- automação de decisões de alto impacto sem human accountability;
- baixa adoção, confiança ou skill;
- skills atrophy, overreliance e perda de colaboração/contexto;
- ausência de fallback quando a IA falha;
- ROI prometido antes da redução de incerteza.

## 14. Valor, ROI e mensuração

### 14.1 Valor é um sistema, não uma métrica isolada

O pacote de ROI representa valor como soma de quatro elementos: impacto sobre outcomes, readiness, prova quantificada e comunicação consistente. As falhas comuns são partir de fornecedor/feature, manter muitos casos desconectados, prometer ROI cedo, ignorar attribution e baseline, subestimar TCO e adoption e comunicar valor de forma episódica. [SRC-036, s. 4, 11-13]

### 14.2 Nove etapas

1. Definir outcomes empresariais e conectá-los a outcomes de RH.
2. Mapear outcomes de RH para use cases.
3. Priorizar casos e montar readiness plan.
4. Escolher benefícios quantificáveis por tipo de caso.
5. Quantificar benefícios com baseline, attribution e sensibilidade.
6. Estimar TCO completo.
7. Construir modelo de break-even, ROI, NPV e payback.
8. Criar narrativa ligando outcome, capability, caso, fornecedor e métrica.
9. Medir e comunicar valor continuamente. [SRC-036, s. 4, 13-52]

O readiness plan ilustrativo usa pre-wave, Wave 1, Wave 2 e Wave 3; um caso pode ser pilotado numa onda e escalado na seguinte. Custos devem incluir tecnologia, dados, integração, segurança, change, treinamento, operação, manutenção e monitoramento. [SRC-036, s. 26-28, 39-46]

### 14.3 Três famílias de valor do operating model

- **ROI — Return on Investment:** custo, produtividade, automação, velocidade e qualidade operacional.
- **ROE — Return on Employee:** esforço, satisfação, confiança, escalonamento humano, adoção e efetividade do time de RH.
- **ROF — Return on Future:** tempo estratégico, valor percebido pelo business, personalização, inovação, velocidade de produto e decisões orientadas por analytics. [SRC-022, p. 21-24]

Baselines e targets no playbook são ilustrativos. O que deve ser preservado é a estrutura: objetivo, métrica, propósito, baseline, target, frequência, método e fonte.

### 14.4 KPIs em camadas

- **Business outcome:** crescimento, produtividade, custo, agilidade, risk e experiência.
- **HR outcome:** hiring, retention, capability, serviço, workforce flexibility.
- **Operational:** cycle time, cases por FTE, containment, erro, qualidade, cost per transaction.
- **Adoption/experience:** active users, completion, satisfação, confiança, escalations.
- **Readiness:** data quality, integration, governance, literacy, manager capability.
- **Behavioral/byproducts:** skills atrophy, overreliance, colaboração, judgment e well-being.
- **Portfolio:** mix por tipo de investimento, value realized, spend, dependencies e stop/scale decisions.

O caso SACE destaca que tempo economizado não vira valor automaticamente: managers e empregados precisam de targets e orientação sobre como realocar o tempo liberado. Clifford Chance monitora readiness e experiência durante a jornada, não somente o resultado final. Synopsys avalia tarefas/skills e redesenha jobs iterativamente. [SRC-006, s. 4-28]

## 15. Roadmap e mecanismo de evolução

O roadmap completo inclui seis workstreams: [SRC-027, p. 3-23]

1. **AI strategy:** trends, readiness, visão/ambição, documento alinhado e refresh.
2. **AI value:** intake, scoring, roadmap, business case, funding, portfólio, benefits e inovação.
3. **AI impact on work:** experimentação, workflows, human moments, jobs, teams, operating model e novos produtos.
4. **AI people and culture:** sentimento/readiness, literacy, intervenções por papel, comunidades, cultura e reconhecimento.
5. **AI governance:** estrutura, council, decision rights, riscos, regulação, training, transparência, vendors e exceptions.
6. **AI data and systems:** dados, metadados, provenance, governança, arquitetura, runtime, observabilidade e feature portfolio.

Atividades iniciais e avançadas podem ocorrer em paralelo, mas há dependências lógicas: dados antes de automação confiável; baseline antes de claim de valor; decision rights antes de alto risco; workflow mapping antes de agentes; literacy e manager enablement antes de escala; pilot evidence antes de full funding em casos incertos.

O mecanismo deve ser dinâmico. Gatilhos de revisão incluem mudança de business strategy, nova capacidade tecnológica, experimento promissor, fricção crescente, alteração de produto/processo, incidentes, regulação ou mudança de sentimento. [SRC-027, p. 11, 14]

## 16. Cenários futuros presentes no corpus

As visões para 2030 são provocações, não previsões certas: [SRC-029, p. 3-14]

- interfaces de aplicações migram para interfaces centradas em agentes/LLMs;
- modelos de colaboração humano-máquina tornam-se mais específicos à cultura e estratégia de cada empresa;
- competências como ambiguidade, pensamento crítico, criatividade e problem solving ganham prêmio;
- valores e contratos tornam-se mais personalizados;
- ética tecnológica deixa de ser revisão caso a caso e passa a framework incorporado;
- well-being e direitos sobre dados/conhecimento ganham relevância;
- climate risk entra em workforce planning.

O valor desses cenários é pressure-testar escolhas e preparar options, não tratá-los como base única de investimento.

## 17. Padrões convergentes que outra IA deve preservar

1. **IA é transformação de trabalho e modelo, não rollout de IT.** RH e IT compartilham responsabilidade: RH traz outcomes, problemas, process ownership e people risk; IT traz arquitetura, segurança, integração e engineering. [SRC-010, p. 1-4]
2. **Work redesign é a ponte entre tecnologia e valor.** Adicionar IA a workflow ruim tende a automatizar fricção.
3. **Augmentation domina o curto prazo, mas não basta.** A criação de valor maior exige reengenharia, novos produtos e mudanças de papéis.
4. **Use cases formam um portfólio.** Cada caso recebe business case, funding, governança e métricas compatíveis com sua incerteza.
5. **Dados incluem conteúdo e contexto.** Políticas, metadados, vigência, ownership e provenance são tão importantes quanto tabelas estruturadas.
6. **Adoção é parte do produto.** Manager enablement, literacy, employee voice, trust, tempo para experimentar e mudança de incentivos não são atividades periféricas.
7. **Governança deve estar embutida no fluxo.** Avaliação, human oversight, logs, appeals, incidentes e vendors fazem parte do desenho desde o início.
8. **Eficiência precisa de decisão explícita sobre o tempo liberado.** Sem realocação, time saved pode não produzir outcome.
9. **Human-first não equivale a human-only.** Significa atribuir papéis conscientemente, proteger moments that matter e manter accountability.
10. **A transformação é contínua.** Processos, jobs, skills, modelos e portfólio precisam de cadência e triggers de revisão.

## 18. Lacunas que o corpus não resolve

Para qualquer aplicação organizacional, outra IA precisará de fontes adicionais:

- estratégia corporativa e ambição de IA;
- prioridades, outcomes e métricas atuais da VP Pessoas;
- estrutura, headcount, budget, service model e capacidade de mudança;
- portfólio atual de projetos e fornecedores;
- arquitetura, contratos, dados, APIs, knowledge bases e qualidade;
- governança empresarial de IA, segurança, privacidade e procurement;
- baseline de processos, experiência, produtividade, risco e custo;
- segmentos de workforce e employee journeys;
- skills atuais, sentimento, adoção e capacidade de managers;
- legislação brasileira vigente, relações sindicais e políticas internas;
- benchmarks e contrapontos de fontes não Gartner;
- decisões explícitas dos sponsors sobre risco, velocidade, build/buy e valor.

Essas lacunas não devem ser preenchidas por inferência a partir do deck customizado `[SRC-033]`.

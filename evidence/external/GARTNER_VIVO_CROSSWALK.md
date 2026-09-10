# Crosswalk Gartner ↔ Vivo

Este documento cruza os frameworks do corpus Gartner (`INTEGRATED_SYNTHESIS.md`, `KNOWLEDGE_BASE.jsonl`) com as evidências internas catalogadas em `VIVO_KNOWLEDGE_BASE.jsonl`.

**Natureza do documento:** interpretação derivada. Nenhuma linha abaixo é fato validado sobre a Vivo. As relações indicam apenas como uma evidência interna se posiciona diante de um framework externo.

**Tipos de relação usados:** confirma, detalha, tensiona, contradiz, lacuna, não avaliável.

---

## 1. Os dois mandatos

| Mandato Gartner | Evidência interna | Relação | Leitura |
|---|---|---|---|
| `AI_TRANSFORMATION_OF_HR` [SRC-018, p. 1-7] | Ambição de RH AI Native [KU-VIVO-022]; arquitetura Data Mesh + plataforma agêntica + People OS [KU-VIVO-024]; portfólio de casos de RH [KU-VIVO-025] | confirma | O mandato A está explicitamente assumido pela função Pessoas. |
| `HR_ENABLES_ENTERPRISE_AI` [SRC-019, p. 1-9] | MVP de liderança com time híbrido e redefinição de job description [KU-VIVO-027]; Business Sprints de estrutura humano-agente [KU-VIVO-026] | detalha | Existe, mas com massa muito menor que o mandato A. Concentrado em liderança. |
| Recomendação de tratar ambos como prioridades explícitas [SRC-030, p. 1-4] | Narrativa de quatro frentes [KU-VIVO-050] | tensiona | As frentes internas misturam os dois mandatos em uma só narrativa. Não há separação formal de ambição, owner e métrica por mandato. |

**Implicação para o plano:** separar explicitamente os dois mandatos é uma das intervenções de menor custo e maior efeito. Hoje o mandato B aparece como subproduto do mandato A.

---

## 2. Cinco componentes da estratégia de IA para RH [SRC-032, s. 6-34]

| Componente | Cobertura interna | Evidência | Avaliação |
|---|---|---|---|
| **Visão** | Alta | [KU-VIVO-001] [KU-VIVO-022] [KU-VIVO-024] [KU-VIVO-050] | Ambição declarada em nível corporativo e funcional. |
| **Valor** | Baixa | [KU-VIVO-028] [KU-VIVO-059] [KU-VIVO-067] | Há um único baseline com hipótese de ROI. Indicadores existem como recomendação, não como realização. Um projeto estruturante declara ausência de metas de benefício. |
| **Risco** | Alta | [KU-VIVO-007] a [KU-VIVO-012], [KU-VIVO-017] a [KU-VIVO-021] | Ponto mais maduro do corpus interno. Normativo abrangente, incluindo sistemas agênticos. |
| **Adoção** | Média-baixa | [KU-VIVO-003] [KU-VIVO-051] [KU-VIVO-073] [KU-VIVO-074] [KU-VIVO-075] | Existe segmentação de personas e voz do colaborador, mas a única medição de adoção encontrada cobre uma diretoria. |
| **Alinhamento** | Não evidenciado | [KU-VIVO-011] [KU-VIVO-012] [KU-VIVO-052] [KU-VIVO-057] | Não foi localizado documento que conecte estratégia empresarial de IA, estratégia de RH e estratégia de HR Technology em um único mapa. |

**Assimetria central:** governança de risco muito à frente da capacidade de demonstrar valor. É o inverso do padrão de "muita atividade, pouca governança" descrito na literatura, e cria um risco diferente: rigor formal sem tração comprovada.

---

## 3. Padrão "alta atividade, valor limitado" [SRC-001, p. 2-5] [SRC-030, p. 3, 7]

O corpus Gartner descreve implementações isoladas, pouca reengenharia, foundations frágeis, baixa adoção e mensuração incompleta.

| Sinal Gartner | Evidência interna | Relação |
|---|---|---|
| Implementações isoladas | 53 iniciativas em nove esteiras, apenas 4 na esteira de IA [KU-VIVO-043] [KU-VIVO-044] | confirma |
| Foundations frágeis | Fim de suporte da folha em 2027, integrações frágeis, qualidade de dados [KU-VIVO-063]; fragmentação e usabilidade em Skills [KU-VIVO-046] | confirma |
| Mensuração incompleta | Ausência de metas de benefício [KU-VIVO-067]; indicadores apenas recomendados [KU-VIVO-059]; Copilot medido por autorrelato [KU-VIVO-062] | confirma |
| Baixa adoção | Pedido por acesso, capacitação aplicada e governança [KU-VIVO-075] | confirma |
| Pouca reengenharia | Predomínio de casos de augmentação; redesenho estrutural limitado ao MVP de liderança [KU-VIVO-027] | confirma |
| Capacidade de entrega | Índice de cobertura da esteira de IA em 0,3, classificado internamente como alto risco [KU-VIVO-045] | **detalha e agrava** |

**Achado mais relevante do cruzamento:** [KU-VIVO-045] é uma métrica interna de capacidade que a literatura externa não fornece. Ela quantifica a distância entre ambição declarada [KU-VIVO-001] e capacidade de execução. É o dado mais acionável do corpus interno.

---

## 4. Quatro blocos do operating model AI-infused [SRC-026, p. 4-14]

| Bloco Gartner | Equivalente interno | Relação | Observação |
|---|---|---|---|
| **HR Innovation Command** | Não localizado como estrutura formal | lacuna | Funções dispersas entre VP Pessoas, HR Tech e Diretoria de IA da VPTI [KU-VIVO-011] [KU-VIVO-054]. |
| **Strategic Talent Leader Pod** | Consultoria Interna [KU-VIVO-053] | detalha | Existe o bloco funcional, mas não há evidência de alocação dinâmica nem de agentes absorvendo demanda rotineira. |
| **Custom HR Product Designers** | COEs [KU-VIVO-053]; camada de Produto e Core [KU-VIVO-057]; Skills como capacidade transversal [KU-VIVO-047] | confirma | A orientação a produto e value stream aparece de forma explícita. |
| **Digital HR Solutions & Delivery** | Experiência do Colaborador [KU-VIVO-053]; Tecnologia, Dados e IA [KU-VIVO-054] | confirma | Corresponde ao deck customizado já presente no corpus principal, que deve continuar tratado como material não validado. |

**Tensão de desenho:** existem três modelos organizacionais coexistindo sem mapa de integração — o TOM corporativo de dados [KU-VIVO-013] [KU-VIVO-015], o modelo operativo da VP Pessoas de 2025 [KU-VIVO-052] e a proposta de HR Tech em três camadas de 2026 [KU-VIVO-057]. Não foi localizado documento que os reconcilie.

---

## 5. Classificação do portfólio [SRC-016, p. 2-9]

Aplicação dos três tipos de investimento às iniciativas internas identificadas.

| Iniciativa | Evidência | Classificação sugerida | Justificativa |
|---|---|---|---|
| Copilot para desenvolvimento | [KU-VIVO-061] [KU-VIVO-062] | **within boundaries** | Vendor maduro e benchmark disponível. Falta apenas medição defensável em vez de autorrelato. |
| ALIADA (análise de RFPs) | [KU-VIVO-028] | **within boundaries** | É o único caso com baseline explícito. Deveria ter business case completo e ROI comprometido. |
| Modernização da folha | [KU-VIVO-063] [KU-VIVO-066] | **within boundaries** com risco de foundations | Prazo regulatório de suporte torna a execução obrigatória, não opcional. |
| Data Mesh Vivo Skills | [KU-VIVO-038] [KU-VIVO-041] [KU-VIVO-048] [KU-VIVO-049] | **pushing boundaries** | Construção técnica avançada, mas adoção, precisão e decisão corporativa pendentes. |
| Offboarding com IA | [KU-VIVO-033] [KU-VIVO-072] | **pushing boundaries** | Valor plausível, porém alto risco por envolver decisões sobre pessoas [KU-VIVO-010] [KU-VIVO-019]. |
| Aprendizagem adaptativa | [KU-VIVO-035] | **pushing boundaries** | Depende de base de contexto ainda inexistente. |
| People OS / plataforma agêntica | [KU-VIVO-024] | **breaking boundaries** | Depende de foundations, operating model e readiness que ainda não existem. Não deve receber promessa de ROI. |
| Redesenho humano-agente de liderança | [KU-VIVO-026] [KU-VIVO-027] | **breaking boundaries** | Alto valor potencial, viabilidade incerta. Medir leading indicators, não retorno financeiro. |

**Uso dos oito critérios de scoring** [SRC-016, p. 6-7]: aplicáveis com os dados disponíveis apenas parcialmente. `data readiness`, `adoption readiness` e `benchmarkability` são justamente as dimensões com mais lacunas internas [KU-VIVO-005] [KU-VIVO-046] [KU-VIVO-067].

---

## 6. AI People Strategy [SRC-007, p. 2-12]

| Componente | Evidência interna | Relação |
|---|---|---|
| **AI-ready workforce** (builders, translators, users) | Segmentação no-code / low-code / pro-code [KU-VIVO-003]; papéis formalizados de IA na VPTI [KU-VIVO-069]; base de skills [KU-VIVO-038] | confirma | 
| **Capacidade organizacional** | Intake formal [KU-VIVO-029] [KU-VIVO-030] [KU-VIVO-031]; MLOps proposto [KU-VIVO-016]; squads transversais [KU-VIVO-055] | detalha |
| **Cultura de confiança e segurança** | Princípios normativos [KU-VIVO-009]; demanda por uso consciente e não compulsório [KU-VIVO-075]; baixa maturidade de gestão de mudança [KU-VIVO-065] | tensiona |

A segmentação por profundidade técnica [KU-VIVO-003] é o equivalente interno mais próximo do mix builders/translators/users. Não há evidência de que essa segmentação esteja conectada a um plano de literacy por persona.

---

## 7. AI literacy [SRC-012, p. 3-15]

| Etapa do roadmap | Evidência interna | Relação |
|---|---|---|
| Comunicar importância e buy-in | Narrativa de quatro frentes [KU-VIVO-050]; capacitação de 100% de diretores e gerentes seniores [KU-VIVO-023] | confirma |
| Conectar learning a outcomes | Não localizado | lacuna |
| Identificar personas | Segmentação técnica [KU-VIVO-003] | detalha parcialmente |
| Aprendizagem ágil e contextual | Visão de motor adaptativo e nudges [KU-VIVO-035]; pedido por capacitação aplicada, fóruns e prompts [KU-VIVO-075] | detalha |
| Medir impacto e iterar | Indicadores de volume, horas e NPS [KU-VIVO-034] | **tensiona** |

**Ponto crítico:** os indicadores de aprendizagem são de participação e satisfação, exatamente o padrão que a literatura recomenda superar em favor de mudança de comportamento e outcomes. A proporção de 95% assíncrono [KU-VIVO-034] também tensiona o padrão 10/20/70, que depende de aplicação e aprendizagem social.

---

## 8. Governança e risco [SRC-032, s. 6-34]

| Exigência | Evidência interna | Relação |
|---|---|---|
| Governança de IA específica de RH conectada à empresarial | Intake e stage gates de HR Tech [KU-VIVO-029] a [KU-VIVO-032]; quatro níveis de governança [KU-VIVO-060] | confirma |
| Representação de RH na governança corporativa de IA | Lista de funções do modelo corporativo [KU-VIVO-012] | **lacuna** |
| Supervisão humana em decisões de alto risco | Restrição normativa explícita [KU-VIVO-010] [KU-VIVO-019] | confirma e supera |
| Controles executados, não apenas exigidos | Nenhuma evidência de inventário preenchido, auditoria realizada ou teste de viés | lacuna |

A governança normativa interna é mais detalhada que o nível tipicamente descrito nos materiais externos. A lacuna não é de norma, é de **evidência de execução da norma**.

---

## 9. Contradições e pontos a validar antes de qualquer decisão

| Tema | Tensão | Referência |
|---|---|---|
| Skills | Base analítica operacional versus plataforma integrada suspensa | [KU-VIVO-049] |
| Ambição versus capacidade | Estratégia de escala corporativa versus cobertura 0,3 na esteira de IA | [KU-VIVO-001] × [KU-VIVO-045] |
| Valor | Benefícios declarados sem metas definidas | [KU-VIVO-023] × [KU-VIVO-067] |
| Operating model | Três desenhos organizacionais sem mapa de integração | [KU-VIVO-013] × [KU-VIVO-052] × [KU-VIVO-057] |
| Benchmark | Percentuais de mercado sem fonte primária | [KU-VIVO-006] |
| Governança | Norma abrangente sem evidência de execução | [KU-VIVO-018] × ausência de auditoria localizada |

---

## 10. Onde o corpus interno é mais forte que o externo

1. **Baseline operacional real.** ALIADA [KU-VIVO-028] e ciclo da folha [KU-VIVO-064] fornecem números de partida que a literatura externa não pode dar.
2. **Métrica de capacidade de entrega.** O índice de cobertura [KU-VIVO-045] é um instrumento interno que permite calibrar ambição com realismo.
3. **Governança normativa detalhada.** Definição de sistema agêntico [KU-VIVO-008] e restrição de decisão automatizada [KU-VIVO-010] antecipam questões que a agenda de agentes vai enfrentar.
4. **Voz do colaborador.** [KU-VIVO-075] traz demanda concreta por uso consciente e não compulsório, tema tratado externamente apenas de forma genérica.

## 11. Onde o corpus interno é mais fraco

1. Ausência de mensuração de valor realizado em toda a cadeia.
2. Ausência de evidência fora de Pessoas e Tecnologia — nada sobre rede, campo, lojas, atendimento ou vendas.
3. Ausência de telemetria de uso e de inventário operacional de agentes.
4. Ausência de mapa de alinhamento entre as estratégias empresarial, funcional e de tecnologia.
5. Ausência de método repetível de work redesign, presente apenas como intenção.

---

## 12. Perguntas prioritárias para a próxima rodada

1. Existe um inventário operacional de soluções e agentes de IA, com owner, status e risco classificado?
2. Qual é a telemetria real de uso das ferramentas licenciadas, por área e por perfil?
3. Que auditorias, relatórios de impacto e testes de viés foram efetivamente executados?
4. Qual é a relação formal entre o TOM corporativo de dados, o modelo operativo da VP Pessoas e a proposta de HR Tech?
5. A função Pessoas tem assento formal na governança corporativa de IA?
6. Qual foi o resultado pós-produção das duas iniciativas de IA em encerramento na esteira de HR Tech?
7. A base de Skills está sendo usada em decisões reais de alocação, sucessão ou recrutamento?
8. Existe evidência de IA aplicada às operações de linha de frente da empresa?
9. Qual é o custo total das iniciativas de IA e existe prática de FinOps aplicada?
10. Qual é o método usado quando um workflow é redesenhado, e ele é repetível?

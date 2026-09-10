# Camada de contexto interno — Vivo

## Status epistemológico

Esta camada é **separada e subordinada** ao corpus Gartner. Ela não valida, não substitui e não corrige o corpus principal. Ela registra o que foi encontrado no ambiente Microsoft 365 acessível durante a curadoria de 5 de setembro de 2026.

Diferença essencial em relação ao corpus principal:

- O corpus Gartner contém **evidência externa e frameworks**.
- Esta camada contém **evidência interna, planos, normas e indicadores**, com qualidade e rastreabilidade variáveis.

Os identificadores usam os prefixos `SRC-VIVO-###` e `KU-VIVO-###` para nunca colidir com `SRC-###` e `KU-###` do corpus principal.

## Arquivos

1. `VIVO_MANIFEST.jsonl` — 20 fontes internas, com escopo, status de leitura e limitações.
2. `VIVO_KNOWLEDGE_BASE.jsonl` — 75 unidades de conhecimento, com status epistemológico, confiança e necessidade de validação.
3. `GARTNER_VIVO_CROSSWALK.md` — cruzamento interpretativo entre os frameworks Gartner e as evidências internas.

## Campos adicionais em relação ao esquema principal

- `org_scope`: Vivo, Vivo e controladas, área específica, projeto específico ou mercado.
- `epistemic_status`: fato documentado, evidência parcial, benchmark, benchmark não rastreável, interpretação, hipótese, recomendação ou lacuna.
- `confidence`: alta, média ou baixa.
- `applicability`: diretamente aplicável à Vivo, potencialmente aplicável ou apenas referência.
- `validation_needed`: booleano. Quando verdadeiro, a unidade não sustenta decisão sozinha.

## Hierarquia de confiança desta camada

1. Normas e políticas formais — `SRC-VIVO-002`, `SRC-VIVO-006`.
2. Indicadores com data e escopo definidos — `SRC-VIVO-011`, `SRC-VIVO-012`.
3. Definições de processo — `SRC-VIVO-010`.
4. Modelos operativos e propostas — `SRC-VIVO-003`, `SRC-VIVO-015`, `SRC-VIVO-016`.
5. Decks estratégicos e narrativas — `SRC-VIVO-001`, `SRC-VIVO-009`, `SRC-VIVO-014`.
6. Relatos autorreportados — `SRC-VIVO-018`.
7. Números externos sem fonte primária — `KU-VIVO-006`, que **não deve ser usado**.

## Síntese

### Escopo e limitações
20 fontes internas cobrindo estratégia, governança, tecnologia, operating model, Pessoas/RH, skills, Copilot e transformação. Uma fonte não foi lida (`SRC-VIVO-007`). Duas duplicidades: `SRC-VIVO-001`/`SRC-VIVO-005` e `SRC-VIVO-016`/`SRC-VIVO-017`.

### Ambição e direção
Ambição documentada de Data & AI First com plataforma unificada, produtização e escala [KU-VIVO-001]. Na função Pessoas, ambição de RH AI Native com arquitetura de Data Mesh, plataforma agêntica e People OS [KU-VIVO-022] [KU-VIVO-024].

### Governança
É o ponto mais maduro. Regulamento cobre IA tradicional, GenAI e sistemas agênticos [KU-VIVO-007], com princípios formalizados [KU-VIVO-009], restrição a decisões automatizadas de alto risco [KU-VIVO-010] e diretrizes de proteção de dados aplicáveis a fornecedores [KU-VIVO-017] [KU-VIVO-020]. Não há evidência de execução dos controles.

### Capacidades e foundations
Plataforma agêntica, Data Mesh, MLOps proposto, controles de segurança, novos papéis de IA e intake formal [KU-VIVO-002] [KU-VIVO-016] [KU-VIVO-029]. A VPTI formalizou papéis de Cientista, Governança e Arquitetura de IA [KU-VIVO-069] e separou papel de cargo [KU-VIVO-070].

### Operating model
Três desenhos coexistem sem mapa de integração: TOM corporativo de dados [KU-VIVO-013] [KU-VIVO-015], modelo operativo da VP Pessoas [KU-VIVO-052] [KU-VIVO-053] e proposta de HR Tech em três camadas [KU-VIVO-057] [KU-VIVO-060].

### Transformação do trabalho
Evidência mais direta: MVP de liderança com time híbrido, redefinição de job description e agente [KU-VIVO-027]. Business Sprints planejados para estrutura humano-agente [KU-VIVO-026]. Squads transversais por skills [KU-VIVO-055].

### Skills, aprendizagem e adoção
Base de skills com volumetria relevante [KU-VIVO-038] e agente analítico [KU-VIVO-039] [KU-VIVO-040], mas a plataforma integrada foi suspensa [KU-VIVO-048], gerando tensão [KU-VIVO-049]. Aprendizagem com escala operacional medida por participação e NPS [KU-VIVO-034]. Pesquisa de adoção restrita a uma diretoria [KU-VIVO-073] [KU-VIVO-074], com demanda por acesso, governança e capacitação aplicada [KU-VIVO-075].

### Valor
Lacuna estrutural. Único baseline com hipótese de ROI é ALIADA [KU-VIVO-028]. Indicadores de HR Tech são recomendados, não realizados [KU-VIVO-059]. Projeto de folha declara ausência de metas de benefício [KU-VIVO-067]. Copilot medido por autorrelato [KU-VIVO-062].

### Risco central
Descompasso entre ambição de escala [KU-VIVO-001] e capacidade de entrega, quantificado pelo índice de cobertura de 0,3 na esteira de IA [KU-VIVO-045], somado à obrigação de modernizar a folha até dezembro de 2027 [KU-VIVO-063], que compete pela mesma capacidade.

## Relatório de qualidade

- Fontes inventariadas: 20
- Fontes com conteúdo examinado: 19
- Fonte não lida: 1 (`SRC-VIVO-007`)
- Unidades de conhecimento: 75
- Unidades com `validation_needed: true`: 55
- Unidade de baixa confiança e uso vedado: `KU-VIVO-006`
- Contradição explícita registrada: `KU-VIVO-049`
- Duplicidades: `SRC-VIVO-001`/`SRC-VIVO-005`, `SRC-VIVO-016`/`SRC-VIVO-017`

### Lacunas prioritárias
1. Inventário operacional de soluções e agentes de IA.
2. Telemetria de uso e adoção por área.
3. Evidência de execução de auditorias, relatórios de impacto e testes de viés.
4. ROI realizado e resultados pós-produção.
5. Mapa de alinhamento entre estratégia empresarial, funcional e de tecnologia.
6. Evidências fora de Pessoas e Tecnologia, especialmente rede, campo, lojas, atendimento e vendas.
7. Método repetível de work redesign.
8. Prática de FinOps aplicada a IA.

## Regras de uso

1. Não converter `planning_assumption`, `recommendation` ou `hipótese` em fato implementado.
2. Não converter POC ou MVP em solução escalada.
3. Preservar data, população e escopo de cada métrica.
4. Não usar `KU-VIVO-006` como benchmark.
5. Validar unidades com `validation_needed: true` antes de qualquer decisão estratégica.
6. Manter o conteúdo dentro do ambiente autorizado; não exportar nomes, contatos ou dados individualizados.
7. Ao citar em produtos posteriores, usar `[KU-VIVO-###]` e `[SRC-VIVO-###]`, mantendo a distinção visual em relação às citações Gartner.

"""One-time editorial revision, September 7, 2026."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'outputs/segunda-feira'
p = OUT / 'ESTRATEGIA_IA_VP_PESSOAS_V2_FORA_PARA_DENTRO.md'
s = p.read_text(encoding='utf-8')
for a,b in [('grandes apostas','big bets'),('Grandes apostas','Big bets'),('cinco apostas','cinco big bets'),('Cinco apostas','Cinco big bets'),('As apostas','As big bets'),('as apostas','as big bets'),('das apostas','das big bets'),('dessas apostas','dessas big bets'),('Aposta:','Big bet:'),('Grande aposta','Big bet')]: s=s.replace(a,b)
s=s.replace('Revisão de 06/09/2026','Revisão de 07/09/2026')
s=s.replace('**Mudança no trabalho → aprendizados do mercado', '**Mudança no trabalho → referenciais Gartner → aprendizados do mercado')
block='''### 1.7 Gartner: como estruturar a transformação

A pesquisa Gartner oferece os referenciais para interpretar a transformação; os casos de empresas mostram práticas em contextos específicos; a realidade da Vivo orienta nossas escolhas. Essa combinação fundamenta a proposta, sem pressupor que as empresas seguiram a Gartner ou que a Gartner avaliou esta estratégia.

| Referencial Gartner | O que orienta na leitura do mercado |
|---|---|
| **Dois mandatos para Pessoas.** Transformar a própria função com IA e preparar a organização para a transformação empresarial. | Observar como a transformação dos serviços de Pessoas se conecta a competências, liderança e organização do trabalho. [SRC-018, pp. 1–7; SRC-019, pp. 1–9; SRC-030, pp. 1–4] |
| **O valor depende do trabalho completo.** Rever processos, decisões e papéis e acompanhar como a capacidade liberada é utilizada. | Distinguir acesso à tecnologia, mudança na execução e resultado efetivo. [SRC-026, pp. 4–14; SRC-006, slides 4–28] |
| **Transformação exige capacidade contínua.** Conectar direção, produtos, dados, adoção, governança e mensuração. | Investigar como as empresas sustentam a mudança além de cada iniciativa. [SRC-032, slides 2–6 e 31–35; SRC-027, pp. 3–23] |

**Esses referenciais oferecem uma lente para interpretar o mercado.** Os casos seguintes dão concretude a partes dessa transformação: aprendizagem aplicada, redesenho de processos, gestão de produtos e capacidades compartilhadas. A convergência ajuda a fundamentar escolhas; não comprova um modelo único ou resultados transferíveis à Vivo.

Fontes e localizadores: [síntese do acervo Gartner](../../evidence/external/INTEGRATED_SYNTHESIS.md) e [catálogo das pesquisas](../../evidence/external/CORPUS_MANIFEST.jsonl). As formulações acima são paráfrases da base catalogada.

'''
s=s.replace('## 2. O mercado',block+'## 2. O mercado',1)
s=s.replace('## 4. A Vivo já tem uma direção sobre a qual construir','Os casos tornam visíveis mecanismos coerentes com os referenciais Gartner, em configurações diferentes. Para a Vivo, importa identificar quais respondem às nossas necessidades e como desenvolvê-los a partir das bases existentes.\n\n## 4. A Vivo já tem uma direção sobre a qual construir')
s=s.replace('## 5. Duas responsabilidades para Pessoas\n','## 5. Duas responsabilidades para Pessoas\n\nA distinção Gartner entre transformar RH e habilitar a transformação empresarial fundamenta estas duas responsabilidades. Sua aplicação à Vivo é uma proposta deste material. [SRC-018, pp. 1–7; SRC-019, pp. 1–9]\n')
start=s.index('A visão combina os dois papéis')
end=s.index('### 7.1',start)
s=s[:start]+'''A visão combina os dois papéis de Pessoas: preparar a Vivo para a mudança do trabalho e transformar a própria função. Os três resultados definem o destino da estratégia:

| Resultado até 2028 | Mudança que queremos produzir |
|---|---|
| **Trabalho mais simples** | Resolver necessidades com menos esforço, etapas, espera e retrabalho, preservando a qualidade. |
| **Pessoas mais preparadas** | Profissionais e líderes capazes de aplicar IA, exercer julgamento e adaptar sua forma de trabalhar. |
| **Entregas melhores** | Produtos e serviços de Pessoas que realizam prioridades estratégicas e evoluem com qualidade e continuidade. |

**Os três resultados são o que queremos alcançar. As cinco big bets são os meios para alcançá-los.** As big bets atuam em conjunto: cada uma constrói uma condição necessária e reforça a contribuição das demais aos resultados.

## 7. Cinco big bets para alcançar os três resultados

As big bets definem onde concentrar investimento, atenção e desenvolvimento organizacional. Traduzem os referenciais Gartner, os aprendizados do mercado e as necessidades da Vivo em cinco compromissos estruturais. Sua formulação é uma escolha desta proposta.

| Big bet — meio estratégico | Como contribui para alcançar os resultados |
|---|---|
| **01 · Estratégia e metas na origem** | Direciona produtos e capacidade para as mudanças pretendidas no trabalho, na preparação das pessoas e nas entregas. |
| **02 · Experiência integrada de IA** | Torna o apoio de IA acessível no cotidiano, permitindo aplicar capacidades e resolver necessidades com menos esforço. |
| **03 · Conhecimento reutilizável** | Sustenta respostas, ações e decisões consistentes, reduzindo retrabalho e preservando conhecimento entre produtos. |
| **04 · Preparação da organização** | Desenvolve competências, liderança e práticas de talento para aplicar IA com julgamento e transformar o trabalho. |
| **05 · Reinvenção dos serviços** | Converte tecnologia, conhecimento e competências em processos mais simples e serviços que atendem melhor às prioridades. |

**Cinco meios que se reforçam → três resultados compartilhados.** A relação é coletiva: não há uma divisão das big bets em grupos exclusivos por resultado. Produtos e jornadas materializam esses meios; o acompanhamento verifica sua contribuição aos três resultados.

''' + s[end:]
s=s.replace('Responsabilidade, qualidade e acompanhamento de valor atravessam as cinco apostas.', 'Responsabilidade, qualidade e acompanhamento de valor atravessam as cinco big bets.')
s=s.replace('## 8. A experiência', '''A execução das cinco big bets exige responsáveis pelo uso e pela continuidade, critérios de qualidade, limites de autonomia, participação humana conforme o impacto e mecanismos para corrigir falhas. Esses controles integram os fóruns e processos competentes. [SRC-025, pp. 3–9]

Considerar IA desde a concepção significa avaliar seu papel no redesenho. Cada etapa pode ser simplificada, automatizada por regras ou apoiada por IA conforme necessidade, viabilidade e risco. [SRC-014, pp. 1–5; SRC-028, pp. 2–5]

## 8. A experiência''',1)
s=s.replace('O acompanhamento precisa demonstrar os resultados da visão e a contribuição das big bets para alcançá-los.', 'O acompanhamento verifica se os cinco meios estratégicos estão produzindo os três resultados da visão. Implantar uma big bet é avanço de execução; seu valor precisa aparecer no trabalho, na preparação das pessoas e nas entregas.')
s=s.replace('| Resultado da visão | Evidência de mudança | Apostas que contribuem diretamente |','| Resultado da visão | Evidência de mudança | Contribuição conjunta das big bets |')
s=s.replace('| Experiência integrada, conhecimento reutilizável e reinvenção dos serviços. |','| As cinco big bets combinam direção, acesso, conhecimento, competência e redesenho para reduzir esforço com qualidade. |').replace('| Preparação da organização, experiência acessível e dados confiáveis. |','| As cinco big bets criam condições para aprender, aplicar, revisar e adaptar o trabalho a objetivos claros. |').replace('| Metas como origem do trabalho, gestão de produto e capacidades compartilhadas. |','| As cinco big bets conectam prioridades à execução, com pessoas preparadas e serviços sustentáveis. |')
s=s.replace('## 12. A estratégia', 'Iniciativas com resultados e viabilidade conhecidos exigem justificativa econômica e acompanhamento do retorno. Iniciativas incertas avançam por testes delimitados, com critérios para ampliar, corrigir ou encerrar. O compromisso de investimento acompanha a evidência disponível. [SRC-016, pp. 2–9; SRC-036, slides 26–28 e 39–46]\n\n## 12. A estratégia',1)
s=s.replace('## Fontes e limites de interpretação','''### 12.1 Mapa executivo da estratégia

**Fundamentos:** Gartner — referenciais de transformação; mercado — mecanismos e experiências; Vivo — direção, bases e necessidades.

**Mandato de Pessoas:** preparar a organização e reinventar os próprios serviços.

**Meios — cinco big bets:** 01 Estratégia e metas na origem · 02 Experiência integrada de IA · 03 Conhecimento reutilizável · 04 Preparação da organização · 05 Reinvenção dos serviços.

**Resultados — visão 2028:** trabalho mais simples · pessoas mais preparadas · entregas melhores.

**Os fundamentos orientam as escolhas. As cinco big bets, executadas em conjunto, são os meios para alcançar os três resultados.** O slide final apresenta essa conexão em um mapa executivo.

## Fontes e limites de interpretação

**Gartner:** a [síntese integrada](../../evidence/external/INTEGRATED_SYNTHESIS.md) e o [manifesto](../../evidence/external/CORPUS_MANIFEST.jsonl) registram os referenciais, títulos e localizadores. SRC-018 e 019 fundamentam os dois mandatos; SRC-026, o redesenho do modelo operativo; SRC-032 e 027, direção e capacidades de execução; SRC-024, dados e conteúdo no serviço; SRC-007, talento, organização e cultura; SRC-025, governança; SRC-016, investimento conforme incerteza; SRC-006 e 036, mensuração e valor. As cinco big bets, a arquitetura de quatro camadas e a visão 2028 são propostas para a Vivo, não prescrições ou endosso Gartner.
''',1)
p.write_text(s,encoding='utf-8')

# Keep presentation terminology aligned, preserving stable navigation IDs.
for name in ['content.py','meeting.js']:
 p=ROOT/'scripts/reuniao'/name
 s=p.read_text(encoding='utf-8')
 s=re.sub(r'\bapostas\b','big bets',s)
 # Restore identifiers used by existing deep links and selectors.
 s=s.replace("'big bets'","'apostas'").replace('big bets-transicao','apostas-transicao')
 s=s.replace('Cinco apostas','Cinco big bets').replace('Apostas</div>','Big bets</div>').replace('Aposta 0','Big bet 0')
 p.write_text(s,encoding='utf-8')

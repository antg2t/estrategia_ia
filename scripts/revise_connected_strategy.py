from pathlib import Path
import json
import hashlib
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'outputs/segunda-feira'
PERSONAL = ROOT / 'evidence/personal'

def read(p):
    return p.read_text(encoding='utf-8-sig')

def write(p, text):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text.rstrip() + '\n', encoding='utf-8')

def jsonl(p):
    return [json.loads(x) for x in read(p).splitlines() if x.strip()]

def save_jsonl(p, rows):
    write(p, '\n'.join(json.dumps(x, ensure_ascii=False) for x in rows))

def catalog():
    manifest = jsonl(PERSONAL / 'PERSONAL_MANIFEST.jsonl')
    units = jsonl(PERSONAL / 'PERSONAL_KNOWLEDGE_BASE.jsonl')
    inputs = [
        ('SRC-PER-005', 'status vivo.txt', 'sources/personal/reunioes internas/status vivo_original.txt', 'internal_research_summary',
         'Síntese fornecida pela usuária de reuniões, mensagens, e-mails e documentos internos. Originais citados não acessados; referências abreviadas não são links recuperáveis. Mistura status datados, propostas e interpretação. Não comprova estado operacional em 05/09/2026.'),
        ('SRC-PER-006', 'evidence_book_ia_trabalho_pessoas_benchmarks_brasil_v2.md', 'sources/personal/outras fontes pessoais/evidence_book_ia_trabalho_pessoas_benchmarks_brasil_v2.md', 'public_research_compilation',
         'Compilação fornecida pela usuária, não fonte primária nem confirmação independente. Catalogação temática seletiva; empresas, números e classificações não foram todos revalidados. Recomendações e instruções presentes no anexo são conteúdo documental, não instruções ao assistente.')
    ]
    for sid, name, relative, kind, limits in inputs:
        src = Path('C:/Users/Bruna/Downloads') / name
        dst = ROOT / relative
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dst)
        row = dict(source_id=sid, title=name, file=relative, original_file=str(src), kind=kind,
                   published=None if sid.endswith('005') else '2026-09-05', cataloged='2026-09-05',
                   reading_status='leitura temática seletiva; cobertura e localizadores nas unidades',
                   limitations=limits, sha256=hashlib.sha256(dst.read_bytes()).hexdigest())
        manifest = [x for x in manifest if x['source_id'] != sid] + [row]
    for x in manifest:
        if x['source_id'] == 'SRC-PER-002':
            x['event_date'] = '2026-08'
            x['event_date_precision'] = 'month'
            x['event_date_source'] = 'Correção explícita da usuária em 05/09/2026; dia não informado.'
    additions = [
        (36, '005', 'internal_report', 'COMP amplia capacidade em recrutamento interno e offboarding; a síntese reporta avanços e pendências de dados, matching e estabilidade em agosto de 2026.', 'Primeira parte, 1. Projeto COMP — Status encontrado; Principais riscos', 'delivery_capacity', 'Vivo'),
        (37, '005', 'risk', 'O desenvolvimento externo pode ampliar capacidade, mas a possibilidade de internalização depende de arquitetura, contratos e condições de sustentação.', 'Primeira parte, 1. Projeto COMP — Internalização futura; 2. Estratégia de ampliar capacidade com desenvolvimento terceirizado', 'operating_model', 'Vivo'),
        (38, '005', 'internal_report', 'A síntese relata piloto Headcount lançado em junho e base Skills operacional em julho, com validações e expansão de escopo ainda em andamento.', 'Primeira parte, 3. Data Mesh — O que já foi entregue; Expansão de escopo', 'data_readiness', 'Vivo'),
        (39, '005', 'risk', 'O relato de Data Mesh registra dependência de especialista, pressão do backlog, necessidade de adoção e de reporte recorrente.', 'Primeira parte, 3. Data Mesh — Sua posição explícita; Riscos e lacunas', 'continuity', 'Vivo'),
        (40, '005', 'internal_report', 'O Tech Product de agentes baseado em Violeta aparece como proposta de fundação reutilizável; há encaminhamento para roadmap e dificuldades de instalação e autenticação.', 'Primeira parte, 4. Violeta — O que é; Status; Dificuldades práticas', 'shared_platform', 'Vivo'),
        (41, '005', 'internal_report', 'Eu Vivo IA é descrito como formação e mobilização de liderança, com pedidos de apoio consultivo e aprendizagem adaptada às áreas.', 'Primeira parte, 5. Eu Vivo IA', 'adoption', 'Vivo'),
        (42, '005', 'internal_report', 'Jeito de Produtar conecta estratégia, capacidade e produtos; seus materiais distinguem carteira obrigatória e discricionária e decisões ao longo do ciclo de vida.', 'Segunda parte, 1. O treinamento “Jeito de Produtar” — Conteúdo central já disseminado', 'portfolio', 'Vivo'),
        (43, '005', 'internal_report', 'O fluxo descrito contém cadastro, qualifying, backlog, comitê, iniciação, desenvolvimento e sustentação; o modelo em evolução separa estratégia, produto/core e execução.', 'Segunda parte, 2. Como nasce uma demanda hoje; 3. Como a demanda é priorizada hoje; 6. Diagnóstico do AS IS versus o modelo desejado', 'operating_model', 'Vivo'),
        (44, '005', 'risk', 'A síntese identifica demanda pouco clara, qualifying oneroso, fragmentação da priorização e fragilidade de indicadores e acompanhamento após entrega.', 'Segunda parte, 5. Como as metas deveriam ser definidas; 6. Diagnóstico — Principais fragilidades registradas', 'value_measurement', 'Vivo'),
        (45, '006', 'research_map', 'O Evidence Book reúne benchmarks de estratégia, dados, trabalho, pessoas e modelo operativo, distinguindo declarações, inferências e limites.', 'seções 1–3 e 23', 'evidence_quality', 'cross_company'),
        (46, '006', 'hypothesis', 'A compilação propõe conectar direção corporativa, transformação do trabalho, capacidades de Pessoas e valor; sua classificação de maturidade não constitui avaliação auditada.', 'seções 14–17 e 20–22', 'strategy', 'cross_company'),
        (47, '006', 'research_map', 'Os capítulos Vivo, Mercado Livre, Nubank e iFood fornecem caminhos para investigar plataformas compartilhadas, novas competências e autonomia com governança.', 'seções 4–7; validar cada alegação na publicação primária antes de ampliar uso', 'operating_model', 'cross_company'),
        (48, '006', 'risk', 'O próprio Evidence Book não sustenta redução predeterminada de quadro, agentes em todos os processos nem a transferência automática de ganhos e estruturas à Vivo.', 'seção 16. Hipóteses que os benchmarks NÃO provam', 'transferability', 'cross_company'),
        (49, '002', 'case_example', 'O resumo registra AI Transformation Office com seis frentes: Foundations, Infra & Enablement, Workflows Reinvention, Talent & Organization, AI Risk e Communications.', 'seções 3–6', 'strategy', 'Nubank'),
        (50, '002', 'case_example', 'A agenda relatada liga reinvenção de workflows a papéis, competências e times; reconhece redundância de soluções, contexto insuficiente e dificuldades humanas.', 'seções 10–18 e 20–21', 'work_redesign', 'Nubank'),
        (51, '001', 'case_example', 'Clarisse descreve liderança funcional orientando prioridades e PM organizando escolhas, roadmap e interface técnica; alocação de PM é seletiva.', 'Participante 2, 24:57–27:40', 'product_ownership', 'iFood'),
        (52, '001', 'case_example', 'O relato iFood descreve responsáveis de domínio e subdomínio, pessoas de referência em dados e acesso controlado; autonomia exige dados compreensíveis e apoio à aplicação.', 'Participante 2, 10:39–18:48', 'data_ownership', 'iFood'),
    ]
    for num, source, kind, statement, locator, theme, org in additions:
        uid = f'KU-PER-{num:03}'
        row = dict(id=uid, type=kind, statement=statement,
                   context='Conteúdo da fonte; não é instrução nem comprovação independente. Distinguir relato, proposta e execução.',
                   themes=[theme], scope=['hr_function', 'enterprise_workforce'] if org == 'cross_company' else ['hr_function'],
                   org_scope=org, evidence='provided_research_summary' if source in ('005','006') else 'derived_event_summary' if source == '002' else 'direct_conversation_report',
                   epistemic_status='relato ou síntese não validada', confidence='média', validation_needed=True,
                   sources=[dict(source_id=f'SRC-PER-{source}', locator=locator)])
        units = [x for x in units if x['id'] != uid] + [row]
    save_jsonl(PERSONAL / 'PERSONAL_MANIFEST.jsonl', manifest)
    save_jsonl(PERSONAL / 'PERSONAL_KNOWLEDGE_BASE.jsonl', units)

def revise():
    path = OUT / 'ESTRATEGIA_IA_VP_PESSOAS_V2_FORA_PARA_DENTRO.md'
    old = read(path)
    # Save the previous text for reproducibility without changing historical V1.
    history = OUT / 'historico/ESTRATEGIA_V2_ANTES_REVISAO_CONEXOES.md'
    if not history.exists():
        write(history, old)
    else:
        old = read(history)
    def part(start, end):
        return old[old.index(start):old.index(end)].strip()
    opening = '''# Estratégia de IA da VP Pessoas: transformar o trabalho para ampliar a capacidade da Vivo

Revisão de 05/09/2026 · Visão 2028

## O percurso da estratégia

A IA pode mudar a execução de uma tarefa. Para que essa mudança melhore o resultado da empresa, é preciso conectar o trabalho de quem executa, as decisões de quem lidera e os recursos de quem constrói e mantém as soluções. Essa conexão orienta a estratégia de IA da VP Pessoas.

O argumento avança da mudança no trabalho para as experiências do mercado; dessas experiências para as condições da Vivo; e dessas condições para o papel de Pessoas e a visão de 2028. As escolhas, o modelo operativo e a execução desdobram essa visão. O texto se dirige inicialmente à diretora e ao CHRO, com os conceitos explicados no próprio percurso.

**Mudança no trabalho → aprendizados do mercado → realidade da Vivo → contribuição de Pessoas → visão 2028 → escolhas e modelo operativo → execução e resultado.**

Os relatos de empresas descrevem práticas em contextos específicos. A comparação e o desenho para a Vivo são análise e recomendação deste material. As fontes aparecem junto às evidências; seu detalhamento está no catálogo do projeto.

## 1. A mudança começa na tarefa e alcança a organização

### 1.1 O ponto de partida: o que muda quando parte da execução recebe apoio de IA?

Considere uma conversa de desenvolvimento. Antes dela, o gestor recupera entregas, reúne registros, organiza informações e prepara os pontos que discutirá com a pessoa. Uma IA pode apoiar essa preparação. O benefício mais imediato é reduzir o esforço para produzir uma primeira síntese.

Mas a finalidade desse trabalho é orientar o desenvolvimento. A síntese só contribui se trouxer informação útil, for interpretada com contexto e levar a uma conversa e a ações melhores. Esse exemplo, ilustrativo, acompanhará o raciocínio: ele permite observar como uma mudança aparentemente individual pode exigir outras mudanças ao redor.

**Para entender o alcance dessa ajuda, precisamos separar a parte que a IA executa do resultado que queremos produzir.**

### 1.2 Da tarefa ao processo: o resultado depende do caminho completo

| Nível | No exemplo da conversa de desenvolvimento | O que precisa funcionar |
|---|---|---|
| Tarefa | Reunir e resumir registros. | A informação deve estar correta e ser relevante. |
| Processo | Preparar, revisar, conversar e acompanhar os acordos. | As etapas devem se conectar e chegar a uma ação útil. |
| Resultado | A pessoa recebe orientação e melhora sua atuação. | A mudança precisa aparecer no desenvolvimento e na entrega. |

Se a preparação fica mais rápida, mas o gestor continua sem reconhecer dificuldades ou combinar próximos passos, o benefício se limita a uma etapa. Se o tempo disponível melhora a conversa e o acompanhamento, há uma hipótese de valor mais ampla.

Isso traz uma escolha: **até onde o trabalho precisa mudar para que a ajuda chegue ao resultado?**

### 1.3 A profundidade da mudança acompanha o problema

No mesmo exemplo, há três possibilidades. Elas servem para comparar alternativas; não são uma sequência obrigatória de maturidade.

| Possibilidade | Como apareceria no exemplo | Quando considerar |
|---|---|---|
| Apoiar uma atividade | Preparar uma síntese que o gestor revisa. | O processo atende à necessidade, mas uma tarefa consome esforço excessivo. |
| Redesenhar o processo | Rever registros, etapas de preparação e acompanhamento. | A dificuldade está nas passagens, regras ou decisões do ciclo. |
| Criar uma capacidade | Oferecer apoio ao desenvolvimento ao longo do trabalho, com contexto atualizado. | A necessidade exige uma continuidade que o serviço atual não consegue oferecer. |

Escolher a alternativa mais ampla exige compreender seus custos e dependências. Uma primeira síntese pode precisar de pouca integração; um acompanhamento contínuo exige dados atualizados, responsabilidades e manutenção. A profundidade deve ser justificada pela necessidade atendida.

**Quanto mais o apoio atravessa o processo, mais precisamos observar o esforço do conjunto.**

### 1.4 Do ganho individual ao ganho coletivo: onde o benefício pode se perder

Imagine que a síntese esteja pronta, mas faltem registros de outra área, a revisão gere retrabalho ou o acompanhamento espere uma decisão que ninguém assumiu. A produção acelerou; a resolução pode continuar demorada.

Para avaliar a mudança, é necessário acompanhar o esforço de preparação e revisão, o tempo de espera e a qualidade da orientação recebida. Também é preciso identificar como a capacidade liberada foi usada. Esses elementos distinguem três coisas: **uso da ferramenta, melhoria do trabalho e resultado para o beneficiário**.

O obstáculo pode estar em uma informação incompleta ou em uma decisão pendente. Por isso, a próxima questão é humana e organizacional: **quem tem condição e responsabilidade para fazer o benefício chegar ao final?**

### 1.5 Do processo aos papéis: competências e responsabilidades também mudam

O gestor passa a precisar conferir evidências, reconhecer lacunas e interpretar contexto. O especialista de Pessoas precisa explicitar os critérios de uma boa orientação. Quem cuida dos dados precisa garantir definições e atualização. Quem responde pelo processo precisa rever etapas e acompanhar seu efeito.

| Papel | Contribuição no exemplo |
|---|---|
| Gestor | Verificar a síntese, acrescentar contexto e conduzir a conversa. |
| Especialista de Pessoas | Definir critérios de qualidade e apoiar o desenvolvimento. |
| Responsável pelo processo | Decidir mudanças nas etapas e acompanhar o resultado completo. |
| Tecnologia e dados | Viabilizar informação, integração e funcionamento da solução. |
| Liderança da área | Dar condições de aprendizagem e orientar o uso da capacidade disponível. |

É assim que IA passa a alcançar competências, liderança e organização do trabalho. A responsabilidade pelo resultado precisa acompanhar o processo, mesmo quando sua execução envolve várias áreas.

### 1.6 A consequência: a estratégia precisa conectar aprendizagem, trabalho e entrega

O exemplo construiu uma cadeia: apoiar uma tarefa exige informação de qualidade; melhorar o resultado pode exigir rever o processo; mudar o processo afeta competências e decisões; sustentar a mudança exige coordenação entre áreas.

Uma estratégia de IA de Pessoas precisa, portanto, responder a três perguntas conectadas: **como preparar quem trabalha, o que redesenhar no trabalho e como organizar a entrega e sua continuidade?**

Com essas perguntas, podemos ler o mercado em uma sequência. Começaremos pela aprendizagem, avançaremos para as competências e o redesenho do trabalho e chegaremos à organização que sustenta a mudança.
'''
    bb = part('### 2.1 Banco', '### 2.3 Nubank')
    bb = bb.replace('**Passagem:** a mudança chega às práticas de Pessoas. O próximo caso mostra isso em um processo que todos conhecemos: avaliação de desempenho.', '**Passagem:** formação e seleção começam a acompanhar o trabalho que muda. Para que essas práticas avancem juntas, a transformação precisa de uma direção comum. O Nubank ajuda a entender como essa agenda é estruturada e como chega a um processo de Pessoas.')
    cases = '''
## 2. O mercado mostra como conectar essas mudanças

Cada caso aprofunda uma pergunta deixada pelo anterior: como aprender, que competência desenvolver, como transformar processos e como manter capacidade de entrega.

''' + bb + '''

### 2.3 Nubank: uma estratégia de transformação que chega ao trabalho e à organização

No HR Think Tank de **agosto de 2026**, realizado na sede do Nubank, Suzana Kubric apresentou, como CHRO, uma agenda mais ampla que a aplicação de IA em RH. O resumo do evento registra a transformação com IA como prioridade corporativa e descreve um AI Transformation Office, estrutura de coordenação organizada em seis frentes.

| Frente apresentada | Problema que procura resolver |
|---|---|
| Foundations | Criar condições mínimas de acesso e regras para transformar. |
| Infra & Enablement | Disponibilizar plataforma, engenharia e padrões reutilizáveis. |
| Workflows Reinvention | Redesenhar fluxos completos de trabalho. |
| Talent & Organization | Ajustar competências, incentivos, papéis e estruturas ao trabalho que muda. |
| AI Risk | Integrar riscos e controles ao desenvolvimento e ao uso. |
| Communications | Construir entendimento, confiança e participação. |

A lógica conecta as frentes: acesso e aprendizagem permitem experimentar; plataforma e contexto tornam a experimentação aproveitável; o redesenho dos processos revela mudanças necessárias em competências e papéis; risco e comunicação acompanham a transformação. O relato também descreve comunidades de aprendizagem e seleção de workflows para acompanhamento mais estruturado.

O ponto relevante da fala da CHRO é o encadeamento entre **fluxo de trabalho, tarefas, funções, equipes e organização**. Uma tarefa redistribuída pode mudar o que um profissional precisa saber; várias mudanças podem exigir outra combinação de papéis na equipe. Essa é uma direção em experimentação no caso apresentado, sem um desenho organizacional final comprovado.

O resumo registra dificuldades com dados fragmentados, falta de contexto, soluções redundantes e qualidade. A velocidade de construção pode superar a capacidade de revisão. Isso ajuda a explicar por que infraestrutura, talento e risco aparecem na mesma estratégia.

**O que aprendemos:** a transformação requer coordenação entre frentes que se afetam. Para Pessoas, isso significa participar do desenho do trabalho e de suas consequências sobre competências e organização, ao mesmo tempo que transforma os próprios serviços.

**Fonte:** [resumo do HR Think Tank Nubank](../../sources/personal/outras%20fontes%20pessoais/HR_Think_Tank_Nubank_Resumo_Completo.md), seções 3–21; SRC-PER-002, KU-PER-012–017 e 049–050. Mês e ano informados pela usuária; dia não informado. O acervo disponível é um resumo derivado de transcrição e fotos; esses originais não foram reexaminados.

Uma comunicação pública distinta, de 11/06/2026, articula a estratégia do Nubank em dados, talento e cultura e informa acesso à IA acompanhado de medição de uso e impacto. Ela complementa o contexto corporativo; a descrição do Transformation Office vem do evento. [Nubank, estratégia de transformação com IA](https://international.nubank.com.br/pt-br/companhia/nubank-detalha-estrategia-de-transformacao-com-ia-baseada-em-dados-modelos-fundacionais-e-aconselhamento-financeiro-democratizado/).

**A estratégia ganha concretude quando essas frentes se encontram em um processo. O caso de performance mostra esse encontro.**

### 2.4 Nubank: performance como aplicação da estratégia

O processo de avaliação descrito no evento exigia esforço para reunir registros, escrever avaliações e realizar calibrações — reuniões para comparar e ajustar avaliações entre equipes. Antes de construir uma solução, o Nubank reuniu 12 executivos em uma oficina de quatro dias para discutir princípios, escolhas e a experiência desejada.

Esse desenho reuniu liderança e capacidades de Produto, Design e Engenharia que, segundo o resumo, já participavam da transformação de People & Culture. As decisões sobre o processo orientaram a construção.

No piloto, a IA apoiava a reunião de evidências e a preparação da avaliação; o gestor revisava, corrigia e acrescentava contexto. O relato reconhece erros, especialmente quando faltava informação ou havia julgamento subjetivo, e descreve experimentação com acompanhamento e processos em paralelo.

Voltamos à conversa de desenvolvimento do capítulo 1. O apoio à preparação só encontra seu propósito quando o gestor usa informações melhores para interpretar e orientar. O caso torna concreta a ligação entre **redesenho, competência do gestor e responsabilidade pela decisão**.

**O que aprendemos:** o responsável pelo processo precisa definir como o trabalho deve funcionar junto de quem conhece sua execução e de quem viabiliza a solução. A liderança entra como coautora do desenho. O piloto oferece aprendizado sobre o método e seus limites, sem estabelecer uma meta de ganho para a Vivo.

**Fonte:** mesmo resumo Nubank, seções 20–29, 40–46, 52–64 e 72–74; SRC-PER-002, KU-PER-017–018.

**Uma mudança desenhada e testada ainda precisa de capacidade para evoluir. O iFood permite aprofundar essa responsabilidade.**

### 2.5 iFood: autonomia para experimentar e responsabilidade para transformar em produto

Na conversa com Clarisse Monteiro, People aparece participando da transformação empresarial por cultura, redesenho da força de trabalho e desenvolvimento de competências. O relato descreve atuação multidisciplinar, envolvendo parceiros de negócio de Pessoas, cultura e tecnologia de RH. A frente de produto ajuda a selecionar o que pode ganhar escala.

Clarisse diferencia contribuições dentro dessa entrega. A liderança funcional orienta as prioridades do tema; o **PM, profissional de gestão de produto**, organiza escolhas, sequência de evolução e interface com tecnologia. Essa capacidade é alocada seletivamente a produtos e também pode acompanhar experimentos. Há uma responsabilidade que continua além do pedido inicial.

Na camada de dados, o relato descreve responsáveis por domínio e subdomínio e pessoas de referência nas áreas, preparadas para trabalhar com os dados. A autonomia depende de definições compreensíveis, regras de acesso e apoio. A interlocutora também relata baixa adesão a algumas soluções e dificuldade dos usuários em formular perguntas: disponibilizar a interface não assegura aplicação útil.

Essa liberdade tem custo. Soluções próprias exigem manutenção, e a expansão da criação por usuários aumenta a demanda por revisão. Clarisse relata que desenvolvimento de software migrou de RH para tecnologia corporativa por questões de retenção e conexão com padrões técnicos, mantendo capacidade alocada aos produtos de Pessoas e apoio externo em algumas frentes.

| Mecanismo relatado | O que ajuda a entender |
|---|---|
| Liderança funcional e PM com papéis distintos | Prioridade do negócio precisa se transformar em escolhas de produto. |
| Responsáveis pelos dados e referências nas áreas | Autonomia exige conhecimento e responsabilidade distribuídos. |
| Experimentos que podem entrar em produtos estruturados | Descoberta local precisa de caminho para continuidade. |
| Desenvolvimento conectado a padrões corporativos | Capacidade técnica e sustentação precisam acompanhar a entrega. |
| Revisão do que construir ou adquirir | A manutenção acumulada influencia a próxima escolha. |

**O que aprendemos:** ownership significa responder pelo resultado ao longo do ciclo de vida. Nossa inferência é que clareza de papéis, capacidade alocada e recursos reutilizáveis podem reduzir espera e retrabalho. A conversa não mede o tempo de entrega nem demonstra que o iFood seja mais rápido que a Vivo.

**Fonte:** [benchmark iFood — Clarisse Monteiro](../../sources/personal/outras%20fontes%20pessoais/Bench%20Ifood%20IA%20Clarisse%20Monteiro_original.txt), falas da Participante 2 em 05:32–09:59, 10:39–18:48, 24:57–27:40 e 31:44–38:47; SRC-PER-001, KU-PER-001–010 e 051–052. Data da conversa não confirmada. As falas do Participante 1 sobre a Vivo são contexto interno, separado do benchmark.

**O percurso chegou à sua terceira pergunta: preparar pessoas e redesenhar processos exige uma forma de entregar e sustentar as mudanças. Podemos agora reunir os aprendizados antes de olhar a Vivo.**

## 3. O que os casos permitem concluir

| Etapa do raciocínio | Evidência apresentada | Critério que levamos para a Vivo |
|---|---|---|
| Aprender a aplicar | Banco do Brasil: formação prática por contexto de trabalho. | Aprendizagem deve desenvolver execução e julgamento em situações reais. |
| Atualizar competências | Mercado Livre: seleção observa trabalho com IA. | Critérios de desenvolvimento e talento precisam acompanhar as atividades que mudam. |
| Coordenar a transformação | Nubank: seis frentes conectam infraestrutura, workflows, talento, risco e comunicação. | A estratégia deve ligar capacidades técnicas e decisões organizacionais. |
| Redesenhar com responsabilidade | Nubank: liderança participa do desenho de performance e gestor revisa o apoio da IA. | Definir o processo e o papel humano antes de ampliar a solução. |
| Sustentar a entrega | iFood: gestão de produto, responsáveis pelos dados, capacidade técnica e manutenção. | O resultado precisa de um responsável que acompanhe sua evolução. |

A síntese é uma cadeia: **aprendizagem permite aplicar; aplicação revela mudanças no trabalho; essas mudanças afetam papéis e decisões; sua continuidade depende de uma organização capaz de entregar e aprender.**

Esses critérios ajudam a formular a estratégia. Sua aplicação depende das prioridades e capacidades da Vivo: não determinam um organograma, uma primeira jornada ou uma meta de produtividade. O próximo passo é reconhecer onde a empresa já está avançando e onde essas conexões precisam ser fortalecidas.
'''
    vivo_intro = part('## 4. A Vivo', '### 4.2 O que')
    vivo = vivo_intro + '''

### 4.2 A VP já está construindo partes dessa resposta

O anexo **Status Vivo** reúne registros internos sobre iniciativas e sobre a evolução da gestão de produtos. É uma síntese fornecida pela usuária, com referências abreviadas a documentos, reuniões e mensagens. Usamos os status com suas datas e distinguimos entregas relatadas de propostas; os registros originais citados não foram acessados nesta revisão.

| Frente | Situação descrita no anexo | Conexão com o que aprendemos |
|---|---|---|
| **Eu Vivo IA** | Formação e mobilização de líderes, com pedidos de apoio consultivo e aplicação por área. | Há uma base de aprendizagem a conectar à mudança efetiva do trabalho. |
| **Data Mesh de Pessoas** | Piloto Headcount lançado em junho; base Skills descrita como operacional em julho, com testes e expansão em andamento. | Dados podem ser reutilizados em diferentes necessidades; adoção, qualidade e continuidade exigem acompanhamento. |
| **Violeta e Tech Product de agentes** | SDK corporativo disponível no contexto relatado; fundação reutilizável proposta, encaminhada para análise de roadmap, com dificuldades práticas de implementação. | Disponibilidade de tecnologia precisa se transformar em capacidade utilizável e apoiada. |
| **COMP** | Construção de recrutamento interno e offboarding; registros de agosto apontam avanços em integrações e pendências de matching, dados e estabilidade. | Parceiros ampliam capacidade, mas dependem de integração, critérios de qualidade e sustentação. |
| **Jeito de Produtar** | Formação e materiais orientam visão, portfólio, governança e indicadores; há uma evolução proposta em estratégia, produto/core e execução. | A própria VP está desenvolvendo a disciplina necessária para conectar prioridade e resultado. |

**Fonte:** [Status Vivo](../../sources/personal/reunioes%20internas/status%20vivo_original.txt), primeira parte, seções 1–5; segunda parte, seções 1–6. SRC-PER-005, KU-PER-036–044. O Tech Product não é tratado como implantado; avanços de integração da COMP não equivalem a jornadas inteiras concluídas.

Essas frentes já contêm elementos da resposta: aprendizagem, dados, plataforma, capacidade e disciplina de produto. A oportunidade estratégica está em fazê-los convergir para as mesmas necessidades, com resultado e continuidade acompanhados.

### 4.3 iFood e Vivo: a comparação relevante é como uma necessidade chega ao resultado

**Modelo operativo** é a forma como uma organização distribui decisões, trabalho e recursos para entregar e manter um resultado. A comparação abaixo combina o relato de Clarisse com a síntese interna da Vivo. É uma comparação de mecanismos relatados, sem medição comparável de desempenho entre as empresas.

| Dimensão | iFood — relato de Clarisse | Vivo — situação descrita no anexo | Questão de desenho para a VPP |
|---|---|---|---|
| **Entrada e descoberta** | PM organiza demandas de diferentes origens junto à liderança funcional. | Cadastro, triagem e qualifying; a síntese registra demandas incompletas e esforço de qualificação. | Como reunir os envolvidos cedo para esclarecer o problema uma vez e evitar devoluções? |
| **Ownership** | Liderança funcional orienta a direção; PM acompanha escolhas e evolução do produto. | Há papéis de PM/PO e responsáveis; a evolução proposta busca responsabilidade por valor após a entrega. | Quem permanece responsável desde a necessidade até adoção, resultado e manutenção? |
| **Prioridade e capacidade** | Alocação seletiva de PM e capacidade técnica por produtos. | Comitês, backlogs e roadmaps; tensão de capacidade e proposta de distinguir carteira obrigatória e discricionária. | Como tornar a capacidade disponível e o custo de oportunidade visíveis numa mesma carteira? |
| **Dados e autonomia** | Responsáveis de subdomínio, referências em dados e acesso controlado. | Data Mesh em expansão; relato de dependência de especialista e necessidade de ampliar adoção. | Como distribuir conhecimento e responsabilidade sem criar definições divergentes? |
| **Construção e sustentação** | Tecnologia corporativa atende produtos; manutenção influencia construir ou adquirir. | Esteiras internas e parceiros; COMP expõe dependências de integração e internalização; Tech Product busca reuso. | Como garantir capacidade de continuidade e componentes comuns desde o desenho? |
| **Velocidade** | Há mecanismos de coordenação e experimentação, com retrabalho também relatado. | Há percepção de demora e fragmentação; os tempos por etapa não estão medidos nas fontes. | Onde estão espera, devolução e retrabalho, e quais decisões podem ocorrer juntas? |

**Fontes:** SRC-PER-001, 24:57–27:40 e 31:44–38:47, para produto e desenvolvimento; 10:39–18:48, para dados. SRC-PER-005, primeira parte, seções 1–4, e segunda parte, seções 2–6, para Vivo. A percepção interna de repasses também aparece em SRC-PER-001, Participante 1, 00:21–04:35; não é uma avaliação feita pelo iFood.

A recomendação que emerge é **testar responsabilidade de ponta a ponta e capacidade conectada ao produto**, aproveitando a evolução já descrita no Jeito de Produtar. O tema cabe nesta estratégia porque a visão só se realiza se as mudanças conseguirem sair da descoberta, chegar ao uso e continuar úteis. Seu desenho concreto aparece no capítulo 9, depois de explicitar o papel de Pessoas, a visão e as escolhas.

Assim, o contexto da Vivo acrescenta uma condição aos aprendizados do mercado: a estratégia deve integrar capacidades e iniciativas já existentes. Isso nos permite definir a contribuição específica da VP.
'''
    roles = part('## 5. Duas', '## 6. Nossa')
    roles = roles.replace('**Discussão:** quais dessas contribuições a VP deve assumir diretamente, quais deve construir em parceria e quais precisam de um acordo corporativo?', 'As duas responsabilidades delimitam a contribuição da VP: preparar a organização para o trabalho que muda e fazer seus próprios serviços acompanharem essa mudança.')
    roles = roles.replace('**Passagem:** para mobilizar a VP inteira, essas responsabilidades precisam virar uma imagem de futuro que cada pessoa consiga reconhecer.', '**O mercado mostrou os mecanismos; o contexto Vivo mostrou as bases e as tensões; as duas responsabilidades definiram nossa contribuição. A visão de 2028 pode agora sintetizar esse percurso.**')
    vision = part('## 6. Nossa', '## 7. Como')
    vision = vision.replace('## 6. Nossa visão para 2028', '''## 6. Visão 2028: a conclusão do percurso

Cada elemento da visão decorre de uma conclusão construída até aqui:

| O que aprendemos | O que encontramos na Vivo | O que isso pede da visão |
|---|---|---|
| Acelerar tarefas só ajuda plenamente quando melhora o processo; o Nubank torna concreto o redesenho. | Há iniciativas de transformação de jornadas e evolução da gestão de produtos. | **Trabalho mais simples:** resolver necessidades com menos esforço e passagens dispensáveis. |
| BB e Mercado Livre ligam aprendizagem e competências ao trabalho; Nubank inclui talento e organização na estratégia. | Eu Vivo IA e dados de Skills oferecem bases para desenvolver capacidades ligadas às necessidades da empresa. | **Pessoas mais preparadas:** profissionais e líderes capazes de executar, julgar e adaptar o trabalho. |
| iFood evidencia ownership e continuidade; os casos distinguem uso e impacto. | Data Mesh, plataforma e parceiros precisam convergir com prioridades, capacidade e sustentação. | **Entregas melhores:** mudanças que chegam ao beneficiário e mantêm qualidade, prazo e utilidade. |

Esses três resultados expressam as duas responsabilidades de Pessoas. Eles se unem na visão:''')
    vision = vision.replace('Em 2028, queremos uma VP Pessoas que usa IA para simplificar o dia a dia, desenvolver pessoas e ajudar a Vivo a entregar melhores resultados.', 'Em 2028, a VP Pessoas terá integrado IA à forma de preparar a organização e de prestar seus serviços: trabalho mais simples, profissionais e líderes capazes de aprender e adaptar sua atuação, e entregas melhores para a Vivo, sustentadas por dados confiáveis e responsabilidade de ponta a ponta.')
    vision = vision.replace('Essa visão se traduz', 'Essa é a ambição estratégica. Ela se traduz')
    vision = vision.replace('Essas cenas são imagens de futuro propostas, não projetos aprovados.', 'Essas cenas ilustram a experiência pretendida para 2028.')
    vision = re.sub(r'\*\*Discussão da visão:\*\*.*?(?=\n\n|$)', 'A visão se completa quando os três compromissos aparecem juntos: simplificação que preserva qualidade, aprendizagem que se aplica e entregas que atendem uma necessidade. As próximas escolhas definem como concentrar esforço para produzi-los.', vision, flags=re.S)
    choices = part('## 7. Como', '## 9. Quem')
    choices = choices.replace('Propomos cinco escolhas para orientar a execução:', 'A visão exige escolhas sobre onde concentrar esforço e como trabalhar. Cada escolha responde a uma condição demonstrada no percurso:')
    choices = choices.replace('Essas são capacidades de execução propostas.', 'O assessment Gartner disponível no projeto pode ajudar a verificar essas condições: estratégia, valor, organização, pessoas e cultura, governança, engenharia e dados. As respostas ainda não foram preenchidas; capacidades corporativas e específicas de Pessoas devem ser distinguidas na avaliação. [Assessment catalogado — SRC-037](../../evidence/external/GARTNER_AI_MATURITY_ASSESSMENT_TRANSCRICAO.md).\n\nEssas são capacidades de execução propostas.')
    choices = choices.replace('## 8. Por onde começar:', '**Com critérios e capacidades definidos, podemos escolher um primeiro recorte de execução.**\n\n## 8. Por onde começar:')
    choices = choices.replace('Integração de novos colaboradores, orientação sobre políticas ou desenvolvimento podem concorrer, conforme sua relevância.', 'As frentes já em curso, como recrutamento interno, offboarding e a aplicação de dados de Skills, entram primeiro no inventário de candidatos. Integrar uma delas ao primeiro ciclo depende de problema, estágio e capacidade; não exige abrir um projeto adicional. Outras necessidades podem concorrer quando sua relevância estiver demonstrada.')
    choices += '\n\nSelecionar a frente define onde atuar. Para que ela avance, precisamos explicitar como os envolvidos decidirão e trabalharão juntos — a resposta à comparação de modelo operativo do capítulo 4.\n'
    operating = '''
## 9. Modelo operativo: responsabilidade de ponta a ponta, com capacidades compartilhadas

A proposta é testar um arranjo por produto ou jornada prioritária, com um responsável pelo resultado e capacidade combinada entre Pessoas, HR Tech e Data, tecnologia corporativa e parceiros. Ele desdobra a direção de estratégia, produto/core e execução descrita no Jeito de Produtar.

Um **produto**, aqui, é uma solução ou serviço mantido para resolver uma necessidade recorrente. Um **responsável pelo resultado** acompanha sua utilidade ao longo do tempo. O PM organiza descoberta, prioridades e evolução; o responsável funcional decide os critérios e mudanças do processo. Essas responsabilidades precisam ser claras mesmo quando uma pessoa acumula papéis. Sua separação não exige, por si só, criar cargos ou mudar o organograma.

### 9.1 Como a necessidade atravessa o modelo

| Momento | Forma de trabalhar proposta | Responsabilidade e saída concreta |
|---|---|---|
| **Definir o resultado** | Negócio, especialista funcional e produto delimitam a necessidade e a situação inicial. | Responsável funcional responde pelo benefício; PM mantém problema, medida e prioridade explícitos. |
| **Descobrir e desenhar juntos** | Quem conhece a rotina trabalha com produto, dados e tecnologia; controles aplicáveis entram cedo. | Equipe define o que eliminar, o papel humano, os dados e a alternativa viável. Incertezas ficam registradas. |
| **Comprometer capacidade** | Portfólio confronta prioridades com pessoas disponíveis, manutenção e dependências. | Liderança de portfólio e responsáveis técnicos registram alocação e escolhas; entrada na carteira não equivale a início. |
| **Construir e testar** | Entregas pequenas usam plataformas e dados compartilhados quando adequados. | Responsável técnico responde por qualidade técnica; dono funcional e usuários avaliam utilidade e efeito no trabalho. |
| **Operar e evoluir** | A mesma responsabilidade de produto acompanha adoção, erros, resultado e custo. | Responsáveis pelo serviço, conteúdo, dados e suporte mantêm condições de continuidade; portfólio decide evolução. |

**Ownership não concentra todas as decisões em uma pessoa.** Ele torna inequívoco quem responde pelo resultado e articula as decisões necessárias. Dados mantêm seus responsáveis por definição, qualidade e acesso; tecnologia responde por arquitetura e operação; áreas funcionais respondem por conteúdo e processo.

### 9.2 Autonomia proporcional ao uso e às consequências

A contribuição do iFood sugere distribuir a descoberta, com um caminho claro para incorporar o que merece continuidade. Para a VPP, propomos três situações:

| Situação | Autonomia proposta | Condição para avançar |
|---|---|---|
| Aprendizagem e experimentação individual | Testar atividades com recursos e dados permitidos, dentro das regras corporativas. | Saber conferir a resposta e identificar limitações. |
| Teste acompanhado em um processo | Experimentar com escopo delimitado, responsável e participação de especialistas. | Verificar qualidade, efeitos, dados e controles antes de ampliar o uso. |
| Serviço do qual outras pessoas dependem | Operar com responsabilidade funcional e técnica, suporte e acompanhamento. | Demonstrar benefício e manter atualização, acesso, custo e resposta a falhas. |

O tipo de dado e o impacto de uma decisão também determinam a análise necessária: um experimento pequeno pode exigir cuidado elevado. A proposta deve funcionar dentro dos canais e controles corporativos vigentes.

### 9.3 Velocidade: reduzir espera e retrabalho no caminho inteiro

A hipótese de aceleração tem mecanismos concretos: descoberta conjunta reduz devoluções por falta de contexto; decisões de portfólio tornam capacidade explícita; dados e componentes reutilizáveis evitam reconstrução; responsabilidade contínua reduz repasses sem resolução.

Para verificar essa hipótese, cada frente acompanha **tempo até o primeiro teste útil, tempo até a resolução em operação, espera por etapa, devoluções e retrabalho**. Qualidade, incidentes e esforço de revisão acompanham essas medidas. Construir rapidamente uma solução que não pode operar não realiza a ambição de velocidade.

Não há baseline comparável entre iFood e Vivo nas fontes. A melhoria será medida contra o fluxo real da própria VPP. Se a espera estiver principalmente numa dependência externa, reorganizar a equipe local pode ser insuficiente; será necessário tratar essa dependência.

### 9.4 Onde as capacidades existentes entram

HR Tech e Data articula descoberta, dados, solução e acompanhamento de valor. Os especialistas funcionais mantêm critérios e conteúdo; referências de dados nas áreas podem distribuir conhecimento e apoiar adoção. Data Mesh provê informação reutilizável conforme a prontidão de cada produto de dados. Violeta e a proposta de Tech Product devem ser avaliados como base técnica, com suporte e condições de uso verificadas.

Parceiros como a COMP entram na capacidade de entrega com interfaces, critérios de aceite, manutenção e condições de saída definidos. A eventual internalização deve ser avaliada desde a escolha técnica e contratual; seguir padrões internos pode facilitar a transição, mas não a garante. Isso responde à tensão de velocidade e continuidade encontrada no anexo.

O desenho será testado nas frentes selecionadas. Uma mudança estrutural mais ampla passa a fazer sentido se o teste mostrar decisões ou capacidades que o arranjo atual não consegue atender. O critério é sua contribuição para resultado, qualidade e continuidade.

**Base da recomendação:** comparação do capítulo 4.3; SRC-PER-001, KU-PER-051–052; SRC-PER-005, KU-PER-037–044. O arranjo acima é uma proposta para a Vivo, não uma estrutura já implantada ou uma reprodução integral do iFood.

O modelo operativo explica como entregar. Para saber se ele realiza a visão, precisamos medir os três resultados que orientaram seu desenho.
'''
    measures = part('## 10. Como', '## 12. O que')
    measures = re.sub(r'\*\*Discussão:\*\*.*?(?=\n\n|$)', 'Os critérios para continuar, corrigir ou interromper serão registrados antes do teste. Assim, a decisão se apoia no benefício pretendido e nas condições de qualidade, sem selecionar apenas a medida que parecer melhor depois.', measures, flags=re.S)
    measures = measures.replace('Propomos uma sequência de cinco fases. **A duração, o calendário e os intervalos entre fases serão definidos depois**, considerando prioridades, recursos e dependências. O horizonte de visão continua sendo 2028; ele não atribui prazo a cada entrega abaixo.', 'A execução avança por cinco fases, com condições verificáveis de passagem. O planejamento de cada frente estabelece metas e prazos conforme seu ponto de partida, capacidade e dependências, mantendo o horizonte de 2028 como direção comum.')
    measures = measures.replace('Entrega para discussão e aceite', 'Entrega verificável').replace('Visão discutida, parceiros identificados', 'Direção traduzida em resultados, parceiros identificados')
    measures = measures[:measures.index('### O que será combinado depois')].rstrip()
    closing = '''

## 12. A estratégia de IA da VPP que resulta desse percurso

O argumento começou numa tarefa: preparar uma conversa. Mostrou que o resultado depende do processo, das competências e de quem assume suas decisões. Os casos acrescentaram aprendizagem aplicada, atualização de talento, coordenação da transformação e responsabilidade pela continuidade. A Vivo trouxe bases concretas e uma necessidade de conectá-las: formação, dados, plataforma, parceiros e evolução da gestão de produtos.

**A estratégia é combinar aprendizagem ampla com transformações selecionadas do trabalho, conectando as capacidades existentes por meio de responsabilidade de ponta a ponta e medindo o efeito sobre a execução da Vivo.**

| Elemento da estratégia | Definição resultante |
|---|---|
| **Visão 2028** | Trabalho mais simples, pessoas mais preparadas e entregas melhores, com IA integrada aos serviços de Pessoas e à preparação da organização. |
| **Contribuição da VPP** | Preparar profissionais e líderes da Vivo e transformar os processos e serviços da própria VP. |
| **Escolha de foco** | Aprendizagem ampla e poucas transformações acompanhadas, começando pelo inventário e pelas necessidades demonstradas. |
| **Forma de operar** | Responsável pelo resultado, descoberta conjunta, capacidade definida e dados e tecnologia compartilhados. |
| **Evidência de avanço** | Melhoria de resolução, competência aplicada e resultado, considerando qualidade, esforço total e continuidade. |
| **Caminho de execução** | Selecionar, desenhar, testar, avaliar e incorporar à rotina; ampliar conforme benefício e capacidade demonstrados. |

Assim, a visão de 2028 reúne o conhecimento acumulado e orienta as escolhas seguintes: desenvolver pessoas para o trabalho que muda, simplificar esse trabalho e organizar a entrega para que o benefício chegue à Vivo e se sustente.

## Fontes e limites de interpretação

Os dois anexos estão preservados e catalogados no padrão da camada pessoal do projeto: [Status Vivo](../../sources/personal/reunioes%20internas/status%20vivo_original.txt), SRC-PER-005, e [Evidence Book v2](../../sources/personal/outras%20fontes%20pessoais/evidence_book_ia_trabalho_pessoas_benchmarks_brasil_v2.md), SRC-PER-006. Manifesto, unidades temáticas e síntese estão em [evidence/personal](../../evidence/personal/README.md).

O Status Vivo é uma síntese interna derivada, com registros de diferentes datas e propostas em evolução. O Evidence Book é um mapa de pesquisa: suas classificações e recomendações não constituem comprovação independente. A seleção de casos preserva o vínculo com as fontes citadas e evita transferir metas ou estruturas de outras empresas à Vivo.

O HR Think Tank ocorreu em agosto de 2026, conforme correção da usuária. O conteúdo utilizado é o resumo disponível do evento. A data da conversa com iFood permanece não confirmada. A comparação descreve mecanismos e hipóteses de melhoria; não demonstra superioridade de velocidade ou maturidade entre empresas.

O [roteiro narrativo](ROTEIRO_NARRATIVO_V2_FORA_PARA_DENTRO.md) acompanha esta versão. O dossiê anterior fica como fundamentação histórica; esta estratégia e o roteiro narrativo definem a sequência atual.
'''
    result = '\n\n'.join(x.strip() for x in [opening, cases, vivo, roles, vision, choices, operating, measures, closing])
    result = result.replace('nem presume uma solução aprovada', 'nem presume uma solução disponível')
    write(path, result)

if __name__ == '__main__':
    catalog()
    revise()

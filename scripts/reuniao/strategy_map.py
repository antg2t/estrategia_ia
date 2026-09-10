"""Gartner grounding and the shared executive strategy map."""

BETS = [
    ('01', 'Estratégia e metas<br>na origem', 'Direcionar produtos e capacidade'),
    ('02', 'Experiência integrada<br>de IA', 'Tornar o apoio acessível'),
    ('03', 'Conhecimento<br>reutilizável', 'Sustentar confiança e consistência'),
    ('04', 'Preparação<br>da organização', 'Desenvolver competência e julgamento'),
    ('05', 'Reinvenção<br>dos serviços', 'Redesenhar para resolver melhor'),
]
RESULTS = [
    ('Trabalho<br> mais simples', 'Menos esforço, etapas e retrabalho.'),
    ('Pessoas<br> mais preparadas', 'Aplicação de IA, julgamento e adaptação.'),
    ('Entregas<br> melhores', 'Prioridades atendidas com qualidade e continuidade.'),
]

def map_body():
    return '''<div class="strategy-map" role="img" aria-label="Gartner, mercado e Vivo fundamentam o mandato de preparar a organização e reinventar Pessoas. Cinco big bets, em conjunto, são os meios para alcançar três resultados até 2028.">
    <div class="map-foundations"><div><b>Gartner</b><span>Referenciais de transformação</span></div><div><b>Mercado</b><span>Mecanismos e experiências</span></div><div><b>Vivo</b><span>Direção, bases e necessidades</span></div></div>
    <div class="map-mandate"><span>PREPARAR A ORGANIZAÇÃO</span><i>+</i><span>REINVENTAR PESSOAS</span></div>
    <div class="map-label"><b>5 BIG BETS</b><span>OS MEIOS · ONDE CONCENTRAR NOSSAS ESCOLHAS</span></div>
    <div class="map-bets">'''+''.join('<div class="map-bet"><span>'+n+'</span><h3>'+t+'</h3><p>'+d+'</p></div>' for n,t,d in BETS)+'''</div>
    <div class="map-convergence"><span>EM CONJUNTO, PARA ALCANÇAR</span></div>
    <div class="map-label results-label"><b>3 RESULTADOS</b><span>O DESTINO · VISÃO 2028</span></div>
    <div class="map-results">'''+''.join('<div><h3>'+t+'</h3><p>'+d+'</p></div>' for t,d in RESULTS)+'''</div></div>'''

def revise(slides, add, cards, takeaway, table):
    add('gartner','Trabalho','Gartner: uma referência para<br>estruturar a transformação.','Os referenciais orientam a leitura dos casos e as escolhas para a Vivo.',
        cards([('Dois mandatos','Preparar e transformar','Pessoas habilita a transformação empresarial e reinventa a própria função.'),('Trabalho completo','Conectar execução a valor','Processos, decisões e papéis evoluem; o benefício precisa chegar ao resultado.'),('Capacidade contínua','Sustentar a mudança','Direção, produtos, dados, adoção, governança e mensuração funcionam juntos.')])+takeaway('Os casos mostram <strong>práticas convergentes</strong>, em configurações diferentes. A proposta para a Vivo traduz esses aprendizados.'),
        sources=['SRC-018','SRC-019','SRC-026','SRC-027','SRC-032'],chapter=1,section='1.7',label='Referenciais Gartner · síntese do acervo',bridge='Com essa lente, observamos como a transformação aparece nas empresas.',note='Paráfrases do acervo catalogado. SRC-018 pp. 1–7; SRC-019 pp. 1–9; SRC-026 pp. 4–14; SRC-027 pp. 3–23; SRC-032 slides 2–6 e 31–35. Não afirmar que os casos seguiram a Gartner ou que ela endossou a proposta.')
    g=slides.pop(); slides.insert(next(i for i,s in enumerate(slides) if s['id']=='mercado-transicao'),g)
    by_id={s['id']:s for s in slides}
    by_id['percurso']['body']=by_id['percurso']['body'].replace('Da tarefa ao resultado','Mudança no trabalho e referenciais Gartner')
    by_id['abertura']['bridge']='Trabalho e Gartner → mercado → Vivo → cinco big bets → três resultados.'
    by_id['trabalho']['bridge']='A Gartner oferece referenciais para conectar essa mudança à transformação da organização.'
    by_id['mercado-transicao']['sub']='Como as práticas relatadas pelas empresas dão concretude aos referenciais de transformação?'
    by_id['mercado']['sub']='Práticas convergentes com os referenciais Gartner: aprendizagem, redesenho e capacidade de execução.'
    by_id['mandatos']['sources']=['SRC-018','SRC-019']
    by_id['mandatos']['sub']='Dois mandatos presentes nos referenciais Gartner, traduzidos para a Vivo.'
    by_id['visao']['sub']='O destino da estratégia até 2028. As cinco big bets são os meios para alcançar estes três resultados.'
    by_id['visao']['body']='<div class="vision-bases"><span>Menos esforço e retrabalho</span><span>Aplicação e julgamento</span><span>Prioridades atendidas com qualidade</span></div>'
    by_id['visao']['note']='Os três resultados são compartilhados pelas cinco big bets. Não apresentar uma correspondência exclusiva entre uma big bet e um resultado.'
    by_id['apostas-transicao']['title']='Três resultados.<br>Cinco meios para alcançá-los.'
    by_id['apostas-transicao']['sub']='As big bets definem onde concentrar investimento, atenção e desenvolvimento organizacional.'
    by_id['apostas-transicao']['bridge']='As cinco big bets se reforçam e contribuem em conjunto para os três resultados.'
    by_id['apostas']['title']='Cinco big bets.<br>Os meios para realizar a visão.'
    by_id['apostas']['sub']='Atuam em conjunto para alcançar trabalho mais simples, pessoas mais preparadas e entregas melhores.'
    by_id['apostas']['bridge']='Cada big bet constrói uma condição; a combinação das cinco produz os resultados pretendidos.'
    by_id['derivacao']['title']='Os resultados definem<br>o destino da estratégia.'
    by_id['derivacao']['sub']='Gartner, mercado e contexto Vivo fundamentam as escolhas. A visão expressa a mudança pretendida.'
    by_id['derivacao']['body']=table(['Resultado até 2028','Mudança pretendida'],[[t.replace('<br>',' '),d] for t,d in RESULTS])+takeaway('<strong>Os três resultados são o destino. As cinco big bets são os meios para alcançá-los.</strong>')
    by_id['valor']['sub']='Avaliamos a contribuição conjunta das cinco big bets aos três resultados, com situação inicial, custo total e qualidade.'
    by_id['valor']['sources']=['SRC-006','SRC-036']
    by_id['reinvencao']['note']+=' Considerar IA desde a concepção inclui escolher simplificação, automação por regras ou IA conforme valor, viabilidade e risco. SRC-014 pp. 1–5; SRC-028 pp. 2–5.'
    by_id['interfaces']['body']+= '<p class="evidence-note">Cada uso precisa de responsável, avaliação de qualidade, limites de autonomia, participação humana conforme o impacto e correção de falhas.</p>'
    by_id['interfaces']['sources']=['SRC-025']
    by_id['trajetoria']['note']+=' O investimento acompanha a incerteza: justificativa econômica para iniciativas maduras; testes delimitados e critérios de ampliar, corrigir ou encerrar para iniciativas incertas. SRC-016 pp. 2–9.'
    by_id['trajetoria']['sources']=['SRC-016']
    final=by_id['encerramento']
    final.update(title='Cinco big bets. Três resultados.',sub='Estratégia de IA da VP Pessoas · Preparar a organização e reinventar seus serviços.',body=map_body(),kind='strategy',label='Mapa executivo · proposta',bridge='Cinco meios que se reforçam para realizar a visão 2028.',note='Mapa de síntese. Gartner, mercado e Vivo fundamentam a proposta. As cinco big bets são escolhas para a Vivo e contribuem em conjunto aos três resultados. Não representa endosso Gartner.')

"""Consistent overview/detail names and connected direction/execution routes."""
from copy import deepcopy
from strategy_map import BETS

BET_IDS = ['metas', 'experiencia', 'conhecimento', 'preparacao', 'reinvencao']
EXECUTION = [('modelo', 'Definir responsabilidades'), ('camadas', 'Organizar capacidades compartilhadas'), ('trajetoria', 'Conduzir a evolução'), ('valor', 'Acompanhar os resultados')]

def revise_narrative(slides, add, cards, takeaway, table):
    by = {s['id']: s for s in slides}
    final = deepcopy(by['encerramento'])
    names = [title.replace('<br>', ' ') for _, title, _ in BETS]
    by['apostas']['body'] = '<div class="bets-system"><button class="bet-primary" data-jump="metas"><b>01</b><span><strong>'+names[0]+'</strong><small>Direcionar produtos e capacidade.</small></span><i>↗</i></button><div class="bet-grid">'+''.join('<button data-jump="'+sid+'"><b>'+n+'</b><h3>'+name+'</h3><p>'+desc+'.</p><span aria-hidden="true">↗</span></button>' for sid,(n,_,desc),name in zip(BET_IDS[1:], BETS[1:], names[1:]))+'</div></div>'
    messages = [
        'Resultados estratégicos orientam os produtos, a capacidade e as escolhas da VP.',
        'A pessoa expressa a necessidade; a experiência conecta os recursos que podem ajudá-la.',
        'Dados, regras e recursos mantidos em comum sustentam respostas consistentes.',
        'Aprendizagem, liderança e práticas de talento fazem a aplicação de IA mudar o trabalho.',
        'Redesenhar necessidades, etapas e papéis torna a transformação uma capacidade de Pessoas.',
    ]
    for i, sid in enumerate(BET_IDS):
        by[sid].update(title=names[i], sub=messages[i], label=f'Big bet {i+1:02} de 05 · proposta')
        by[sid]['detail'] = []
    by['experiencia'].update(chapter=7, section='7.2')
    by['apostas']['bridge'] = 'Começamos por Estratégia e metas na origem: o que orienta as escolhas.'
    by['metas']['bridge'] = 'Com a direção definida, Experiência integrada de IA aproxima as pessoas dos recursos.'
    by['experiencia']['bridge'] = 'Essa experiência depende de Conhecimento reutilizável para responder com consistência.'
    by['conhecimento']['bridge'] = 'Recursos confiáveis precisam de Preparação da organização para serem bem aplicados.'
    by['preparacao']['bridge'] = 'Pessoas preparadas participam da Reinvenção dos serviços e da mudança do trabalho.'
    by['reinvencao']['bridge'] = 'As cinco big bets estão definidas. Execução organiza como realizá-las em conjunto.'
    by['visao']['detail'] = []
    by['visao']['bridge'] = 'Estes três resultados são o destino. As cinco big bets definem os meios para alcançá-los.'
    by['direcao-transicao']['sub'] = 'Que responsabilidade assumimos, quais resultados buscamos e onde concentramos as escolhas?'
    by['mandatos']['bridge'] = 'Preparar a organização e reinventar Pessoas se traduzem em três resultados para 2028.'

    by['execucao-transicao']['sub'] = 'Como realizar as cinco big bets e verificar sua contribuição aos três resultados?'
    by['execucao-transicao']['bridge'] = 'Quatro perguntas organizam a execução do mesmo conjunto de big bets.'
    add('execucao-mapa', 'Execução', 'Como executar as cinco big bets.',
        'Responsabilidades, capacidades, evolução e resultados organizam a realização das escolhas.',
        '<div class="execution-index">'+''.join('<button data-jump="'+sid+'"><span>'+str(i+1).zfill(2)+'</span><h3>'+title+'</h3><p>'+q+'</p></button>' for i, ((sid,title),q) in enumerate(zip(EXECUTION, ['Quem decide, entrega e sustenta?', 'O que os produtos precisam compartilhar?', 'Como avançar e decidir o próximo passo?', 'Que mudança demonstra valor?'])))+'</div>'+takeaway('As <strong>cinco big bets</strong> seguem como escolhas estratégicas. Estas quatro perguntas organizam sua execução.'),
        chapter=9, bridge='Primeiro, Definir responsabilidades para que cada escolha tenha continuidade.')
    by = {s['id']: s for s in slides}
    for i, (sid, title) in enumerate(EXECUTION):
        by[sid].update(title=title, group='Execução', label=f'Execução {i+1:02} de 04 · proposta')
    by['modelo']['sub'] = 'As metas entram na carteira com decisão, entrega e sustentação claramente atribuídas.'
    by['modelo']['body'] = table(['Papel proposto', 'Responsabilidade na execução'], [
        ['Liderança funcional', 'Definir resultados e escolhas de investimento.'],
        ['Gestão de produto · PMs', 'Traduzir metas em evolução do produto e acompanhar o resultado.'],
        ['Negócio e especialistas de Pessoas', 'Definir critérios do serviço, impactos no trabalho e preparação das pessoas.'],
        ['Tecnologia e dados', 'Disponibilizar recursos, integrar e sustentar a operação.'],
        ['Segurança e privacidade', 'Participar das decisões conforme o uso, os dados e o impacto.'],
    ]) + takeaway('Cada uso precisa de <strong>responsável, avaliação, limites de autonomia e correção de falhas.</strong>')
    by['modelo']['sources'] = ['SRC-025']
    by['modelo']['detail'] = []
    by['modelo']['note'] += ' Interfaces integradas neste quadro. Responsabilidades propostas para discussão nas instâncias existentes; SRC-025, pp. 3–9.'
    by['modelo']['bridge'] = 'Com responsáveis definidos, Organizar capacidades compartilhadas evita reconstruir as mesmas bases.'
    by['camadas']['sub'] = 'As quatro camadas detalham a base comum para Experiência integrada de IA e Conhecimento reutilizável.'
    by['camadas']['bridge'] = 'Com a cobertura das bases visível, Conduzir a evolução conecta investimento, uso e aprendizagem.'
    by['trajetoria']['sub'] = 'Conectar, incorporar e ampliar: movimentos orientados por metas, capacidade e evidências.'
    by['trajetoria']['body'] += takeaway('A cada movimento, decidir com evidências: <strong>ampliar, corrigir ou encerrar.</strong>')
    by['trajetoria']['bridge'] = 'Para decidir o próximo passo, Acompanhar os resultados retoma a visão 2028.'
    by['valor']['sub'] = 'Os mesmos três resultados da visão orientam a avaliação conjunta das cinco big bets.'
    by['valor']['bridge'] = 'As evidências de valor permitem consolidar os ajustes da estratégia e da execução.'
    by['revisao'].update(title='Acompanhar os resultados', label='Execução 04 de 04 · aprofundamento', sub='Quando os sinais não melhoram, investigar a causa e ajustar a execução das big bets.')
    by['revisao']['bridge'] = 'Os ajustes identificados alimentam a discussão sobre direção e execução.'
    by['discussao']['sub'] = 'Retomamos a visão, as cinco big bets e as quatro perguntas de execução.'
    by['discussao']['body'] = '<div class="discussion-prompts"><div><b>01</b><h3>A visão expressa a mudança que queremos?</h3><p>Trabalho mais simples · Pessoas mais preparadas · Entregas melhores.</p></div><div><b>02</b><h3>As cinco big bets sustentam essa visão?</h3><p>'+ ' · '.join(names) +'.</p></div><div><b>03</b><h3>O que precisamos esclarecer na execução?</h3><p>'+ ' · '.join(t for _,t in EXECUTION) +'.</p></div></div>'
    by['discussao']['bridge'] = 'O mapa final reúne os fundamentos, as cinco big bets e os três resultados discutidos.'

    # Overview labels also serve as literal titles throughout the benchmark block.
    cases = [('bb','Aprender no trabalho'), ('meli','Compartilhar capacidades'), ('nubank','Redesenhar com as pessoas'), ('ifood','Ligar direção e entrega'), ('toqan','Ampliar a autonomia'), ('comparacao','Comparar as funções')]
    for sid, title in cases:
        by[sid]['title'] = title
    for sid, parent in [('meli-pessoas','Compartilhar capacidades'), ('performance','Redesenhar com as pessoas'), ('nubank-publico','Redesenhar com as pessoas')]:
        previous = by[sid]['title'].replace('<br>', ' ')
        by[sid].update(title=parent, sub=previous+' '+by[sid]['sub'], label=by[sid]['label']+' · aprofundamento')
    by['trabalho']['bridge'] = 'Do exemplo do trabalho aos referenciais que ajudam a estruturar a transformação.'
    by['papeis']['bridge'] = 'Essas responsabilidades se conectam aos referenciais Gartner de transformação.'
    by['mercado']['bridge'] = 'Aprendizagem, recursos, redesenho, direção e autonomia orientam a leitura das bases Vivo.'
    by['comparacao']['bridge'] = 'Com as funções do mercado esclarecidas, olhamos as bases e necessidades da Vivo.'
    by['percurso']['body'] = by['percurso']['body'].replace('Modelo, evolução e valor', 'Responsabilidades, capacidades, evolução e resultados')
    for sid, executive, extended in [
        ('trabalho', 'O exemplo do trabalho nos leva aos referenciais Gartner de transformação.', 'No mesmo exemplo, a profundidade da mudança depende do problema que queremos resolver.'),
        ('mercado', 'Essas cinco referências orientam a leitura das bases e necessidades da Vivo.', 'Começamos pelo Banco do Brasil: Aprender no trabalho.'),
        ('bases', 'As bases Vivo nos levam à Direção: responsabilidades, visão e cinco big bets.', 'Essas bases se apoiam na direção corporativa já existente na Vivo.'),
        ('valor', 'As evidências de valor alimentam a discussão sobre direção e execução.', 'Acompanhar os resultados também mostra quando ajustar a execução.'),
    ]:
        by[sid]['route_bridges'] = {'executivo': executive, 'estendido': extended}
    removed = {'derivacao', 'apostas-transicao', 'capacidades-transicao', 'interfaces'}
    order = [s['id'] for s in slides if s['id'] not in removed | {'camadas','execucao-mapa'}]
    order.insert(order.index('modelo'), 'execucao-mapa')
    order.insert(order.index('modelo')+1, 'camadas')
    slides[:] = [by[sid] for sid in order]
    for s in slides:
        s['detail'] = [sid for sid in s['detail'] if sid not in removed]
    assert by['encerramento'] == final, 'Final slide must remain intact'

EXEC = ['abertura','percurso','trabalho-transicao','trabalho','gartner','mercado-transicao','mercado','vivo-transicao','bases','direcao-transicao','mandatos','visao','apostas',*BET_IDS,'execucao-transicao','execucao-mapa','modelo','camadas','trajetoria','valor','discussao','encerramento']

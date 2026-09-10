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
    revise_first_half(by)
    assert by['encerramento'] == final, 'Final slide must remain intact'

def revise_first_half(by):
    """Every early overview announces the literal titles used by its children."""
    from html import escape
    from bs4 import BeautifulSoup
    def plain(text):
        return BeautifulSoup(text.replace('<br>', ' '), 'html.parser').get_text(' ', strip=True)
    def index(items):
        return '<div class="narrative-index">'+''.join('<button data-jump="'+sid+'"><b>'+str(i+1).zfill(2)+'</b><span><h3>'+escape(plain(by[sid]['title']))+'</h3><p>'+description+'</p></span><i aria-hidden="true">↗</i></button>' for i,(sid,description) in enumerate(items))+'</div>'
    work = [
        ('trabalho', 'Da tarefa ao resultado', 'Preparar, conversar e acompanhar: o valor depende do caminho completo.'),
        ('profundidade', 'Profundidade da mudança', 'Apoiar uma atividade, redesenhar o processo ou criar uma capacidade.'),
        ('beneficio', 'Espera e retrabalho', 'Observar onde o benefício se perde até a necessidade ser resolvida.'),
        ('papeis', 'Responsabilidades no trabalho', 'Explicitar quem faz o benefício chegar ao resultado.'),
        ('gartner', 'Referenciais Gartner', 'Conectar o exemplo à transformação da organização.'),
    ]
    for i,(sid,title,sub) in enumerate(work):
        by[sid].update(title=title, sub=sub, label=f'Trabalho {i+1:02} de 05 · '+by[sid]['label'])
    by['trabalho']['sub'] += ' Exemplo: conversa de desenvolvimento.'
    by['trabalho-transicao'].update(kind='content', title='Trabalho', sub='Da tarefa ao resultado: cinco temas para entender o que precisa mudar.', body=index([(sid,sub) for sid,_,sub in work]), label='Mapa dos temas', detail=[sid for sid,_,_ in work])
    by['trabalho-transicao']['bridge'] = 'Da tarefa ao resultado abre o raciocínio com uma conversa de desenvolvimento.'
    by['trabalho']['route_bridges'] = {'executivo':'Referenciais Gartner conecta Da tarefa ao resultado à transformação da organização.', 'estendido':'Da tarefa ao resultado leva à próxima pergunta: qual Profundidade da mudança é necessária?'}
    by['profundidade']['bridge'] = 'Em qualquer Profundidade da mudança, Espera e retrabalho podem consumir o benefício.'
    by['beneficio']['bridge'] = 'Para reduzir Espera e retrabalho, precisamos esclarecer as Responsabilidades no trabalho.'
    by['papeis']['bridge'] = 'Responsabilidades no trabalho se conectam aos Referenciais Gartner de transformação.'
    by['gartner']['bridge'] = 'Os Referenciais Gartner orientam a leitura do Mercado: como essas práticas aparecem nas empresas?'

    cases = [('bb','Banco do Brasil','Aprender no trabalho'),('meli','Mercado Livre','Compartilhar capacidades'),('nubank','Nubank','Redesenhar com as pessoas'),('ifood','iFood','Ligar direção e entrega'),('toqan','Prosus / Toqan','Ampliar a autonomia')]
    by['mercado'].update(title='Cinco referências de mercado', sub='Cinco temas para ler os casos; ao final, Comparar as funções reúne os aprendizados.')
    by['mercado-transicao']['sub'] = 'Os Referenciais Gartner ganham concretude em Cinco referências de mercado.'
    by['mercado-transicao']['bridge'] = 'Cinco referências de mercado apresenta os nomes que orientam a leitura de cada caso.'
    for i,(sid,company,title) in enumerate(cases):
        by[sid+'-transicao'].update(title=title, sub=company+' · '+by[sid+'-transicao']['sub'], label=f'Referência {i+1:02} de 05')
        by[sid+'-transicao']['bridge'] = title+': a seguir, o mecanismo descrito no caso '+company+'.'
        by[sid]['label'] = f'Referência {i+1:02} de 05 · '+by[sid]['label']
    by['bb']['bridge'] = 'Aprender no trabalho exige recursos para aplicar. Mercado Livre aprofunda Compartilhar capacidades.'
    by['meli']['bridge'] = 'Compartilhar capacidades também alcança os serviços e as competências no Mercado Livre.'
    by['meli-pessoas'].update(sub='Mercado Livre · Capacidades compartilhadas nos serviços e na avaliação de competências.',label='Referência 02 de 05 · aprofundamento')
    by['meli-pessoas']['bridge'] = 'Recursos e competências levam a Redesenhar com as pessoas, no caso Nubank.'
    by['performance'].update(sub='Nubank · Performance: aplicação de Redesenhar com as pessoas, conforme o relato do evento.',label='Referência 03 de 05 · aprofundamento')
    by['nubank']['bridge'] = 'Redesenhar com as pessoas se concretiza no exemplo de performance do Nubank.'
    by['performance']['bridge'] = 'Ainda em Redesenhar com as pessoas, distinguimos os recursos públicos e seus estágios.'
    by['nubank-publico'].update(sub='Nubank · Recursos de apoio: AskNu para consulta e catálogo de skills para desenvolvedores.',label='Referência 03 de 05 · aprofundamento')
    by['nubank-publico']['bridge'] = 'O redesenho precisa de direção para entregar. O iFood mostra Ligar direção e entrega.'
    by['ifood']['bridge'] = 'Ligar direção e entrega orienta as escolhas. Ampliar a autonomia aproxima os recursos das pessoas.'
    by['toqan']['bridge'] = 'Após Ampliar a autonomia, Comparar as funções reúne o que as experiências oferecem.'
    by['comparacao']['sub'] = 'Retomada dos casos: o que a pessoa usa e o que a empresa precisa manter.'
    by['comparacao']['bridge'] = 'Comparar as funções nos ajuda a examinar a Vivo: direção, bases e conexões.'
    by['mercado']['route_bridges'] = {'executivo':'Cinco referências de mercado orienta o próximo bloco: Vivo.', 'estendido':'A primeira das Cinco referências de mercado é Aprender no trabalho, no Banco do Brasil.'}

    vivo = [('bases','Bases existentes','Eu Vivo IA, Data Mesh, Violeta, COMP e Jeito de Produtar.'),('vivo-corporativa','Direção corporativa','A contribuição de Pessoas parte da estratégia de IA já existente.'),('lacunas','Conexão entre metas e produtos','O que precisa estar definido antes de uma demanda disputar capacidade.')]
    for i,(sid,title,sub) in enumerate(vivo):
        by[sid].update(title=title,sub=sub,label=f'Vivo {i+1:02} de 03 · '+by[sid]['label'])
    by['bases']['sub'] = 'Cinco movimentos na VPP oferecem as Bases existentes para construir a estratégia.'
    by['vivo-transicao'].update(kind='content',sub='Os aprendizados do Mercado orientam três temas sobre o ponto de partida da Vivo.',body=index([(sid,sub) for sid,_,sub in vivo]),label='Mapa dos temas')
    by['vivo-transicao']['bridge'] = 'Começamos por Bases existentes: o que já está em movimento na VPP.'
    by['bases']['route_bridges'] = {'executivo':'As Bases existentes dão o ponto de partida para Direção: mandatos, resultados e cinco big bets.', 'estendido':'As Bases existentes se apoiam na Direção corporativa de IA já documentada.'}
    by['vivo-corporativa']['bridge'] = 'A Direção corporativa precisa se desdobrar na Conexão entre metas e produtos.'
    by['lacunas']['bridge'] = 'A Conexão entre metas e produtos leva à Direção proposta para Pessoas.'

    by['mandatos'].update(title='Preparar a organização.<br>Reinventar Pessoas.',sub='Dois mandatos conectam a Direção corporativa à contribuição da VP Pessoas.',label='Direção 01 de 03 · proposta')
    by['mandatos']['body'] = by['mandatos']['body'].replace('Preparar para<br>o trabalho com IA','Preparar a organização').replace('Reinventar serviços<br>e decisões de Pessoas','Reinventar Pessoas')
    by['visao']['label'] = 'Direção 02 de 03 · Visão 2028'
    direction = [('mandatos','Os dois mandatos da VP Pessoas.'),('visao','Os três resultados que queremos alcançar até 2028.'),('apostas','As escolhas que contribuem, em conjunto, para os três resultados.')]
    by['direcao-transicao'].update(kind='content',sub='O ponto de partida da Vivo se traduz em mandatos, resultados e escolhas.',body=index(direction),label='Mapa dos temas')
    by['direcao-transicao']['bridge'] = 'Preparar a organização. Reinventar Pessoas. define a contribuição da VP.'
    by['mandatos']['bridge'] = 'Os dois mandatos orientam os resultados: Trabalho mais simples. Pessoas mais preparadas. Entregas melhores.'
    by['visao']['bridge'] = 'Para alcançar os três resultados: Cinco big bets. Os meios para realizar a visão.'
    by['percurso']['title'] = 'Percurso'
    by['abertura']['bridge'] = 'Percurso apresenta os blocos Trabalho, Mercado, Vivo, Direção e Execução.'

EXEC = ['abertura','percurso','trabalho-transicao','trabalho','gartner','mercado-transicao','mercado','vivo-transicao','bases','direcao-transicao','mandatos','visao','apostas',*BET_IDS,'execucao-transicao','execucao-mapa','modelo','camadas','trajetoria','valor','discussao','encerramento']

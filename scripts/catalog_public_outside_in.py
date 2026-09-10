"""Registra pesquisa pública da revisão outside-in; preserva os registros anteriores."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'evidence' / 'public'
ROWS = [
    (6, 'The state of AI in 2026: On the road to ROI', 'https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai', '2026-08-25', 'survey', 'Key takeaways; Despite broader use; About the research', 'Pesquisa global por autorrelato; não permite inferência causal ou representatividade específica do Brasil. Página dinâmica substituiu a edição de 2025.', 'Ganhos individuais percebidos e impacto financeiro empresarial são medidas distintas; adoção não demonstra captura de valor.'),
    (7, 'Generative AI and jobs: A 2025 update', 'https://www.ilo.org/publications/generative-ai-and-jobs-2025-update', '2025-05-20', 'research_brief', 'Resumo do Working Paper 140', 'Exposição ocupacional estimada; não é previsão de desligamentos nem diagnóstico Vivo.', 'A análise por tarefas distingue exposição técnica e transformação do trabalho de substituição integral de cargos.'),
    (8, 'Generative AI at Work — arXiv v2', 'https://arxiv.org/abs/2304.11771', '2024-11-06', 'field_research', 'Abstract; v2', 'Implantação gradual em contexto específico. Versão v2: 5.172 agentes e 15%; NBER revisado em 2023 usa 5.179 e 14%. Não misturar versões.', 'O efeito do assistente em suporte varia conforme experiência e habilidade; ganho médio não é meta transferível a RH.'),
    (9, 'Shifting Work Patterns with Generative AI', 'https://www.hbs.edu/ris/Publication%20Files/w33795_dd1e2857-d195-4333-86ba-6a8953119ed4.pdf', '2025-05-06', 'randomized_field_experiment', 'Abstract, PDF p. 2; autoria/afiliação pp. 2–3', 'Autores incluem Microsoft Research. Tempo de e-mail não equivale a produtividade total; ITT e usuários frequentes têm denominadores distintos.', 'Acesso individual a IA alterou comportamentos individuais mais que comportamentos dependentes de coordenação.'),
    (10, 'Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity', 'https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/', '2025-07-10', 'randomized_experiment', 'Resumo e método; 16 desenvolvedores/246 tarefas', 'Ferramentas do início de 2025 e profissionais familiarizados com projetos maduros; não generalizar a todo trabalho técnico ou ao estado de 2026.', 'Um resultado negativo de produtividade em contexto real refuta a hipótese de benefício universal.'),
    (11, 'We are Changing our Developer Productivity Experiment Design', 'https://metr.org/blog/2026-02-24-uplift-update/', '2026-02-24', 'research_method_update', 'Abertura; Wider adoption; Details of the productivity study', 'Seleção de participantes/tarefas e tempo em agentes concorrentes prejudicam a estimativa atual; não usar resultados brutos como efeito causal estável.', 'A evolução do uso exige revisar o método de avaliação; o estudo anterior não deve ser tratado como retrato permanente.'),
    (12, 'Telefónica — Strategy: Transform & Grow 2026–2030', 'https://www.telefonica.com/en/about-us/strategy/', '2025-11-04', 'corporate_strategy', 'Context and new strategic reflection; Our six strategic pillars', 'Data do lançamento do plano, não data comprovada de atualização da página. Direção do grupo não substitui metas locais brasileiras.', 'A estratégia do grupo relaciona experiência, crescimento, tecnologia, simplificação e desenvolvimento de talento.'),
    (13, 'Telefônica Brasil — Perfil Corporativo', 'https://ri.telefonica.com.br/a-empresa/perfil-corporativo/', '2026-05-11', 'corporate_publication', 'Descrição do negócio; data de atualização', 'Dados de divulgação institucional com data própria; não usar como quadro atual de RH sem reconciliação. Fonte contextual, sem estatísticas transplantadas para a estratégia.', 'O perfil público descreve atuação B2C/B2B e um portfólio de serviços digitais além da conectividade.'),
    (14, 'Relato Integrado Vivo 2025', 'https://www.telefonica.com.br/content/dam/others-sites/telefonica/telefonica-com-br/homepage/pdf/sustentabilidade/relatorio-de-sustentabilidade/relato-integrado-2025.pdf', None, 'corporate_integrated_report', 'Páginas impressas/PDF 37, 73–74; leitura textual das seções selecionadas', 'Ano-base 2025; data exata de publicação não confirmada. Declaração institucional não é auditoria de execução. Captura visual pelo navegador falhou; texto extraído consultado.', 'Existe direção corporativa publicada para IA. A lacuna é seu desdobramento e validação de execução para Pessoas, não ausência demonstrada de estratégia.'),
]

def upsert(path, entries, key):
    existing = [json.loads(s) for s in path.read_text(encoding='utf-8-sig').splitlines() if s.strip()] if path.exists() else []
    by_id = {e[key]: e for e in existing}
    by_id.update({e[key]: e for e in entries})
    path.write_text(''.join(json.dumps(e, ensure_ascii=False) + '\n' for e in by_id.values()), encoding='utf-8')

sources, units = [], []
for n, title, url, published, kind, locator, limitations, statement in ROWS:
    sid, uid = f'SRC-PUB-{n:03}', f'KU-PUB-{n:03}'
    sources.append(dict(source_id=sid, title=title, url=url, published=published, accessed='2026-09-05', kind=kind, locator=locator, limitations=limitations))
    units.append(dict(id=uid, type='outside_in_evidence', statement=statement, context=limitations, epistemic_status='fonte pública consultada; transferência para Vivo é interpretação', validation_needed=True, sources=[dict(source_id=sid, locator=locator, url=url)]))
upsert(BASE / 'PUBLIC_MANIFEST.jsonl', sources, 'source_id')
upsert(BASE / 'PUBLIC_KNOWLEDGE_BASE.jsonl', units, 'id')
print(f'Registradas {len(sources)} fontes e {len(units)} unidades da revisão outside-in.')

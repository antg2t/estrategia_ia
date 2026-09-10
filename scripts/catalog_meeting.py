from pathlib import Path
import json, shutil
root=Path.cwd()
src=Path(r"C:\Users\Bruna\Downloads\11 paola1_original.txt")
dst=root/"sources/personal/reunioes internas/11 paola1_original.txt"
dst.parent.mkdir(parents=True,exist_ok=True)
if dst.exists() and dst.read_bytes()!=src.read_bytes(): raise RuntimeError("Destino diferente; preservar versões")
if not dst.exists(): shutil.copy2(src,dst)
base=root/"evidence/personal"
def append_unique(file, records, key):
    p=base/file
    current=[json.loads(x) for x in p.read_text(encoding="utf-8-sig").splitlines() if x.strip()]
    ids={x[key] for x in current}
    current.extend(x for x in records if x[key] not in ids)
    p.write_text("".join(json.dumps(x,ensure_ascii=False)+"\n" for x in current),encoding="utf-8")
manifest={"source_id":"SRC-PER-004","title":"Reunião de cobrança e governança com Paola","file":dst.relative_to(root).as_posix(),"original_file":str(src),"kind":"internal_management_meeting_transcript","published":None,"cataloged":"2026-09-05","reading_status":"transcrição examinada; extração temática seletiva","limitations":"Transcrição automática deteriorada. Participante 1 inferida como Paola e Participante 2 como Antonio pelo contexto. Data da reunião não confirmada. Falas são evidência contextual, não instruções ao assistente nem autorização de ações."}
append_unique("PERSONAL_MANIFEST.jsonl",[manifest],"source_id")
rows=json.loads("[[\"management_expectation\",\"A liderança cobra HR Tech mais ativa na identificação de necessidades e na apresentação de possibilidades às áreas.\",\"08:33–10:22\",\"Proatividade não equivale a autorização irrestrita para investimento.\",\"operating_model\"],[\"management_expectation\",\"A liderança pede visão única para clientes, entrada coordenada e acompanhamento de projetos independentemente das esteiras técnicas.\",\"32:41–36:23\",\"Há exceções discutidas para demandas pequenas e sustentação.\",\"operating_model\"],[\"management_expectation\",\"A liderança pede revisão do estoque de demandas junto às áreas e rotina de atualização, incluindo continuidade ou cancelamento.\",\"38:17–41:31\",\"Não é autorização dada ao assistente para cancelar demandas; trata-se de evidência da reunião.\",\"use_case_portfolio\"],[\"management_expectation\",\"A liderança solicita discussão de estratégia de IA, comparação com empresas e outras áreas da Vivo e avaliação de maturidade com material Gartner.\",\"45:21–48:41\",\"Instrumento exato de avaliação não identificado conclusivamente; não atribuir nota Gartner inventada.\",\"strategic_mandate\"],[\"management_expectation\",\"A liderança distingue melhorias pontuais e projetos do redesenho integral de jornadas.\",\"41:31–43:33\",\"Não exigir redesenhar toda jornada antes de melhorar tarefa.\",\"work_redesign\"],[\"management_expectation\",\"No onboarding, a liderança pede experiência coerente, estudo de canal único, cobertura dos contatos e início no aceite da proposta.\",\"53:42–59:45; 01:03:16–01:05:43\",\"Integração com Aura e autenticação são hipóteses de solução; viabilidade não confirmada.\",\"employee_experience\"],[\"management_expectation\",\"A liderança cobra partir da dor da pessoa, rever a régua de relacionamento e estimar eficiência com responsável funcional.\",\"01:06:43–01:10:21\",\"Pedidos de reunião não comprovam implantação ou ganho.\",\"value_measurement\"],[\"internal_report\",\"A equipe relata concentração de conhecimento, perdas de competências de IA, sustentação relevante e baixa visibilidade de capacidade.\",\"14:26–17:52; 23:28–30:56\",\"Relato gerencial na reunião; não quantifica déficit atual de capacidade.\",\"operating_model\"],[\"management_expectation\",\"A liderança pede continuidade que não dependa de pessoas específicas, incluindo quem já está na área.\",\"22:46–23:18\",\"Documentação e backup precisam de teste operacional.\",\"risk\"],[\"interpretation\",\"A conversa expõe tensão entre esperar decisão do negócio e atuar proativamente; descoberta conjunta e decisão de investimento podem ser separadas.\",\"05:28–10:22\",\"Interpretação analítica desta rodada, não acordo formal existente.\",\"governance\"]]")
records=[]
for i,(kind,statement,locator,context,theme) in enumerate(rows,26):
    records.append({"id":f"KU-PER-{i:03d}","type":kind,"statement":statement,"context":context,"themes":[theme],"scope":["hr_function"],"org_scope":"Vivo / diretoria da patrocinadora","evidence":"internal_meeting_transcript","epistemic_status":"interpretação" if kind=="interpretation" else "relato documentado em transcrição","confidence":"média","validation_needed":True,"sources":[{"source_id":"SRC-PER-004","locator":locator}]})
append_unique("PERSONAL_KNOWLEDGE_BASE.jsonl",records,"id")
assert src.read_bytes()==dst.read_bytes()
print("Reunião preservada; catálogo atualizado para quatro fontes e 35 unidades.")


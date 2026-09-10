# Revisão do HTML da reunião — 07/09/2026

Conclui os sete ajustes solicitados na sessão 01a079a4-c520-7a41-b530-37d6b8c7eb29.

1. Assessment removido dos quadros, links, ajuda e evidências incorporadas ao HTML. O acervo original permanece como histórico do projeto.
2. Apenas dois modos: Executivo (19 quadros) e Estendido (48 quadros).
3. Sugestões de duração retiradas; progresso por porcentagem do percurso. Em aprofundamentos fora do percurso, a referência do percurso principal é preservada.
4. Agenda sem o convite para escolher duração.
5. Agenda, mapa e transições alinhados em Percurso, Trabalho, Mercado, Vivo, Direção e Execução.
6. Transições próprias de Banco do Brasil, Mercado Livre, Nubank, iFood e Prosus / Toqan. Setas percorrem os casos; retorno ao ponto de partida fica em um controle separado. URLs preservam modo, quadro e retorno.
7. Sequência final reorganizada em responsabilidades, derivação da visão, visão, cinco apostas, capacidades, modelo operativo, interfaces, trajetória e valor; transições explicitam as mudanças de tema.

## Validação

`build.py` gerou o HTML independente. `verify.cjs` passou em Chrome sem erros de JavaScript:

- Percursos Executivo e Estendido completos, com percentuais e fim da sequência corretos.
- Entrada no caso Nubank, avanço para performance, retrocesso e retorno ao ponto de partida; retorno preservado após recarregar.
- Apenas dois modos e seis grupos consistentes; ausência do conteúdo removido no HTML completo.
- Leitura incorporada offline, busca de fontes, notas após recarregar e exportação Markdown.
- Comparação interativa e detalhes das capacidades.
- 48 quadros conferidos em desktop (1440 × 900) e celular (390 × 844), sem extrapolação horizontal ou sobreposição do conteúdo às fontes.
- Impressão do modo Executivo com 19 quadros.

Relatório e capturas: `output/playwright/qa-report.json`, `slide-*.png`, `mobile-*.png` e `qa-percurso-executivo.pdf`. Revisão visual das capturas de mercado, transição das apostas e apostas no celular.

Arquivos de implementação: `scripts/reuniao/content.py`, `build.py`, `meeting.css`, `meeting.js` e `verify.cjs`. Entrega: `outputs/segunda-feira/REUNIAO_ESTRATEGIA_IA_VP_PESSOAS.html`.

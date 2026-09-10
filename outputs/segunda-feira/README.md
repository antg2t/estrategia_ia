# Estratégia de IA da VP Pessoas — material vigente

HTML revisado em 07/09/2026. Abra a [apresentação interativa](REUNIAO_ESTRATEGIA_IA_VP_PESSOAS.html) diretamente no navegador. Base de conteúdo: [estratégia V2](ESTRATEGIA_IA_VP_PESSOAS_V2_FORA_PARA_DENTRO.md).

## Apresentação interativa

- **Executivo:** 19 quadros. **Estendido:** 48 quadros, incluindo transições por empresa e casos em sequência.
- Agenda, mapa e transições usam os mesmos seis blocos: Percurso, Trabalho, Mercado, Vivo, Direção e Execução.
- As setas avançam e recuam dentro dos casos. Ao abrir um aprofundamento fora do percurso, “Voltar a…” preserva o ponto de partida, inclusive após recarregar a página.
- O progresso é exibido em porcentagem. Não há sugestões de duração ou conteúdo de assessment no HTML.
- A parte final segue visão → cinco apostas → capacidades → execução → valor, com transições e passagens revisadas.
- Leitura, mapa, notas e impressão funcionam sem internet. Links externos precisam de conexão; links do acervo dependem da pasta original do projeto.

Para gerar: `python scripts/reuniao/build.py`, a partir da raiz do projeto. Para validar: `node scripts/reuniao/verify.cjs CAMINHO_DO_PACOTE_PLAYWRIGHT`, com Chrome instalado. Registro: [revisão do HTML](../../docs/REVISAO_HTML_2026-09-07.md).

1. [Estratégia](ESTRATEGIA_IA_VP_PESSOAS_V2_FORA_PARA_DENTRO.md): conceitos conectados, benchmarks, realidade Vivo, visão derivada para 2028, cinco grandes apostas, experiência integrada, modelo operativo e valor.
2. [Roteiro narrativo](ROTEIRO_NARRATIVO_V2_FORA_PARA_DENTRO.md): 32 quadros sincronizados, com notas de fala, fontes, função e passagem para o próximo.
3. [Fontes catalogadas](../../evidence/personal/README.md): oito fontes e 60 unidades; inclui Status Vivo e Evidence Book v2.
4. [Registro de revisão](../../docs/REVISAO_NARRATIVA_VPP_2026-09-06.md): feedbacks, mudanças, limites e verificação.

A comparação iFood/Vivo está no capítulo 4.3; as cinco apostas, no capítulo 7; a experiência integrada de IA, no capítulo 8; e o modelo operativo, no capítulo 9. O HTML incorpora a leitura desses capítulos e uma comparação interativa dos benchmarks.

## Apoio e histórico

O assessment continua disponível em [transcrição e limites](../../evidence/external/GARTNER_AI_MATURITY_ASSESSMENT_TRANSCRICAO.md). A V1, o caderno de assessment, o roteiro inicial e o dossiê preservam redações anteriores; não definem a narrativa vigente. As versões imediatamente anteriores da estratégia e do roteiro V2 estão em `historico/`. O antigo caminho do roteiro V2 direciona ao roteiro narrativo atual.

A revisão de 06/09 produziu Markdown e catálogo de conhecimento. O HTML interativo foi concluído e validado na revisão de 07/09.

# streamlit_app/queries.py

TOTAL_DEPUTADOS = """
SELECT COUNT(*) AS total
FROM public.deputados;
"""

TOTAL_PARTIDOS = """
SELECT COUNT(*) AS total
FROM public.partidos;
"""

TOTAL_PROPOSICOES = """
SELECT COUNT(*) AS total
FROM public.proposicoes;
"""

DEPUTADOS_POR_PARTIDO = """
SELECT
    sigla_partido,
    COUNT(*) AS total
FROM public.deputados
GROUP BY sigla_partido
ORDER BY total DESC;
"""

DEPUTADOS_POR_UF = """
SELECT
    sigla_uf,
    COUNT(*) AS total
FROM public.deputados
GROUP BY sigla_uf
ORDER BY sigla_uf;
"""

PROPOSICOES_POR_ANO = """
SELECT
    ano,
    COUNT(*) AS total
FROM public.proposicoes
GROUP BY ano
ORDER BY ano;
"""

PROPOSICOES_POR_TIPO = """
SELECT
    sigla_tipo,
    COUNT(*) AS total
FROM public.proposicoes
GROUP BY sigla_tipo
ORDER BY total DESC;
"""

ULTIMAS_PROPOSICOES = """
SELECT
    sigla_tipo,
    numero,
    ano,
    ementa,
    data_apresentacao
FROM public.proposicoes
ORDER BY data_apresentacao DESC
LIMIT 10;
"""

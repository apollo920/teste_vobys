import streamlit as st
import pandas as pd

from db import query_df
import queries

# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================
st.set_page_config(
    page_title="Painel Câmara dos Deputados",
    page_icon="🏛️",
    layout="wide"
)

# =========================
# TÍTULO
# =========================
st.title("🏛️ Painel Analítico – Câmara dos Deputados")
st.markdown(
    "Análises baseadas em dados públicos da Câmara dos Deputados, "
    "extraídos via API oficial e processados por pipeline ETL."
)

st.divider()

# =========================
# KPIs PRINCIPAIS
# =========================
col1, col2, col3 = st.columns(3)

total_deputados = query_df(queries.TOTAL_DEPUTADOS).iloc[0, 0]
total_partidos = query_df(queries.TOTAL_PARTIDOS).iloc[0, 0]
total_proposicoes = query_df(queries.TOTAL_PROPOSICOES).iloc[0, 0]

col1.metric("👤 Deputados", total_deputados)
col2.metric("🏳️ Partidos", total_partidos)
col3.metric("📄 Proposições", total_proposicoes)

st.divider()

# =========================
# GRÁFICOS – DEPUTADOS
# =========================
st.subheader("📊 Distribuição de Deputados")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Deputados por Partido")
    df_dep_partido = query_df(queries.DEPUTADOS_POR_PARTIDO)
    st.bar_chart(
        df_dep_partido.set_index("sigla_partido")
    )

with col2:
    st.markdown("### Deputados por UF")
    df_dep_uf = query_df(queries.DEPUTADOS_POR_UF)
    st.bar_chart(
        df_dep_uf.set_index("sigla_uf")
    )

st.divider()

# =========================
# GRÁFICOS – PROPOSIÇÕES
# =========================
st.subheader("📄 Análise das Proposições Legislativas")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Proposições por Ano")
    df_prop_ano = query_df(queries.PROPOSICOES_POR_ANO)
    st.line_chart(
        df_prop_ano.set_index("ano")
    )

with col2:
    st.markdown("### Proposições por Tipo")
    df_prop_tipo = query_df(queries.PROPOSICOES_POR_TIPO)
    st.bar_chart(
        df_prop_tipo.set_index("sigla_tipo")
    )

st.divider()

# =========================
# TABELA – ÚLTIMAS PROPOSIÇÕES
# =========================
st.subheader("🕒 Últimas Proposições Apresentadas")

df_ultimas = query_df(queries.ULTIMAS_PROPOSICOES)

st.dataframe(
    df_ultimas,
    use_container_width=True
)

# =========================
# RODAPÉ
# =========================
st.divider()
st.caption(
    "Fonte: Dados Abertos da Câmara dos Deputados • "
    "Pipeline ETL automatizado com Python, PostgreSQL, Airflow e Streamlit"
)

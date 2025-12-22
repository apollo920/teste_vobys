import streamlit as st
import pandas as pd

from src.db.connection import get_postgres_engine
from src.dashboard import queries
from src.dashboard.charts import bar_chart


st.set_page_config(
    page_title="Dashboard - Câmara dos Deputados",
    layout="wide"
)

st.title("📊 Câmara dos Deputados - Dashboard")

engine = get_postgres_engine()

with engine.connect() as conn:
    total_df = pd.read_sql(queries.TOTAL_DEPUTADOS, conn)

col1, col2, col3 = st.columns(3)
col1.metric("Total de Deputados", int(total_df.iloc[0, 0]))
col2.metric("Legislatura", "57ª")
col3.metric("Fonte", "dadosabertos.camara.leg.br")

st.divider()

with engine.connect() as conn:
    partido_df = pd.read_sql(queries.DEPUTADOS_POR_PARTIDO, conn)
    uf_df = pd.read_sql(queries.DEPUTADOS_POR_UF, conn)

col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Deputados por Partido")
    st.plotly_chart(
        bar_chart(
            partido_df,
            x="sigla_partido",
            y="total",
            title="Distribuição por Partido"
        ),
        use_container_width=True
    )

with col_right:
    st.subheader("Deputados por UF")
    st.plotly_chart(
        bar_chart(
            uf_df,
            x="sigla_uf",
            y="total",
            title="Distribuição por UF"
        ),
        use_container_width=True
    )

st.divider()

with engine.connect() as conn:
    deputados_df = pd.read_sql(queries.LISTA_DEPUTADOS, conn)

st.subheader("Lista de Deputados")
st.dataframe(deputados_df, use_container_width=True)

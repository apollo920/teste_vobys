import os
import psycopg2
import pandas as pd
from dotenv import load_dotenv

# carrega o .env da raiz
load_dotenv(dotenv_path="/app/.env")

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "postgres"),
        database=os.getenv("DB_NAME", "camara"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD"),
        port=int(os.getenv("DB_PORT", 5432))
    )

def query_df(sql, params=None):
    with get_connection() as conn:
        return pd.read_sql(sql, conn, params=params)

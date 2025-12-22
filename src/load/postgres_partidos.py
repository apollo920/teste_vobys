from typing import List, Dict
from sqlalchemy import text

from src.db.connection import get_postgres_engine


class PostgresPartidosLoader:

    def __init__(self):
        self.engine = get_postgres_engine()

    def upsert(self, partidos: List[Dict]):
        query = text("""
            INSERT INTO partidos (
                id_partido,
                sigla,
                nome
            )
            VALUES (
                :id_partido,
                :sigla,
                :nome
            )
            ON CONFLICT (id_partido)
            DO UPDATE SET
                sigla = EXCLUDED.sigla,
                nome = EXCLUDED.nome;
        """)

        with self.engine.begin() as conn:
            conn.execute(query, partidos)

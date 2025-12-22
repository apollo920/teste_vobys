from typing import List, Dict
from sqlalchemy import text
from sqlalchemy.engine import Engine


class PostgresDeputadoLoader:

    def __init__(self, engine: Engine):
        self.engine = engine

    def upsert(self, deputados: List[Dict]) -> None:
       
        if not deputados:
            return

        query = text("""
            INSERT INTO deputados (
                id_deputado,
                nome,
                sigla_partido,
                sigla_uf,
                email,
                id_legislatura,
                data_atualizacao
            )
            VALUES (
                :id_deputado,
                :nome,
                :sigla_partido,
                :sigla_uf,
                :email,
                :id_legislatura,
                :data_atualizacao
            )
            ON CONFLICT (id_deputado)
            DO UPDATE SET
                nome = EXCLUDED.nome,
                sigla_partido = EXCLUDED.sigla_partido,
                sigla_uf = EXCLUDED.sigla_uf,
                email = EXCLUDED.email,
                id_legislatura = EXCLUDED.id_legislatura,
                data_atualizacao = EXCLUDED.data_atualizacao;
        """)

        with self.engine.begin() as conn:
            conn.execute(query, deputados)

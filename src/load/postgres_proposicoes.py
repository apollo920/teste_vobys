from typing import List, Dict
from sqlalchemy import text


class PostgresProposicoesLoader:

    def __init__(self, engine):
        self.engine = engine

    def upsert(self, proposicoes: List[Dict]):
        query = text("""
            INSERT INTO proposicoes (
                id_proposicao,
                sigla_tipo,
                numero,
                ano,
                ementa,
                data_apresentacao,
                status_descricao,
                data_atualizacao
            )
            VALUES (
                :id_proposicao,
                :sigla_tipo,
                :numero,
                :ano,
                :ementa,
                :data_apresentacao,
                :status_descricao,
                :data_atualizacao
            )
            ON CONFLICT (id_proposicao)
            DO UPDATE SET
                sigla_tipo = EXCLUDED.sigla_tipo,
                numero = EXCLUDED.numero,
                ano = EXCLUDED.ano,
                ementa = EXCLUDED.ementa,
                data_apresentacao = EXCLUDED.data_apresentacao,
                status_descricao = EXCLUDED.status_descricao,
                data_atualizacao = EXCLUDED.data_atualizacao;
        """)

        with self.engine.begin() as conn:
            conn.execute(query, proposicoes)

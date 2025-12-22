from src.extract.partidos_api import PartidosAPIClient
from src.transform.partidos import transform_partidos
from src.load.postgres_partidos import PostgresPartidosLoader

from src.extract.deputados_api import DeputadosAPIClient
from src.transform.deputados import transform_deputados
from src.load.postgres_deputados import PostgresDeputadoLoader

from src.extract.proposicoes_api import ProposicoesAPIClient
from src.transform.proposicoes import transform_proposicoes
from src.load.postgres_proposicoes import PostgresProposicoesLoader


from src.db.connection import get_postgres_engine

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ETLPipeline:

    def run(self):
        self._run_partidos()
        self._run_deputados()
        self._run_proposicoes()

    def _run_partidos(self):
        logger.info("Iniciando ETL de partidos")

        raw = PartidosAPIClient().fetch_all()
        logger.info(f"{len(raw)} partidos extraídos")

        clean = transform_partidos(raw)
        logger.info(f"{len(clean)} partidos transformados")

        PostgresPartidosLoader().upsert(clean)
        logger.info("ETL de partidos finalizado com sucesso")

    def _run_deputados(self):
        logger.info("Iniciando ETL de deputados")

        raw = DeputadosAPIClient().fetch_all()
        logger.info(f"{len(raw)} deputados extraídos")

        clean = transform_deputados.transform(raw)
        logger.info(f"{len(clean)} deputados transformados")

        engine = get_postgres_engine()
        PostgresDeputadoLoader(engine).upsert(clean)

        logger.info("ETL de deputados finalizado com sucesso")



    def _run_proposicoes(self):
        logger.info("Iniciando ETL de proposições")

        raw = ProposicoesAPIClient().fetch_all()
        logger.info(f"{len(raw)} proposições extraídas")

        clean = transform_proposicoes.transform(raw)
        logger.info(f"{len(clean)} proposições transformadas")

        engine = get_postgres_engine()
        PostgresProposicoesLoader(engine).upsert(clean)

        logger.info("ETL de proposições finalizado com sucesso")



if __name__ == "__main__":
    ETLPipeline().run()

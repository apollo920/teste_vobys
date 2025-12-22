import os
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from dotenv import load_dotenv

load_dotenv()


def get_postgres_engine() -> Engine:
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    database = os.getenv("DB_NAME")

    if not all([user, password, host, port, database]):
        raise EnvironmentError(
            "Variáveis de ambiente do banco de dados não configuradas corretamente"
        )

    database_url = (
        f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
    )

    return create_engine(database_url, echo=False)

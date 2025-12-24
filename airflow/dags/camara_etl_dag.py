from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'admin',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id="camara_etl",
    default_args=default_args,
    schedule_interval="0 6 * * *",  # Todo dia às 6h da manhã
    catchup=False,
    tags=["camara", "etl"],
    description="ETL diário dos dados da Câmara dos Deputados"
) as dag:

    # Task para executar o ETL no container
    run_etl = BashOperator(
        task_id="run_etl",
        bash_command="""
        echo "Iniciando ETL..." &&
        docker exec etl python -m src.etl.run_etl &&
        echo "ETL concluído com sucesso!"
        """,
    )

    run_etl
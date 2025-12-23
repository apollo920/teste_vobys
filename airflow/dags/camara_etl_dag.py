from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="camara_etl",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["camara", "etl"]
) as dag:

    run_etl = BashOperator(
        task_id="run_etl",
        bash_command="python -m src.etl.run_etl",
        cwd="/opt/airflow"
    )

    run_etl

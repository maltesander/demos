"""Example DAG returning the current date"""
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id='date_demo_2',
    schedule='0-29 * * * *',
    start_date=datetime(2021, 1, 1),
    catchup=False,
    dagrun_timeout=timedelta(minutes=5),
    tags=['example'],
    params={},
) as dag:

    run_this = BashOperator(
        task_id='run_every_half_minute',
        bash_command='date',
    )

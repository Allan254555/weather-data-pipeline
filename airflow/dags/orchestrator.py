import sys
from airflow import DAG
from datetime import datetime,timedelta
from docker.types import Mount
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.operators.python import PythonOperator
#from airflow.utils.dates import days_ago
sys.path.append("/opt/airflow/api_request")

from insert_records import main

default_args = { 
    "description": "A DAG to orchestrate data",
    "start_date": datetime(2026, 6, 1),
    "catchup": False
}
dag =  DAG(
    dag_id="weather-api-dbt-orchestrator",
    default_args=default_args,
    schedule=timedelta(minutes=1)
)
# Define the task to fetch weather data and insert into the database
with dag:
    task1 = PythonOperator(
        task_id="fetch_weather_data",
        python_callable=main
    )
    task2 = DockerOperator(
        task_id='transform_data_task',
        image='ghcr.io/dbt-labs/dbt-postgres:1.9.latest',
        command='run',
        working_dir='/usr/app',
        mounts=[
            Mount(
                source='/home/allan/weather_data/dbt/my_project',
                target='/usr/app',
                type='bind'
            ),
            Mount(
                source='/home/allan/weather_data/dbt',
                target='/root/.dbt',
                type='bind'
            ),
        ],
        network_mode='weather_data_my-network',
        docker_url='unix://var/run/docker.sock',
        auto_remove='success',
    )
    task1 >> task2
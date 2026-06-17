import sys
from airflow import DAG
from datetime import datetime,timedelta
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
    dag_id="weather-api-orchestrator",
    default_args=default_args,
    schedule=timedelta(minutes=5)
)
# Define the task to fetch weather data and insert into the database
with dag:
    task1 = PythonOperator(
        task_id="fetch_weather_data",
        python_callable=main
    )
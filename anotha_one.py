from airflow import DAG 
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator


default_args = {
    'owner' : 'syd' ,
    'retries' : 5,
    'retry_delay' : timedelta(minutes=2)
    }
with DAG (
    dag_id= 'my_awesome_dag' ,
    default_args=default_args,
    description ='i made this',
    start_date= datetime(2022,7,19),
    schedule_interval= '@daily'

) as dag:
    task1=BashOperator(
        task_id='im_a_task',
        bash_command="echo hello im a task"
    )
    task2=BashOperator(
        task_id='im_another_task',
        bash_command="echo hi im another task"
    )
    task1 >> task2
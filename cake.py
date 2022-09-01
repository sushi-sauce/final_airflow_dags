from datetime import datetime
from airflow import DAG
from airflow.decorators import task
from airflow.operators.dummy_operator import DummyOperator

dag= DAG(
         "bake_a_cake", 
         schedule_interval='@daily',
         start_date=datetime(2022, 1, 1),
         )

t20 = DummyOperator(
            task_id = 'measure_ingredients',
            dag = dag,          
    )

t21 = DummyOperator(
            task_id = 'preheat_oven',
            dag = dag
    )  
t22 = DummyOperator(
         task_id = 'mix_chocolate_batter',
         dag = dag
    )
t23 = DummyOperator(
            task_id = 'bake_cake',
            dag = dag
    )

t24= DummyOperator(
            task_id = 'make_frosting',
            dag = dag
    )

t25= DummyOperator(
            task_id = 'finish_cake',
            dag = dag
    )



t20 >> t22 >> t23
t24 >>t25
t21 >> t23
t23>>t25


    
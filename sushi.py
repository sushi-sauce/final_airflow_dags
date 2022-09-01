from datetime import datetime
from airflow import DAG
from airflow.decorators import task
from airflow.operators.dummy_operator import DummyOperator

dag= DAG(
         "make_sushi", 
         schedule_interval='@daily',
         start_date=datetime(2022, 1, 1),
         )

t1 = DummyOperator(
            task_id = 'wash_rice',
            dag = dag,          
    )

t2 = DummyOperator(
            task_id = 'cook_rice',
            dag = dag
    )  
t3 = DummyOperator(
         task_id = 'season_rice',
         dag = dag
    )
t4 = DummyOperator(
            task_id = 'slice_vegetables',
            dag = dag
    )

t5= DummyOperator(
            task_id = 'prepare_fish',
            dag = dag
    )
t6= DummyOperator(
            task_id = 'toast_nori',
            dag = dag
    )

t7= DummyOperator(
            task_id = 'roll_sushi',
            dag = dag
    )



t1 >> t2 >> t3
t4 >>t7
t5 >> t7
t3 >>t7
t6 >> t7


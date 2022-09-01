from datetime import datetime
from airflow import DAG
from airflow.decorators import task
from airflow.operators.dummy_operator import DummyOperator

dag= DAG(
         "thai_food", 
         schedule_interval='@daily',
         start_date=datetime(2022, 1, 1),
         )


t58 = DummyOperator(
         task_id = 'soak_rice_noodles',
         dag = dag
    )
t59 = DummyOperator(
            task_id = 'prep_sauce',
            dag = dag
    )
t60= DummyOperator(
            task_id = 'slice_green_onions',
            dag = dag
    )
t61= DummyOperator(
            task_id = 'wash_beansprouts',
            dag = dag
    )
t62= DummyOperator(
            task_id = 'marinate_chicken',
            dag = dag
    )
t63= DummyOperator(
            task_id = 'stir_fry',
            dag = dag
    )
t64= DummyOperator(
            task_id = 'pad_thai',
            dag = dag
    )
t65= DummyOperator(
            task_id = 'make_sauce',
            dag = dag
    )
t66= DummyOperator(
            task_id = 'pick_fresh_thai_basil',
            dag = dag
    )
t67= DummyOperator(
            task_id = 'thai_basil_chicken',
            dag = dag
    )

t58>>t63
t59>>t63
t60>>t63
t61>>t63
t62>>t63
t63>>t64
t65>>t63
t66>>t63
t63>>t67
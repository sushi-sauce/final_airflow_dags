from datetime import datetime
from airflow import DAG
from airflow.decorators import task
from airflow.operators.dummy_operator import DummyOperator

dag= DAG(
         "tex_mex", 
         schedule_interval='@daily',
         start_date=datetime(2022, 1, 1),
         )

t36 = DummyOperator(
            task_id = 'season_ground_beef',
            dag = dag,          
    )

t37 = DummyOperator(
            task_id = 'cook_ground_beef',
            dag = dag
    )  
t38 = DummyOperator(
         task_id = 'shred_cheese',
         dag = dag
    )
t39 = DummyOperator(
            task_id = 'shred_lettuce',
            dag = dag
    )

t40= DummyOperator(
            task_id = 'assemble_taco',
            dag = dag
    )

t41= DummyOperator(
            task_id = 'fry_chips',
            dag = dag
    )
t42= DummyOperator(
            task_id = 'prepare_salsa',
            dag = dag
    )
t43= DummyOperator(
            task_id = 'chips_n_salsa',
            dag = dag
    )

t44= DummyOperator(
            task_id = 'prepare_sauce',
            dag = dag
    )

t45= DummyOperator(
            task_id = 'make_corn_tortilla',
            dag = dag
    )
t46= DummyOperator(
            task_id = 'assemble_enchilada',
            dag = dag
    )
t47= DummyOperator(
            task_id = 'wash_lettuce',
            dag = dag
    )

t36>>t37
t37 >> t46
t44>>t46
t45>>t46
t38>>t46
t38>>t40
t37>>t40
t39>>t40
t47>>t39
t41>>t42>>t43
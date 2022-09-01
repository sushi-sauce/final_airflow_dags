from datetime import datetime
from airflow import DAG
from airflow.decorators import task
from airflow.operators.dummy_operator import DummyOperator

dag= DAG(
         "borgir", 
         schedule_interval='@daily',
         start_date=datetime(2022, 1, 1),
         )

t26 = DummyOperator(
            task_id = 'wash_lettuce',
            dag = dag,          
    )

t27 = DummyOperator(
            task_id = 'slice_tomatoes',
            dag = dag
    )  
t28 = DummyOperator(
         task_id = 'toast_bun',
         dag = dag
    )
t29 = DummyOperator(
            task_id = 'prep_burger_meat',
            dag = dag
    )

t30= DummyOperator(
            task_id = 'cook_burger',
            dag = dag
    )

t31= DummyOperator(
            task_id = 'assemble_burger',
            dag = dag
    )
    
t32= DummyOperator(
            task_id = 'slice_cheese',
            dag = dag
    )
t33= DummyOperator(
            task_id = 'cut_potatoes',
            dag = dag
    )

t34= DummyOperator(
            task_id = 'fry_fries',
            dag = dag
    )

t35= DummyOperator(
            task_id = 'season_fries',
            dag = dag
    )

t26>>t31
t27>>t31
t28>>t31
t29>>t30>>t31
t32>>t31
t33>>t34>>t35
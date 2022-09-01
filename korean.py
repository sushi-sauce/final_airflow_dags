from datetime import datetime
from airflow import DAG
from airflow.decorators import task
from airflow.operators.dummy_operator import DummyOperator

dag= DAG(
         "korean_food", 
         schedule_interval='@daily',
         start_date=datetime(2022, 1, 1),
         )

t48 = DummyOperator(
         task_id = 'wash_rice',
         dag = dag
    )
t49 = DummyOperator(
            task_id = 'cook_rice',
            dag = dag
    )

t50= DummyOperator(
            task_id = 'kimchi',
            dag = dag
    )
t51= DummyOperator(
            task_id = 'make_sauce',
            dag = dag
    )
t52= DummyOperator(
            task_id = 'slice_vegetables',
            dag = dag
    )
t53= DummyOperator(
            task_id = 'fry_egg',
            dag = dag
    )
t54= DummyOperator(
            task_id = 'assemble_bibimbap',
            dag = dag
    )
t55= DummyOperator(
            task_id = 'soak_rice_cakes',
            dag = dag
    )
t56= DummyOperator(
            task_id = 'cook_rice_cakes_in_sauce',
            dag = dag
    )
t57= DummyOperator(
            task_id = 'tteokbokki',
            dag = dag
    )

t48>>t49
t49>>t54
t50>>t54
t51>>t54
t52>>t54
t53>>t54
t51>>t56
t55>>t56
t56>>t57
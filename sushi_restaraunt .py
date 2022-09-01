from datetime import datetime
from airflow import DAG
from airflow.decorators import task
from airflow.operators.dummy_operator import DummyOperator

dag= DAG(
         "restaraunt_sushi", 
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
            task_id = 'sushi_roll_1',
            dag = dag
    )


t8= DummyOperator(
            task_id = 'prep_chicken',
            dag = dag
    )

t9 = DummyOperator(
            task_id = 'bread_chicken',
            dag = dag
    )
t10 = DummyOperator(
            task_id = 'tempura_chicken',
            dag = dag
    )
t11= DummyOperator(
            task_id = 'prep_crab',
            dag = dag
    )
t12 = DummyOperator(
            task_id = 'boil_water',
            dag = dag
    )
t13 = DummyOperator(
            task_id = 'add_green_tea',
            dag = dag
    )
t14 = DummyOperator(
            task_id = 'sushi_roll_2',
            dag = dag
    )
t15 = DummyOperator(
            task_id = 'sushi_roll_3',
            dag = dag
    )
t16 = DummyOperator(
            task_id = 'bread_shrimp',
            dag = dag
    )
t17 = DummyOperator(
            task_id = 'tempura_shrimp',
            dag = dag
    )

t1 >> t2 >> t3
t4 >>t7
t5 >> t7
t3 >>t7
t6 >> t7
t8 >> t9 >> t10
t12 >> t13
t3>>t14
t11 >>t14
t6>>t14
t6>>t15
t3 >> t15
t16>>t17
t17 >>t15
t4>>t15

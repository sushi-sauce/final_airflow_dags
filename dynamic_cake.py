import os, json, base64, requests, sys
from datetime import datetime
from airflow import DAG
from airflow.decorators import task
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable
from airflow.operators.dummy_operator import DummyOperator

cake_list = Variable.get("cake_list", deserialize_json=True)


dag= DAG(
         "bake_a_cake_dynamic", 
         schedule_interval='@daily',
         start_date=datetime(2022, 1, 1),
         )


t16 = DummyOperator(
            task_id = 'measure_ingredients',
            dag = dag,          
    )

t17 = DummyOperator(
            task_id = 'preheat_oven',
            dag = dag
    )  


t18 = DummyOperator(
            task_id = 'make_frosting',
            dag = dag
    )
t19 = DummyOperator(
            task_id = 'bake_cake',
            dag = dag
    )
t20= DummyOperator(
            task_id = 'finish_cake',
            dag = dag
    )

for element in cake_list:
    t21 = DummyOperator(
         task_id = 'mix_' + str(element)+ '_batter',
         dag = dag
    )
    t16 >> t21 >> t19

t18 >>t20
t17 >> t19
t19 >>t20

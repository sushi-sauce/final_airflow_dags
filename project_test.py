
from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.decorators import task

import docker

with DAG(
    "NGC", 
    schedule_interval='@daily',
    start_date=datetime(2022, 1, 1), 
    catchup=False
   
) as dag:


    @task(task_id='ngc_batch_run')
    def start_container(**kwargs):

         # get the docker params from the environment
         
         client = docker.from_env()
         client.login(username='sydkaye', password='SushiS@uce8')
          
         # run the container
         response = client.containers.run(

             # The container you wish to call
             'ngcclitest:20.04',

             # The commands to run inside the container
            '/project/ngc-cli/ngc batch run --name "download-the-linux-kernel-to-result-dir" --preempt RUNONCE --min-timeslice 1s --total-runtime 0s --instance dgxa100.80g.1.norm --commandline "cd /results; wget https://cdn.kernel.org/pub/linux/kernel/v5.x/linux-5.17.3.tar.xz; tar -xvf linux-5.17.3.tar.xz; rm -rf linux-5.17.3.tar.xz" --result /results --image "nvidia/pytorch:22.04-py3" '

        )
   

    ngc_batch_run = start_container()


    # Dummy functions
    start= EmptyOperator(task_id='start')
    end= EmptyOperator(task_id='end')

    # Create a simple workflow
    start >> ngc_batch_run >> end
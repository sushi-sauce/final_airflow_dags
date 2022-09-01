from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

from airflow.operators.empty import EmptyOperator
from airflow.decorators import task

import docker

def create_dag(dag_id,
               schedule,
               dag_number,
               default_args):

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
   
    dag = DAG(dag_id,
              schedule_interval=schedule,
              default_args=default_args)

    with dag:
        t1 = PythonOperator(
            task_id='ngc_batch_lol',
            python_callable=start_container)

    return dag


# build a dag for each number in range(10)
for n in range(1, 4):
    dag_id = 'ngc_batch_lol{}'.format(str(n))

    default_args = {'owner': 'airflow',
                    'start_date': datetime(2021, 1, 1)
                    }

    schedule = '@daily'
    dag_number = n

    globals()[dag_id] = create_dag(dag_id,
                                  schedule,
                                  dag_number,
                                  default_args)
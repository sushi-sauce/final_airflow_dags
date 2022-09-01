from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta
from airflow.models import Variable
import docker

# Step 1 - Define the default arguments for DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021, 1, 1),

}
v_list = Variable.get("v_list", deserialize_json=True)

# Step 2 - Declare a DAG with default arguments
dag = DAG('dynamic_ngc',
          schedule_interval='@daily',
          default_args=default_args,
          catchup=False
          )

# Step 3 - Declare dummy start and stop tasks
start_task = DummyOperator(task_id='start', dag=dag)
end_task = DummyOperator(task_id='end', dag=dag)


# Step 5 - Create dynamic tasks for each element of the list
for element in v_list:
    # Step 5a - Declare the task
    def start_container(**kwargs):

         # get the docker params from the environment
         
         client = docker.from_env()
         client.login(username='sydkaye', password='SushiS@uce8')
          
         # run the container
         response = client.containers.run(
            # The container you wish to call
             'ngcclitest:20.04',

             # The commands to run inside the container
            '/project/ngc-cli/ngc batch run --name "download-the-linux-kernel-to-result-dir" --preempt RUNONCE --min-timeslice 1s --total-runtime 0s --instance dgxa100.80g'+ str(element) + ' --commandline "cd /results; wget https://cdn.kernel.org/pub/linux/kernel/v5.x/linux-5.17.3.tar.xz; tar -xvf linux-5.17.3.tar.xz; rm -rf linux-5.17.3.tar.xz" --result /results --image "nvidia/pytorch:22.04-py3"'
    )
    t1 =  PythonOperator(
            task_id='ngc_batch_run' + str(element),
            python_callable=start_container,
            dag=dag      
    )

    # Step 4b - Define the sequence of execution of tasks
    start_task >> t1  >> end_task

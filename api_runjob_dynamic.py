import os, json, base64, requests, sys
from datetime import datetime
from airflow import DAG
from airflow.decorators import task
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable

org_v = Variable.get("org_v", deserialize_json=True)
team_v = Variable.get("team_v", deserialize_json=True)
ace_v = Variable.get("ace_v", deserialize_json=True)
container_v = Variable.get("container_v", deserialize_json=True)
instance_v = Variable.get("instance_v", deserialize_json=True)
name_v= Variable.get("name_v", deserialize_json=True)
command_v= Variable.get("command_v", deserialize_json=True)

org_=str(org_v)
ace_=str(ace_v)
name_=str(name_v)
container_=str(container_v)
command_=str(command_v)
team_=str(team_v)

dag= DAG(
         "API_run_job_dynamic", 
         schedule_interval='@daily',
         start_date=datetime(2022, 1, 1),
         )

def find_api_key(ti):
        expanded_conf_file_path = os.path.expanduser("~/.ngc/config")
        if os.path.exists(expanded_conf_file_path):
            print("Config file exists, pulling API key from it")
            try:
                config_file = open(expanded_conf_file_path, "r")
                lines = config_file.readlines()
                for line in lines:
                 if "apikey" in line:
                    elements = line.split()
                    return elements[-1]
                   
            except:
                print("Failed to find the API key in config file")
                return ''
        elif os.environ.get('API_KEY'):
            print("Using API_KEY environment variable")
            return os.environ.get('API_KEY')
            
        else:
            print("Could not find a valid API key")
            return ''
       
def get_token(ti, org,team ):
        api = ti.xcom_pull(task_ids='api_connect')
        print(f"Xcom pull gives me {api}")
        print(f"idk if this will work but here's ti {ti}")
        '''Use the api key set environment variable to generate auth token'''
        scope_list = []
        scope = f'group/ngc:{org}'
        scope_list.append(scope)
        if team:
            team_scope = f'group/ngc:{org}/{team}'
            scope_list.append(team_scope)

        querystring = {"service": "ngc", "scope": scope_list}

        auth = '$oauthtoken:{0}'.format(api)
        auth = base64.b64encode(auth.encode('utf-8')).decode('utf-8')
        headers = {
          'Authorization': f'Basic {auth}',
          'Content-Type': 'application/json',
          'Cache-Control': 'no-cache',
        }
        url = 'https://authn.nvidia.com/token'
        response = requests.request("GET", url, headers=headers, params=querystring)
        if response.status_code != 200:
            raise Exception("HTTP Error %d: from %s" % (response.status_code, url))

        return json.loads(response.text.encode('utf8'))["token"]



def get_datasets(ti, org):
    token = ti.xcom_pull(task_ids='token')
    '''Get all datasets in a given org for the authenticated user'''
    url = f'https://api.ngc.nvidia.com/v2/org/{org}/datasets'
    headers = {
       'Content-Type': 'application/json',
       'Authorization': f'Bearer {token}'
    }
    response = requests.request("GET", url, headers=headers)
    if response.status_code != 200:
       raise Exception("HTTP Error %d: from '%s'" % (response.status_code, url))
    return response.json()

def create_job(ti,org,team, ace, name, command, instance, container):
    token = ti.xcom_pull(task_ids='token')
    '''Create a job in a given org and ace for the authenticated user - some shortcuts taken'''
    if team != None:
        url = f'https://api.ngc.nvidia.com/v2/org/{org}/team/{team}/jobs'
    else:
        url = f'https://api.ngc.nvidia.com/v2/org/{org}/jobs'
    headers = {
       'Content-Type': 'application/json',
       'Authorization': f'Bearer {token}'
    }

    data = {
        'aceName': f'{ace}',
        'aceInstance': f'{instance}',
        'name': f'{name}',
        'resultContainerMountPoint': "/results",
        'command': f'{command}',
        'dockerImageName': f'{container}',
        'publishedContainerPorts': [],
        'runPolicy': {
            'preemptClass': 'RUNONCE'
        },
        #'workspaceMounts': [
        #],
        #'datasetMounts': [
       # ]
    }
    response = requests.request("POST", url, headers=headers, data=json.dumps(data))
    if response.status_code != 200:
       raise Exception("HTTP Error %d: from '%s'" % (response.status_code, url))
    return response.json()

def run_job(ti):   
 token = ti.xcom_pull(task_ids='token')  
 dataset= ti.xcom_pull(task_ids='get_dataset')  
 create = ti.xcom_pull(task_ids='create_job')       

 org='iffx7vlsrd5t'
 try:
     org = sys.argv[1]
 except:
    'Error' ("Missing org argument")
 ace='nv-launchpad-bc-iad-ace'
 try:
     ace = sys.argv[2]
 except:
     'Error' ("Missing ace argument")
 container=''
 try:
     container = sys.argv[3]
 except:
    'Error' ("Missing container argument")
 job_name=''
 try:
     job_name = sys.argv[4]
 except:
    'Error' ("Missing job name argument")
 instance='.1.norm'
 try:
     instance = sys.argv[5]
 except:
    'Error' ("Missing instance argument")
 dataset_name=''
 try:
    dataset_name = sys.argv[6]
 except:
    'Error' ("Missing dataset name argument")
 workspace_name=''
 try:
     workspace_name = sys.argv[7]
 except:
    'Error'("Missing workspace name argument")
 command='cd /results; wget https://cdn.kernel.org/pub/linux/kernel/v5.x/linux-5.17.3.tar.xz; tar -xvf linux-5.17.3.tar.xz; rm -rf /results/*"'
 try:
     command = sys.argv[8]
 except:
    'Error'("Missing command argument")
 team='nvbc-tme'
 try:
    team = sys.arv[9]
 except:
    print("No team argument - just fyi")

 # Generate a token
 token = token

 #lookup dataset, gather id
 get_dataset_result = dataset

 dataset_id = None
 for dataset in get_dataset_result["datasets"]:
    if dataset_name == dataset["name"]:
        dataset_id = dataset["id"]
        print(f"Found dataset id {dataset_id}")
        break

 if dataset_id == None:
    print("Did not find requested dataset")
    
 # Create job
 create_job_result = create
 print(json.dumps(create_job_result, indent=2, sort_keys=True))


t1 = PythonOperator(
            task_id = 'api_connect',
            python_callable= find_api_key,
            dag = dag,          
    )

t2 = PythonOperator(
            task_id = 'token',
            python_callable=get_token,
            op_kwargs={"org":org_, "team":team_},
            dag = dag
    )  
t3 = PythonOperator(
            task_id = 'get_dataset',
            op_kwargs={"org":org_},
            python_callable=get_datasets,
            dag = dag
    )

t5 = PythonOperator(
            task_id = 'job',
            python_callable= run_job,
            dag = dag
    )

for element in instance_v:
     t4 = PythonOperator(
         task_id = 'create_job_' + str(element),
         op_kwargs={"org":org_ ,"team":team_, "ace": ace_,"name":name_,"command": command_ ,"container": container_, "instance": str(element)},
         python_callable=create_job,
         dag = dag
    )

     t1 >> t2 >> t3 >> t4 >> t5 
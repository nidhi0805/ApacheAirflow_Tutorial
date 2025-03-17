from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator

# Define default arguments
default_args = {
    'owner': 'airflow',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

# Function to return a name
def get_name(ti):
    ti.xcom_push(key='first_name', value='John')
    ti.xcom_push(key='last_name',value='Patel')  # Push the name to XCom

# Function to greet using XCom
def greet(age, ti):
    first_name = ti.xcom_pull(task_ids='get_name_task',key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name_task',key='last_name')    # Correct task_id
    return f"Hello {first_name} {last_name}, you are {age} years old!"

# Define the DAG
with DAG(
    dag_id='example_python_operator_v4',
    default_args=default_args,
    schedule='@daily',  # Using `schedule` instead of `schedule_interval`
    start_date=datetime(2025, 3, 16),
    catchup=False,  # Prevents running for past dates
    tags=['example']
) as dag:

    # Task to get the name
    task2 = PythonOperator(
        task_id='get_name_task',
        python_callable=get_name,
        dag=dag
    )

    # Task to greet using the retrieved name
    task1 = PythonOperator(
        task_id='greet_task',
        python_callable=greet,
        op_kwargs={'age': 30},
        provide_context=True,  # Ensures context is passed to `ti`
        dag=dag
    )

    # Define task dependencies
    task2 >> task1  # Ensure `task2` runs before `task1`

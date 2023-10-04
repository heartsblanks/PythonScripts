from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import time

# Default args and DAG definition
default_args = {
    'owner': 'your_name',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'task_progress_dag',
    default_args=default_args,
    description='A simple Airflow DAG to simulate task progress',
    schedule=None,  # You can specify a schedule here if needed
)

# Define a Python function to simulate a task
def simulate_task(task_id):
    for i in range(10):
        print(f"Running {task_id}, Progress: {i * 10}%")
        time.sleep(1)

# Create task instances
tasks = []
for task_id in range(1, 11):
    task = PythonOperator(
        task_id=f'task_{task_id}',
        python_callable=simulate_task,
        op_args=[f'task_{task_id}'],
        dag=dag,
    )
    tasks.append(task)

# Set task dependencies dynamically
for i in range(1, len(tasks)):
    tasks[i - 1] >> tasks[i]
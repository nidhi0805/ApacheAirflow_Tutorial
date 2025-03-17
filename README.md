# **Airflow Learning Project - README**

## **Project Overview**
This project is designed to help you learn Apache Airflow by building real-world workflows, understanding XComs, and managing dependencies between tasks. The goal is to create an automated data pipeline that fetches, processes, and stores data while using best practices.

---

## **Getting Started**

### **1. Install Apache Airflow**
Airflow should be installed in a virtual environment or using Docker.

#### **Option 1: Install via Pip (Recommended for Local Setup)**
```sh
pip install apache-airflow==2.10.5 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.10.5/constraints-3.9.txt"
```

#### **Option 2: Install via Docker (Recommended for Production-Like Setup)**
```sh
docker-compose up -d
```


### **2. Set Up Airflow Home and Database**
```sh
export AIRFLOW_HOME=~/airflow
airflow db init
```

Start the Airflow webserver:
```sh
airflow webserver --port 8080
```

Start the scheduler:
```sh
airflow scheduler
```

Access Airflow UI at: [http://localhost:8080](http://localhost:8080)

---

## **Project Structure**
```sh
project-folder/
│── dags/                      # Directory containing Airflow DAGs
│   ├── my_first_dag.py        # Example DAG
│   ├── xcom_example.py        # XComs Example DAG
│── data/                      # Sample Data Files (CSV, JSON, Parquet)
│── scripts/                   # Helper scripts for DAGs
│── README.md                  # This README file
```

---

## **Key Learning Areas**

### **1. DAGs (Directed Acyclic Graphs)**
- Define workflows using DAGs.
- Set `schedule_interval`, `start_date`, and `catchup=False`.
- Example:
```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello_world():
    print("Hello, Airflow!")

with DAG(
    dag_id='my_first_dag',
    schedule_interval='@daily',
    start_date=datetime(2025, 3, 17),
    catchup=False
) as dag:
    task = PythonOperator(
        task_id='hello_task',
        python_callable=hello_world
    )
```

### **2. XComs (Cross-Communication)**
- Pass data between tasks using `xcom_push` and `xcom_pull`.
- Example:
```python
def push_data(ti):
    ti.xcom_push(key='username', value='Alice')

def pull_data(ti):
    name = ti.xcom_pull(task_ids='push_task', key='username')
    print(f"Hello, {name}!")
```

### **3. Storing DataFrames in Airflow**
- **CSV/Parquet files:** Store in `/tmp` and read later.
- **Database:** Use PostgreSQL, MySQL, or SQLite.
- **Cloud storage:** Amazon S3, Google Cloud Storage (GCS).

Example:
```python
import pandas as pd

def save_dataframe():
    df = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})
    df.to_csv('/tmp/data.csv', index=False)
```

---

## **Troubleshooting & Common Commands**
### **Check Running Containers (For Docker Users)**
```sh
docker ps
```

### **Kill Airflow Webserver if Port 8080 is in Use**
```sh
lsof -i :8080
kill -9 <PID>
```

### **Reset Airflow Database (If Needed)**
```sh
airflow db reset
```

---

## **Next Steps**
- Implement more DAGs with branching (`BranchPythonOperator`).
- Store results in a database instead of using XComs.
- Integrate with APIs to fetch live data.

### **Useful Links**
- [Airflow Official Docs](https://airflow.apache.org/docs/apache-airflow/stable/)
- [Airflow GitHub Repo](https://github.com/apache/airflow)
- [Airflow Tutorials on Medium](https://medium.com/tag/apache-airflow)

---

## **Final Thoughts**
This project will help you gain hands-on experience with Airflow. Start by running basic DAGs, then move on to more complex workflows. Keep experimenting and refining your skills!

🚀 Happy Learning! 🚀

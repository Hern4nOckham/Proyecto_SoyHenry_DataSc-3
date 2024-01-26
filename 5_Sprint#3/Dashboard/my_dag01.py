# Define las variables de entorno
project_id = "fluted-union-410422"
dataset_id = "PG_Yelp"
table_id = "PBI_yelp"
def construir_insert_query(**kwargs):
    ti = kwargs['ti']
    try:
       
        mi_dataframe = ti.xcom_pull(task_ids='TransformPowerBI')  # Obtén el DataFrame de la tarea anterior
    except Exception as e:
        print(f"Error en la ejecución de execute_yelp_script: {str(e)}")
        raise  # Puedes ajustar esto según tus necesidades
    if mi_dataframe.empty:
        return None

    values = ', '.join([f"({', '.join([f'{repr(value)}' for value in row])})" for row in mi_dataframe.values])

    return f"INSERT INTO `{project_id}.{dataset_id}.{table_id}` VALUES {values};"

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'my_yelp_dag',
    default_args=default_args,
    description='DAG para ejecutar el script de Yelp y cargar datos en BigQuery',
    schedule_interval=timedelta(days=7),  # Programado para ejecutarse semanalmente
)

# Define el operador Python que ejecutará el script
run_script_task = PythonOperator(
    task_id='TransformPowerBI',
    python_callable=execute_yelp_script,
    provide_context=True,  # Necesario para pasar el contexto a la función
    dag=dag,
)

# Define el operador Python que construirá la consulta de inserción y la ejecutará
load_to_bigquery_task = PythonOperator(
    task_id='load_to_bigquery_task',
    python_callable=construir_insert_query,
    provide_context=True,  # Necesario para pasar el contexto a la función
    dag=dag,
)

# Configura las dependencias del DAG
run_script_task >> load_to_bigquery_task

if __name__ == "__main__":
    dag.cli()

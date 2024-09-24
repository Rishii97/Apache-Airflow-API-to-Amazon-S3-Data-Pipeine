# Define the DAG
with DAG(
    dag_id='weather_data_pipeline',
    schedule_interval='@daily',
    start_date=datetime(2024, 9, 23),
    catchup=False,
) as dag:
    
    extract_task = PythonOperator(
        task_id='extract_weather_data',
        python_callable=extract_weather_data,
    )

    transform_task = PythonOperator(
        task_id='transform_weather_data',
        python_callable=transform_weather_data,
    )

    load_task = PythonOperator(
        task_id='load_to_s3',
        python_callable=load_to_s3,
    )

    # Set task dependencies
    extract_task >> transform_task >> load_task

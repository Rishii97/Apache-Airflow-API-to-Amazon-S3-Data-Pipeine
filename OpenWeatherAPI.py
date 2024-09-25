from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import requests
import pandas as pd
import boto3
import os

# Define constants
API_KEY = 'your_openweathermap_api_key'  # Replace with your OpenWeatherMap API key
CITY_NAME = 'London'  # Replace with the city you want
API_URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}'
CSV_FILE_PATH = '/tmp/weather_data.csv'
S3_BUCKET = 'your-s3-bucket-name'  # Replace with your S3 bucket name
S3_FILE_KEY = f'weather_data/{CITY_NAME}.csv'  # Path in the S3 bucket

def extract_weather_data():
    """Extract weather data from the OpenWeatherMap API."""
    response = requests.get(API_URL)
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json()

    # Parse the required data
    weather_data = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'weather': data['weather'][0]['description'],
        'wind_speed': data['wind']['speed'],
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    # Convert to DataFrame
    df = pd.DataFrame([weather_data])
    df.to_csv(CSV_FILE_PATH, index=False)
    print(f"Weather data extracted and saved to {CSV_FILE_PATH}")

def transform_weather_data():
    """Transform the weather data (in this case, the data is simple, so no real transformation)."""
    # If necessary, read the CSV and perform transformations
    df = pd.read_csv(CSV_FILE_PATH)
    
    # Example transformation: convert temperature from Kelvin to Celsius
    df['temperature_celsius'] = df['temperature'] - 273.15
    
    # Save the transformed data back to CSV
    df.to_csv(CSV_FILE_PATH, index=False)
    print(f"Transformed data saved to {CSV_FILE_PATH}")

def load_to_s3():
    """Load the CSV file to Amazon S3."""
    s3_client = boto3.client('s3')
    s3_client.upload_file(CSV_FILE_PATH, S3_BUCKET, S3_FILE_KEY)
    print(f"File uploaded to S3 bucket {S3_BUCKET} with key {S3_FILE_KEY}")

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
#added a line here to check the code push
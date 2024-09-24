# Apache-Airflow-API-to-Amazon-S3-Data-Pipeine
 This project implements an ETL (Extract, Transform, Load) pipeline using Apache Airflow to automate the fetching, processing, and storage of data. It extracts CSV data from a specified API, transforms it to meet quality and format requirements, and loads the cleaned data into an Amazon S3 bucket for analysis or storage

## Project Overview

This project implements an **ETL (Extract, Transform, Load)** pipeline using **Apache Airflow** to automate the process of fetching, processing, and storing data in a cloud environment. The pipeline extracts CSV data from a specified API, transforms it to meet data quality and format requirements, and then loads the cleaned data into an **Amazon S3** bucket for further analysis or storage.

## Features

- **Extract**: Fetches CSV data from a specified API.
- **Transform**: Cleans and preprocesses the data.
- **Load**: Uploads the transformed data to an Amazon S3 bucket.

## Technologies Used

- **Apache Airflow**: For orchestrating the ETL workflow.
- **Python**: The programming language for scripting.
- **Pandas**: For data manipulation and transformation.
- **Requests**: For making HTTP requests to the API.
- **Boto3**: For interacting with AWS services, specifically S3.

## Requirements

- Python 3.7+
- Apache Airflow
- pandas
- requests
- boto3

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Rishii97/airflow-api-to-s3-pipeline.git
   cd airflow-api-to-s3-pipeline

Finance Data Pipeline Project

This project is a data pipeline designed to automate the extraction, processing, and storage of financial data. The pipeline is built using Apache Airflow, and it interacts with the Twelve Data API to fetch stock market data, process it into a CSV format, and store it in a Google Cloud Storage (GCS) bucket.

Table of Contents
Project Overview
Features
Technologies Used
Installation
Usage
Contributing
License
Project Overview
This project provides a simple yet powerful data pipeline that automates the process of fetching financial data from an API, converting it into a CSV file, and uploading it to Google Cloud Storage. The process is fully automated using Apache Airflow, which schedules and manages the various tasks involved in the pipeline.

Features
Automated Data Extraction: Fetches financial data from the Twelve Data API.
Data Processing: Converts the API response into a CSV file for easy storage and analysis.
Cloud Storage: Uploads the CSV file to a Google Cloud Storage bucket.
Orchestration with Apache Airflow: Manages and schedules tasks in the pipeline, ensuring reliable and repeatable processes.
Technologies Used
Python: Core programming language used for data extraction and processing.
Apache Airflow: Orchestrates the pipeline, handling task dependencies and scheduling.
Google Cloud Platform (GCP): Used for storing the processed data in a GCS bucket.
Twelve Data API: Source of financial data, providing real-time and historical stock information.
CSV: Format used to store the extracted data.
Installation
Prerequisites
Python 3.x installed on your system.
Apache Airflow installed and configured.
Google Cloud SDK installed and authenticated with access to your GCS bucket.
API Key from Twelve Data API.
Steps
Clone the Repository:


bash
Copy code
git clone https://github.com/ahmedmakroum/pipelinestocks.git
cd finance-data-pipeline
Install Python Dependencies:



Copy code
pip install -r requirements.txt
Set Up Airflow:

Place the dag.py script in your Airflow DAGs directory.
Start the Airflow scheduler and web server:


Copy code
airflow scheduler
airflow webserver
Configure Google Cloud Storage:

Ensure your GCP credentials are set up and your project is selected.
Update the bucket name in dag.py to match your GCS bucket.
Usage
Triggering the DAG:


Access the Airflow web UI at http://localhost:8080.
Locate the finance_data_pipeline DAG.
Trigger the DAG manually or set it to run on a schedule.
Monitoring:


Monitor the DAG's execution from the Airflow UI to ensure tasks are running as expected.
Check the GCS bucket to verify that the CSV files are being uploaded correctly.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request for review.



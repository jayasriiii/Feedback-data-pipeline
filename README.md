# Feedback Data Pipeline (Azure + Python)

## Problem

User feedback data is stored in raw JSON format in Azure Blob Storage.
This data is unstructured and not directly useful for analytics.

## Solution

This project builds a simple data pipeline that:

1. Reads raw feedback data from Azure Blob Storage
2. Processes and enriches the data
3. Stores cleaned data in a separate container

## What this pipeline actually does

* Reads JSON files from `raw-feedback`
* Calculates:

  * feedback length
  * processing status
* Writes updated JSON to `processed-feedback`

## Example

### Input

{
"feedback": "Good service"
}

### Output

{
"feedback": "Good service",
"feedback_length": 12,
"processed": true
}

## Tech Stack

* Python
* Flask
* Azure Blob Storage

## How it works

1. Flask API triggers the pipeline
2. Python script reads blobs
3. Data is processed in-memory
4. Updated data is written back to Azure

## How to Run

pip install -r requirements.txt
python app.py

## Future Improvements

* Add error handling
* Add logging
* Automate with Azure Functions
* Add dashboard (Streamlit)

## Author

Jayasri

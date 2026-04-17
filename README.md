# Feedback Data Pipeline (Azure + Python)

## Overview

This project is a simple data pipeline that processes user feedback stored in Azure Blob Storage.

It:

* Reads raw JSON feedback files from a container
* Processes the data (adds metadata like feedback length)
* Writes processed data to another container

## Tech Stack

* Python
* Flask (for API)
* Azure Blob Storage

## Architecture

Raw Container → Processing Script → Processed Container

## Features

* Automated data processing
* JSON transformation
* Cloud storage integration

## How to Run

1. Clone the repo

2. Install dependencies:
   pip install -r requirements.txt

3. Run:
   python app.py

## Future Improvements

* Add validation
* Add logging
* Add dashboard
* Deploy on Azure

## Author

Jayasri

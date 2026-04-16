from azure.storage.blob import BlobServiceClient
import os
import json
import time
from dotenv import load_dotenv

load_dotenv()

connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

blob_service_client = BlobServiceClient.from_connection_string(connect_str)

source_container = "raw-feedback"
target_container = "processed-feedback"

container_client = blob_service_client.get_container_client(source_container)

while True:
    print("Checking for new files...")

    for blob in container_client.list_blobs():
        blob_client = blob_service_client.get_blob_client(container=source_container, blob=blob.name)

        data = blob_client.download_blob().readall()
        data = json.loads(data)

        if data.get("processed"):
            continue

        data["feedback_length"] = len(data["feedback"])
        data["processed"] = True

        target_blob = blob_service_client.get_blob_client(container=target_container, blob=blob.name)
        target_blob.upload_blob(json.dumps(data), overwrite=True)

        print(f"Processed: {blob.name}")

    time.sleep(10)
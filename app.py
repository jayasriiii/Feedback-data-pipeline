from flask import Flask, request, render_template_string
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os
import datetime
import json

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Get values from .env
connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
container_name = os.getenv("CONTAINER_NAME")

# Connect to Azure Blob
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

# Simple HTML form
HTML = """
<h2>Feedback Form</h2>
<form method="POST">
    Name: <input type="text" name="name" required><br><br>
    Feedback: <textarea name="feedback" required></textarea><br><br>
    <input type="submit">
</form>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        feedback = request.form["feedback"]

        # Create structured data
        data = {
            "name": name,
            "feedback": feedback,
            "timestamp": str(datetime.datetime.now())
        }

        # Unique file name
        blob_name = f"feedback_{datetime.datetime.now().timestamp()}.json"

        # Upload to Azure
        blob_client = blob_service_client.get_blob_client(
            container=container_name,
            blob=blob_name
        )

        blob_client.upload_blob(json.dumps(data))

        return "✅ Feedback stored in Azure!"

    return render_template_string(HTML)


if __name__ == "__main__":
    app.run(debug=True)
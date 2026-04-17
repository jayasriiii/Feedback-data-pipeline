from ingest import read_data
from validate import validate_data
from transform import transform_data

def run_pipeline():
    data = read_data("data/raw/input.json")

    data = validate_data(data)

    data = transform_data(data)

    import json
    with open("data/processed/output.json", "w") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    run_pipeline()

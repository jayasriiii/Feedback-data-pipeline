from ingest import read_data
from transform import process_data
from load import save_data

def run_pipeline():
    data = read_data()
    processed_data = process_data(data)
    save_data(processed_data)

if __name__ == "__main__":
    run_pipeline()

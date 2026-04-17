import pandas as pd

def read_data():
    try:
        data = pd.read_csv("data/raw_feedback.csv")
        print("✅ Data loaded successfully")
        return data
    except Exception as e:
        print("❌ Error reading data:", e)
        return None

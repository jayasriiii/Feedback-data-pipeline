def save_data(df):
    if df is None:
        print("❌ No data to save")
        return

    try:
        df.to_csv("data/processed_feedback.csv", index=False)
        print("✅ Data saved successfully")
    except Exception as e:
        print("❌ Error saving data:", e)

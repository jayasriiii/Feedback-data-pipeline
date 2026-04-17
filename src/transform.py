def process_data(df):
    if df is None:
        print("❌ No data to process")
        return None

    # Drop null values
    df = df.dropna()

    # Example: convert text to lowercase
    if "feedback" in df.columns:
        df["feedback"] = df["feedback"].str.lower()

    print("✅ Data transformed")
    return df

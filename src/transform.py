def transform_data(data):
    for record in data:
        record["feedback_length"] = len(record["feedback"])

    return data

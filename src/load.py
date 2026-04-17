
def validate_data(data):
    valid_data = []

    for record in data:
        if "feedback" in record and record["feedback"]:
            valid_data.append(record)

    return valid_data

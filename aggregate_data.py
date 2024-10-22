def aggregate_data(data_list):
    # Sample function to aggregate data
    total_temp = sum(data['temperature'] for data in data_list)
    return total_temp / len(data_list) if data_list else 0

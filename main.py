from demographic_data_analyzer import calculate_demographic_data

if __name__ == "__main__":
    results = calculate_demographic_data(print_data=True)

    print("\nSummary of results (returned as dictionary):")
    for key, value in results.items():
        print(f"{key}: {value}")
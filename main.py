from demographic_data_analyzer import calculate_demographic_data

# making sure the code only runs if it actually run this file directly
if __name__ == "__main__":
    # calling the main function from the other file
    results = calculate_demographic_data(print_data=True)

    print("\nSummary of results (returned as dictionary):")
    for key, value in results.items():
        print(f"{key}: {value}")
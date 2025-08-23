import pandas as pd

def calculate_demographic_data(print_data=True):
    # column names for the dataset since the CSV doesn't have headers
    columns = [
        "age", "workclass", "fnlwgt", "education", "education-num",
        "marital-status", "occupation", "relationship", "race", "sex",
        "capital-gain", "capital-loss", "hours-per-week", "native-country", "salary"
    ]

    # reading the dataset and adding the column names
    df = pd.read_csv(
        "adult.data.csv",
        header=None,
        names=columns,
        skipinitialspace=True,
        na_values="?"
    )

    for col in df.select_dtypes(include="object"):
        df[col] = df[col].str.strip()

    # count the number of people in each race category
    race_count = df["race"].value_counts()

    # get only men and calculate their average age
    men = df[df["sex"] == "Male"]
    average_age_men = round(men["age"].mean(), 1)

    # percentage of people with Bachelors degree
    percentage_bachelors = round(df["education"].eq("Bachelors").mean() * 100, 1)

    # masks to separate higher education (Bachelors, Masters, Doctorate) from others
    higher_mask = df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    lower_mask = ~higher_mask
    rich_mask = df["salary"] == ">50K"

    # counting totals for both groups
    higher_total = df[higher_mask].shape[0]
    lower_total  = df[lower_mask].shape[0]

    # counting how many in each group earn >50K
    higher_rich  = df[higher_mask & rich_mask].shape[0]
    lower_rich   = df[lower_mask & rich_mask].shape[0]

    # percentage of rich people with higher and lower education
    higher_education_rich = round((higher_rich / higher_total) * 100, 1) if higher_total else 0.0
    lower_education_rich  = round((lower_rich  / lower_total)  * 100, 1) if lower_total  else 0.0

    # find the minimum hours worked per week in the dataset
    min_work_hours = int(df["hours-per-week"].min())

    # mask to get people who work the minimum hours
    min_mask = df["hours-per-week"].eq(min_work_hours)
    min_total = df[min_mask].shape[0]
    
    # out of those who work minimum hours, count how many earn >50K
    min_rich  = df[min_mask & rich_mask].shape[0]
    rich_percentage = round((min_rich / min_total) * 100, 1) if min_total else 0.0

    # calculate rich percentage by country
    country_total = df["native-country"].value_counts()
    country_rich  = df[rich_mask]["native-country"].value_counts()
    pct_by_country = (country_rich / country_total * 100).dropna()

    # find which country has the highest percentage of rich people
    if not pct_by_country.empty:
        highest_earning_country = pct_by_country.idxmax()
        highest_earning_country_percentage = round(pct_by_country.max(), 1)
    else:
        highest_earning_country = None
        highest_earning_country_percentage = 0.0

    # for India, check the most popular occupation among rich people
    india_rich = df[(df["native-country"] == "India") & rich_mask]
    top_IN_occupation = india_rich["occupation"].mode().iat[0] if not india_rich.empty else None

    # print results if print_data is True
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    # Return a dictionary with all results
    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }
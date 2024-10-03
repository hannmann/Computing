import pandas as pd

# Load the COVID data provided by the user
file_path = '/Users/nicolasrauth/Downloads/covid.csv'
covid_data = pd.read_csv(file_path)

# Display the content of the file
covid_data.head()

# 10) Create a function called "country_with_least_average_cases"
#     that takes the data structure and returns the name of the country
#     with the lowest average number of active cases.
def country_with_least_average_cases(covid_data):
    # Calculate the average active cases
    country_avg = covid_data.groupby('Country')['Active'].mean()
    # Return the country with the lowest average active cases
    return country_avg.idxmin()

# Example usage:
print(country_with_least_average_cases(covid_data))


# 7) Create a function called "country_total_cases"
#    that takes the data structure and returns a dictionary with
#    the total number of cases for each country.
def country_total_cases(covid_data):
    return {country: sum(cases) for country, cases in covid_data.items()}

# 8) Create a function called "country_with_most_cases"
#    that takes the data structure and returns the name of the country
#    with the highest number of total cases.
def country_with_most_cases(covid_data):
    total_cases = country_total_cases(covid_data)
    return max(total_cases.items(), key=lambda x: x[1])[0]

# 9) Create a function called "weekly_case_average"
#    that takes the data structure and returns a dictionary with
#    the average number of cases per week for each country.
def weekly_case_average(covid_data):
    return {country: sum(cases) / len(cases) for country, cases in covid_data.items()}

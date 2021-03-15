import requests
import csv
import pandas as pd
import matplotlib.pyplot as plt

base_url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'

# Call API to get covid data and store it in a csv file
covid_api = requests.get(base_url)
covid_content = covid_api.content
covid_csv = open('covid.csv', 'wb')
covid_csv.write(covid_content)
covid_csv.close()

# Create dataframe from csv file
covid_county_df = pd.read_csv('covid.csv')

# Create data frame to document case count by county 
covid_cases_county_df = covid_county_df.groupby(['fips', 'county', 'state'], as_index=False)['cases'].max()

# Create data frame to document death count by county 
covid_deaths_county_df = covid_county_df.groupby(['fips', 'county', 'state'], as_index=False)['deaths'].max()

# Convert fips codes to be strings
covid_cases_county_df['fips'] = covid_cases_county_df['fips'].apply(lambda x: str(int(x)))
covid_deaths_county_df['fips'] = covid_deaths_county_df['fips'].apply(lambda x: str(int(x)))

# Add a leading 0 to the fips codes of AK, AZ, AL, AR, CA, and CO

def update_fips(fip):
    if len(fip) == 4:
        return '0'+fip
    else:
        return fip

covid_cases_county_df['fips'] = covid_cases_county_df['fips'].apply(lambda x: update_fips(x))
covid_deaths_county_df['fips'] = covid_deaths_county_df['fips'].apply(lambda x: update_fips(x))


# Create data frame to document case count by county 
covid_cases_state_df = covid_cases_county_df.groupby('state', as_index=False)['cases'].sum()

# Create data frame to document death count by county 
covid_deaths_state_df = covid_deaths_county_df.groupby('state', as_index=False)['deaths'].sum()

# Update deaths in the state df to be integers
covid_deaths_state_df['deaths'] = covid_deaths_state_df['deaths'].apply(lambda x: int(x))

# Add state abbreviations to both state dfs

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "NI", "OH", "OK", "OR", "PA", "PR", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VI", "VA", "WA", "WV", "WI", "WY"]

covid_cases_state_df['state_abb'] = states
covid_deaths_state_df['state_abb'] = states

# test for checking county data by state
# sd_cases_df = covid_cases_county_df[covid_cases_county_df['state'] == 'South Dakota']

# print(sd_cases_df.tail(20))
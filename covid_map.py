import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from data_mining import covid_cases_county_df, covid_deaths_county_df, covid_cases_state_df, covid_deaths_state_df
from urllib.request import urlopen
import json

# Where the geolocations for the us counties are stored
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

# Create the map for covid cases by county
county_cases_fig = px.choropleth(covid_cases_county_df, geojson=counties, locations='fips', 
                    color='cases', color_continuous_scale="orrd",
                    range_color=(0, 100000), color_continuous_midpoint= 25000, 
                    scope="usa", hover_name='county', hover_data=["cases"]
                    )

county_cases_fig.update_layout(margin={"r":10,"t":10,"l":10,"b":10})

# Write the graph to an html file. Change 'auto_open' to "True" to see graph in browser
pio.write_html(county_cases_fig, file=f'templates/county_covid_cases.html', auto_open=True)


# Create the map for covid deaths by county
county_deaths_fig = px.choropleth(covid_deaths_county_df, geojson=counties, locations='fips', 
                    color='deaths', color_continuous_scale="orrd",
                    range_color=(0, 2500), scope="usa", 
                    hover_name='county', hover_data=["deaths"]
                    )

county_deaths_fig.update_layout(margin={"r":10,"t":10,"l":10,"b":10})

# Write the graph to an html file. Change 'auto_open' to "True" to see graph in browser
pio.write_html(county_deaths_fig, file=f'templates/county_covid_deaths.html', auto_open=False)


# Create the map for covid cases by state
state_cases_fig = go.Figure(
                data=go.Choropleth(
                locations=covid_cases_state_df['state_abb'], # Spatial coordinates
                z = covid_cases_state_df['cases'].astype(int), # Data to be color-coded
                locationmode = 'USA-states', # set of locations match entries in `locations`
                colorscale = 'reds',
                colorbar_title = "Covid Cases",
                ))

state_cases_fig.update_layout(
    title_text = 'Covid Cases by State',
    geo_scope='usa', # limite map scope to USA
    margin={"r":0,"t":0,"l":0,"b":0}
)

# Write the graph to an html file. Change 'auto_open' to "True" to see graph in browser
pio.write_html(state_cases_fig, file=f'templates/state_covid_cases.html', auto_open=False)

# Create the map for covid deaths by state
state_deaths_fig = go.Figure(
                data=go.Choropleth(
                locations=covid_deaths_state_df['state_abb'], # Spatial coordinates
                z = covid_deaths_state_df['deaths'].astype(int), # Data to be color-coded
                locationmode = 'USA-states', # set of locations match entries in `locations`
                colorscale = 'reds',
                colorbar_title = "Covid Deaths",
                ))

state_deaths_fig.update_layout(
    title_text = 'Covid Deaths by State',
    geo_scope='usa', # limite map scope to USA
    margin={"r":0,"t":0,"l":0,"b":0}
)

# Write the graph to an html file. Change 'auto_open' to "True" to see graph in browser
pio.write_html(state_deaths_fig, file=f'templates/state_covid_deaths.html', auto_open=False)
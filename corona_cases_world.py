import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Read data from csv 
# *got from kaggle: https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset/version/50
corona_confirmed = pd.read_csv("time_series_covid_19_confirmed.csv",sep=',')
corona_deaths = pd.read_csv("time_series_covid_19_deaths.csv",sep=',')

# get dates from csv columns: 
# put it on correct format for image index
dates = pd.to_datetime(corona_confirmed.columns[4:],dayfirst=False) 
# get current format for selecting data to plot
columns = list(corona_confirmed.columns[4:])

# format data for image
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=10))

# select which countries to view/export data
countries = ['Brazil','Italy','Spain','United Kingdom','Canada']

for country in countries:
    # get data for specific country (sum all provincies)
    plot_country_confirmed = corona_confirmed[corona_confirmed['Country/Region']==country].sum()
    plot_country_deaths = corona_deaths[corona_deaths['Country/Region']==country].sum()

    # plot confirmed cases
    plt.plot(dates,plot_country_confirmed[columns])
    plt.gcf().autofmt_xdate()
    plt.title('Coronavirus Cases in ' + country)
    plt.grid(True)
    plt.show()
    plt.close()

    # plot number of deaths
    plt.plot(dates,plot_country_deaths[columns])
    plt.gcf().autofmt_xdate()
    plt.title('Coronavirus Deaths in ' + country)
    plt.grid(True)
    plt.show()
    plt.close()

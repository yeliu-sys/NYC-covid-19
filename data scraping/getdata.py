# data processing
import pandas as pd
import numpy as np
from datetime import timedelta, datetime


# data visualization
import plotly.graph_objs as go
from plotly.graph_objs import Bar, Layout
from plotly import offline
import matplotlib.pyplot as plt

plt.rcParams['axes.unicode_minus'] = False 

# change text color
import colorama
from colorama import Fore, Style

def GET_csse_covid_19_time_series():

    print('loading timeseries data......')

    ts_confirmed_us = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv')
    ts_confirmed_global = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    ts_deaths_us = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv')
    ts_deaths_global = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
    ts_recovered_global = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
    print('complete')
    
    return ts_confirmed_us,ts_confirmed_global,ts_deaths_us,ts_deaths_global,ts_recovered_global


def GET_csse_covid_19_daily_reports():

    print('loading daily data......')
    
    latest = datetime.strptime(ts_confirmed_us.columns[-1],'%m/%d/%y').strftime('%m-%d-%Y')
    prev = (datetime.strptime(ts_confirmed_us.columns[-1],'%m/%d/%y')+timedelta(-1)).strftime('%m-%d-%Y')
    
    url1 = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/'

    latest_data_global = pd.read_csv(url1 + f'csse_covid_19_daily_reports/{latest}.csv')
    prev_data_global = pd.read_csv(url1 + f'csse_covid_19_daily_reports/{prev}.csv')
    
    latest_data_us = pd.read_csv(url1 + f'csse_covid_19_daily_reports_us/{latest}.csv')
    prev_data_us = pd.read_csv(url1 + f'csse_covid_19_daily_reports_us/{prev}.csv')


    print('complete')
    return latest_data_global,prev_data_global,latest_data_us,prev_data_us

        
  

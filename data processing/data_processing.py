#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 21:48:46 2022

@author: liuye
"""

# import packages

# data processing
import pandas as pd
import numpy as np
from datetime import timedelta, datetime


import re

# data visualization
from tabulate import tabulate
import plotly.graph_objs as go
from plotly.graph_objs import Bar, Layout
from plotly import offline
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="whitegrid")
sns.set(rc={'figure.figsize':(11.7,8.27)})

plt.rcParams['axes.unicode_minus'] = False 

# change text color
import colorama
from colorama import Fore, Style

# IPython
from IPython.display import IFrame

def ts_process_US(ts_data, death = False, clip = False):
    # get loc
    ts_data = ts_data.dropna()
    loc_data = ts_data[['UID','FIPS','Admin2','Province_State','Lat','Long_']]

    ts_data = ts_data.set_index(['Province_State','Admin2']).iloc[:,9:]
    if death:
        population = ts_data.groupby('Province_State')['Population'].sum()
        ts_data = ts_data.drop('Population',axis=1)

    if clip:
        ts_data = ts_data.diff(axis=1).fillna({ts_data.columns[0]:ts_data[ts_data.columns[0]]},downcast = 'infer').clip(lower=0)
    else:
        ts_data = ts_data.diff(axis=1).fillna({ts_data.columns[0]:ts_data[ts_data.columns[0]]},downcast = 'infer')
        
    ts_data = ts_data.groupby('Province_State').sum()
    ts_data = ts_data.sort_values(by = ts_data.columns[-1],ascending=False)
    ts_data = ts_data.T
    ts_data.index = pd.to_datetime(ts_data.index)
    ts_data.columns.name = ''

    sorted_state = ts_data.columns

    if death:
        return ts_data,loc_data,sorted_state,population
    
    return ts_data,loc_data,sorted_state






# New York City COVID-19 Time Series Analysis

This is a project where I analyzed COVID-19 data for New York and the US from 2020 to 2023. 

## Overview

This repository contains time series analysis and visualizations of COVID-19 data for New York and the United States, focusing on confirmed cases and deaths from 2020 to 2023. The project uses advanced time series decomposition and forecasting techniques to analyze pandemic trends.

## Where the data comes from

All the data comes from the Johns Hopkins COVID-19 repository:
- [JHU CSSE COVID-19 Data](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data)

These folks did an amazing job collecting pandemic data worldwide.

## What I looked at

By breaking down the COVID-19 numbers in a few ways:

- **Breaking apart the patterns** - Separated the data into trend, seasonal patterns, and random noise
- **Weekly patterns** - Checked out how cases went up and down within each week
- **Major waves** - Identified the big peaks, especially that massive one in January 2022
- **Forecasting** - Tried a bunch of different methods to predict future numbers

## Key findings

- New York had several distinct COVID waves, with the biggest spike hitting in January 2022
- There's a clear weekly pattern in the data (weekends reported differently than weekdays)
- The data was "stationary" after adjustments 
- Some forecasting methods worked way better than others

## Visualizations

Checking  in results file:

1. **Daily case counts** with smoothed averages to cut through the noise
2. **Decomposed trends** showing the underlying direction without the weekly ups and downs
3. **Seasonal patterns** broken out by year
4. **Forecast comparisons** where I tested 9 different prediction methods
5. **Death statistics** that follow similar but distinct patterns from case counts

## Forecasting Model Selection

Testing different forecasting methods against each other:
- Simple smoothing methods
- More complex ARIMA and SARIMA models 
- Automatically optimized versions

After a lot of testing, the model ARIMA(2,2,2)(1,0,1)[6] came out on top. But the simple models performed surprisingly well too.


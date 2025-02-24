# data processing
import pandas as pd
import numpy as np
from datetime import timedelta, datetime


# data visualization
import plotly.graph_objs as go
from plotly.graph_objs import Bar, Layout
from plotly import offline
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['Heiti TC'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

# change text color
import colorama
from colorama import Fore, Style

def GET_csse_covid_19_time_series():

    print('正在读取【时间序列】数据......')

    ts_confirmed_us = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv')
    ts_confirmed_global = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    ts_deaths_us = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv')
    ts_deaths_global = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
    ts_recovered_global = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
    
    print('读取完毕')
    
    return ts_confirmed_us,ts_confirmed_global,ts_deaths_us,ts_deaths_global,ts_recovered_global



def GET_csse_covid_19_daily_reports():

    print('正在读取【横截面】数据......')
    
    ts_confirmed_us = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv')

    latest = datetime.strptime(ts_confirmed_us.columns[-1],'%m/%d/%y').strftime('%m-%d-%Y')
    prev = (datetime.strptime(ts_confirmed_us.columns[-1],'%m/%d/%y')+timedelta(-1)).strftime('%m-%d-%Y')
    
    url1 = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/'

    latest_data_global = pd.read_csv(url1 + f'csse_covid_19_daily_reports/{latest}.csv')
    prev_data_global = pd.read_csv(url1 + f'csse_covid_19_daily_reports/{prev}.csv')
    
    latest_data_us = pd.read_csv(url1 + f'csse_covid_19_daily_reports_us/{latest}.csv')
    prev_data_us = pd.read_csv(url1 + f'csse_covid_19_daily_reports_us/{prev}.csv')


    print('读取完毕')
    return latest_data_global,prev_data_global,latest_data_us,prev_data_us

def GET_shanghai_data(plot = True, encoding = "UTF-8"):

    '''
    data_name:数据名称：可选：'ts_shanghai_covid' 或者 'latest_shanghai_covid'，默认是'ts_shanghai_covid'
    plot：是否画图，默认是否
    '''
    import re
    print('正在获取并处理【上海】数据（数据来自上海卫健委）......')
    url = f'https://raw.githubusercontent.com/datoujinggzj/WhalePkg/master/DATA/ts_shanghai_covid.csv'
    
    # 读取数据的detail
    data = pd.read_csv(url)['detail']
    print('读取完毕')
    
    
    # 数据清洗
    # 需要得到【新增本土确诊】和【新增本土无症状】数据
    
    data = data[data.str.startswith('上海202')].sort_values()
             
    data = data.apply(lambda x : x.replace('无新增','0'))

    data = data.apply(lambda x: re.findall(r'\d+',x))

    df = pd.DataFrame({'日期': [i[:3] for i in data ],                                                  
                         '新增本土确诊': [i[3] for i in data],
                         '新增本土无症状': [i[4] for i in data]})
    
    
    for j in range(len(data)):
        df['日期'][j] = ''.join(str(i) for i in df['日期'][j])
        df['日期'][j]= datetime.strptime(df['日期'][j],'%Y%m%d').strftime('%Y-%m-%d')
        
    df.index = pd.to_datetime(df.index, format = '%Y-%m-%d %H:%M')
    df = df.set_index('日期').sort_index()
    df = df.astype('int32')
    df = df[df.index <'2022-06-12']

    if plot:
        fig, axes = plt.subplots(nrows=2, ncols=1,figsize = [10,5*2])
        df.index = pd.to_datetime(df.index, format = '%Y-%m-%d %H:%M')
        df_2022 = df[df.index>'2022-01-01']
        
        for col,ax in zip(df_2022.columns,axes):
            ax.step(df_2022.index, df_2022[col], color = '#202124',linewidth = 2)
            ax.bar(df_2022.index, df_2022[col],alpha = .8)
            ax.vlines(x=pd.to_datetime('2022-04-01'), ymin=0, ymax=df[col].max(), linewidth=2, color = '#4b7ffc', linestyle = '--')
            ax.vlines(x=pd.to_datetime('2022-06-01'), ymin=0, ymax=df[col].max(), linewidth=2, color = '#4b7ffc', linestyle = '--')

            ax.hlines(y=df[col].max(), xmin=df_2022.index[0], xmax=df_2022.index[-1], linewidth=1, color = '#ff0000')
            ax.text(x = df_2022.index[0], s=df[col].max(),y = df[col].max(), color = 'black', fontsize = 14)
            ax.text(x = df_2022.index[0], s=f"峰值：时间：{str(df.index[df[col].argmax()])} \n新增：{df[col].max()}例",y = df[col].max()/2, color = '#ff0000', fontsize = 18)
            ax.text(x = df_2022.index[0], s=f"今日：时间：{str(df.index[-1])} \n新增：{df[col][-1]}例",y = df[col].max()/4, color = '#ff0000', fontsize = 18)

            ax.text(x = pd.to_datetime("2022-03-15"), s="始于玩笑\n2022年4月1日",y = df[col].max()*2/3, color = 'black', fontsize = 12)
            ax.text(x = pd.to_datetime("2022-05-15"), s="终于儿戏\n2022年6月1日",y = df[col].max()*2/3, color = 'black', fontsize = 12)

            ax.set_xlabel('日期')
            ax.set_ylabel(f'{col}数')
            ax.set_title(f'{col}时间序列趋势图',fontsize = 16)

        plt.tight_layout()

    return df
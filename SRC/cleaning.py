# Title: energy use data cleaning
# Author: Doug
# Date Created: 7/30/2020
# Last Updated: 8/10/2020

import numpy as np
import pandas as pd


df = pd.read_csv('Data/energy_consumption.csv')
df.head()
df.info()

#dropping entries for which month code == 13, meaning whole year
for i in range(df.shape[0]):
    if str(df.year_month[i])[-2:] == '13':
        df.drop(i, axis=0, inplace=True)
df.shape[0]


def create_month(df,month=str,num=int):
    '''
    For creating monthly Boolean variables

    df: pandas dataframe
    month: 3 letter string for month
    num: 2 digit month number, 01 through 12
    '''
    number = str(num)
    df['placeholder'] = 0
    for i in range(0, len(df)):
        temp = str(df.year_month[i])
        if temp[-2:] == number:
            df.placeholder[i] = 1
        else:
            continue
    df.rename(columns={'placeholder':month}, inplace=True)

create_month(df,jan,'01')
create_month(df,feb,'02')
create_month(df,mar,'03)'
create_month(df,apr,'04')
create_month(df,may,'05')
create_month(df,jun,'06')
create_month(df,jul,'07')
create_month(df,aug,'08')
create_month(df,sep,'09')
create_month(df,oct,'10')
create_month(df,nov,'11')
create_month(df,dec,'12')

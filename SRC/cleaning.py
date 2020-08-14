# Title: energy use data cleaning
# Author: Doug
# Date Created: 7/30/2020
# Last Updated: 8/10/2020

import numpy as np
import pandas as pd

'''
THIS CODE BLOCK NO LONGER NEEDED DUE TO ADOPTION OF DIFFERENT CSV FILE WITH
MORE USEFUL FORMATTING AND MORE COMPLETE DATA

# df = pd.read_csv('Data/energy_consumption.csv')
#dropping entries for which month code == 13, meaning whole year
for i in range(df.shape[0]):
    if str(df.year_month[i])[-2:] == '13':
        df.drop(i, axis=0, inplace=True)
df.shape[0]
'''

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
'''
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
df = pd.read_csv('Data/use_gen_data.csv')
df.head()
df.info()
'''
df = pd.read_csv('Data/use_gen_data.csv')

#creating month dummies, retaining original column just in case
df['m2'] = df.month
df = pd.get_dummies(df,columns=['m2'])

#This should be moved to another file
'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
# Code used to seperate the 4 digit year from column of strings with year, month
# where month string is non-numeric
def seperate(df,varname=str,filepath=str,newfilepath=str)
''' Code used to seperate the 4 digit year from column of strings with year, month
where month string is non-numeric, requires column names in csv

df: name of temp dataframe 
filepath: string, filepath to pull csv file containing unhelpful date formats
newfilepath: string, filepath to save new csv containing seperated columns

EX: 
seperate(df2,long,Data/longdates.csv,Data/justdate.csv)
'''
    df = pd.read_csv(filepath)
    df['year'] = None
    
    for i in range(df.shape[0]):
        df.year[i] = int(df.varname[i][:4])

    df['month'] = None
    for i in range(df.shape[0]):
        df.month[i] = df.varname[i][6:]

    df.drop([varname],axis=1, inplace=True)
    df.to_csv(newfilepath)
    del df
'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

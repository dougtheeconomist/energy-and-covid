# Title: energy use data cleaning
# Author: Doug
# Date Created: 7/30/2020
# Last Updated: 9/1/2020

import numpy as np
import pandas as pd

def first_diff(df, column=str, keep=True):
    '''
    appends new column to specified dataframe which has the values of the change from 
    previous period of a specified existing column
    df: dataframe object
    
    column: name of column to take difference of, string
    
    keep(optional): if specified False, drop original column
    '''
    place = str(column)
    new = place + 'diff'
    df[new] = None
    for i in range(1, len(df[column])):
        df[new][i] = float(df[column][i]-df[column][i-1])
    if keep == False:
        df.drop([column], axis=1, inplace=True)

#making date variable for graphing, dropping first row
def make_date(val1, val2):
    '''
    For creating date variable from existing year, month data
    
    val1: year
    val2: month
    '''
    date_var = datetime.date(int(val1), int(val2), 1)
    return date_var

# Function to encompass all of cleaning, with option to pickle upon completion
def clean_to_pickle(filepath=str,pickle_df=False, newfilepath='Data/energy_820.pkl'):
    '''
    Loads data from csv file as dataframe object, cleans it, in this case mostly generating new columns
    based on existing data for analysis and saves to pickled file

    filepath: string, location of csv file containing data for analysis

    pickle_df: default False, if True will save resulting dataframe to pickled file

    newfilepath: string, filepath to save pickled file, if applicable

    current filepath: 'Data/use_gen_data.csv'
    '''

    df = pd.read_csv(filepath)

    #creating columns for percentage of total electricity generated for each source
    df['coal_prcnt'] = df.coal_prod / df.total_primary_energy_prod
    df['ng_prcnt'] = df.nat_gas_prod / df.total_primary_energy_prod
    df['c_oil_prcnt'] = df.crude_oil_prod / df.total_primary_energy_prod
    df['ngl_prcnt'] = df.natural_gas_liquids_prod / df.total_primary_energy_prod
    df['tot_fossil_prcnt'] = df.total_ff_prod / df.total_primary_energy_prod
    df['nuke_prcnt'] = df.nuclear_prod / df.total_primary_energy_prod
    df['hydro_prcnt'] = df.hydro_prod / df.total_primary_energy_prod
    df['geo_prcnt'] = df.geothermal_prod / df.total_primary_energy_prod
    df['solar_prcnt'] = df.solar_prod / df.total_primary_energy_prod
    df['wind_prcnt'] = df.wind_prod / df.total_primary_energy_prod
    df['bio_prcnt'] = df.biomass_prod / df.total_primary_energy_prod
    df['tot_renew_prcnt'] = df.total_renewable_prod / df.total_primary_energy_prod




    #creating change variables for all relevant columns
    for i in df.columns[2:]:
        first_diff(df,i)

    #creating month dummies, retaining original column just in case
    df['m2'] = df.month
    df = pd.get_dummies(df,columns=['m2'])

    df['date'] = 0
    for i in range(df.shape[0]):
        df.date[i] = make_date(df.year[i],df.month[i])

    # dropping first row containing nontype values and converting columns to floats
    df.drop(0, axis=0, inplace = True)
    col_list= ['residential_cdiff', 'commercial_cdiff',
        'industrial_cdiff', 'transportation_cdiff', 'gen_cdiff', 'total_cdiff',
        'coal_proddiff', 'nat_gas_proddiff', 'crude_oil_proddiff',
        'natural_gas_liquids_proddiff', 'total_ff_proddiff', 'nuclear_proddiff',
        'hydro_proddiff', 'geothermal_proddiff', 'solar_proddiff',
        'wind_proddiff', 'biomass_proddiff', 'total_renewable_proddiff',
        'total_primary_energy_proddiff', 'coal_prcntdiff', 'ng_prcntdiff',
        'c_oil_prcntdiff', 'ngl_prcntdiff', 'tot_fossil_prcntdiff',
        'nuke_prcntdiff', 'hydro_prcntdiff', 'geo_prcntdiff', 'solar_prcntdiff',
        'wind_prcntdiff', 'bio_prcntdiff', 'tot_renew_prcntdiff']
    for i in col_list:
        df[i] = df[i].astype(float)

    if pickle_df == True:
        df.to_pickle(Data/energy_820.pkl, compression='zip')
    else:
        pass
    
    return df


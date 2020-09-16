# Title: energy use, data analysis
# Author: Doug
# Date Created: 8/18/2020
# Last Updated: 9/15/2020

import numpy as np
import pandas as pd
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt
#in jupyter
# %matplotlib inline
from cleaning import first_diff, clean_to_pickle, make_date

# either load pickle:
df = pd.read_pickle('Data/energy_820.pkl', compression='zip')

# or load csv and manually run clean function:
df = clean_to_pickle(Data/use_gen_data.csv, pickle_df=False)



'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~Consumption analysis~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
# average monthly for comparison
df.groupby('month').mean()[['residential_c', 'commercial_c', 'industrial_c',
       'transportation_c', 'gen_c', 'total_c', 'residential_cdiff', 'commercial_cdiff',
       'industrial_cdiff', 'transportation_cdiff', 'gen_cdiff', 'total_cdiff']]
#values for April
df.iloc[-1][2:8]

# Isolating into arrays for easy comparison
dfg = np.array(df.groupby('month').mean())
past_ave = dfg[3][1:7]

current_val = np.array(df.iloc[-1][2:8])

# Finding the percentage drop of April 2020 from mean
perc_drop = ((past_ave - current_val)/past_ave)*100
perc_drop

# T-test function
def test_param(df,val,col=str,month=int):
    dfm = df[df['month'] == month]
    return stats.ttest_1samp(dfm[col],val)[1]

#Function to do all of this
def mean_comparison(df,first_year,varlist,month_minus_one=int,test = False):
    '''
    finds mean for given variables by month going back to specified year and 
    calculates change from mean to 2020 value.
    
    df: name of dataframe object with relevant variables
    first_year: first year of data to include in mean
    varlist: list of variables within dataframe for comparison
    month_minus_one: integer, one less than the numerical month of interest
                     for comparison. For example, to look at April would be 3
    test: defualt False, setting to true will print result of t-test wherein 
            null hypthesis is that 2020 value is within the distribution of past values
            alternative is that it is not
    '''
    dfp = df[(df['year'] <2020) & (df['year'] >= first_year)]
    dfg = np.array(dfp.groupby('month').mean()[varlist])
    past_ave = dfg[month_minus_one]
    
#     dfsd = np.array(dfp.groupby('month').std()[varlist])
    
    newlist =[]
    
    for i in range(len(varlist)):
        if test == False:
            place = ((df[varlist[i]][df.shape[0]] - past_ave[i]) / past_ave[i]) * 100
            newlist.append(place)
            print(varlist[i], 'percentage change :', place)
        else:
            place = ((df[varlist[i]][df.shape[0]] - past_ave[i]) / past_ave[i]) * 100
            newlist.append(place)
            print(varlist[i], 'percentage change :', place, test_param(dfp,df[varlist[i]][df.shape[0]],varlist[i],month=(month_minus_one+1)))
    return newlist

vlist = ['residential_c', 'commercial_c', 'industrial_c',
       'transportation_c', 'gen_c', 'total_c','residential_cdiff', 'commercial_cdiff',
       'industrial_cdiff', 'transportation_cdiff', 'gen_cdiff', 'total_cdiff']
mean_comparison(df,2008, vlist,3,test=True)




'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~Generation analysis~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

# UNUSED AS COMPARISON FUNCTION DOESN'T USE VALUES THIS FAR BACK
#drop values prior to 1985 to avoid nan values for solar, wind. 144 rows dropped
# df= df[df["year"] >= 1985]

#looking at energy generation by source
# April
prod_list = ['coal_prod', 'nat_gas_prod',
       'crude_oil_prod', 'natural_gas_liquids_prod', 'total_ff_prod',
       'nuclear_prod', 'hydro_prod', 'geothermal_prod', 'solar_prod',
       'wind_prod', 'biomass_prod', 'total_renewable_prod',
       'total_primary_energy_prod']
mean_comparison(df,2008, prod_list,3,test=True)

# May
mean_comparison(df,2008, prod_list,4,test=True)

#looking at production source percentage of total energy produced
# April
prod_pc_list = ['coal_prcnt', 'ng_prcnt', 'c_oil_prcnt',
       'ngl_prcnt', 'tot_fossil_prcnt', 'nuke_prcnt', 'hydro_prcnt',
       'geo_prcnt', 'solar_prcnt', 'wind_prcnt', 'bio_prcnt',
       'tot_renew_prcnt']
mean_comparison(df,2008, prod_pc_list,3,test=True)
# May
mean_comparison(df,2008, prod_pc_list,4,test=True)

# looking at change in all of these
# April
prod_change = ['coal_proddiff', 'nat_gas_proddiff', 'crude_oil_proddiff',
       'natural_gas_liquids_proddiff', 'total_ff_proddiff', 'nuclear_proddiff',
       'hydro_proddiff', 'geothermal_proddiff', 'solar_proddiff',
       'wind_proddiff', 'biomass_proddiff', 'total_renewable_proddiff',
       'total_primary_energy_proddiff', 'coal_prcntdiff', 'ng_prcntdiff',
       'c_oil_prcntdiff', 'ngl_prcntdiff', 'tot_fossil_prcntdiff',
       'nuke_prcntdiff', 'hydro_prcntdiff', 'geo_prcntdiff', 'solar_prcntdiff',
       'wind_prcntdiff', 'bio_prcntdiff', 'tot_renew_prcntdiff']
mean_comparison(df,2008, prod_change,3,test=True)
# May
mean_comparison(df,2008, prod_change,4,test=True)

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Graphic View~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
#graphing trends for most recent years
dfr = df[df['year'] > 2017]

#grahping total use and change in total use by month
fig, axs=plt.subplots(2, figsize = (8, 10))

ax = axs[0]
tot_prior=ax.plot(dfr.date[:27], dfr.total_c[:27], 'c', label='Pre Covid')
tot_post=ax.plot(dfr.date[26:], dfr.total_c[26:], 'm', label='During Covid')
ax.set_xlabel('Time', fontsize = 18)
ax.set_ylabel('Energy Use, Trillion BTU',fontsize = 18)
ax.set_title('Total Energy Use',fontsize = 22, pad = 8)
ax.grid(axis='y')
ax.legend(shadow=1, fontsize='large',loc=1)
ax.tick_params(labelrotation=45, axis='x')
ax = axs[1]
diff_prior=ax.plot(dfr.date[:27], dfr.total_cdiff[:27], 'c', label='Pre Covid')
diff_post=ax.plot(dfr.date[26:], dfr.total_cdiff[26:], 'm', label='During Covid')
ax.set_xlabel('Time', fontsize = 18)
ax.set_ylabel('Change, Trillion BTU',fontsize = 18)
ax.set_title('Month-to-Month Change in Energy Use',fontsize = 22, pad = 8)
ax.grid(axis='y')
# ax.legend(shadow=1, fontsize='large',framealpha=1,loc=8)
ax.tick_params(labelrotation=45, axis='x')
plt.tight_layout()

#Graphing monthly use by sector, excluding generation sector
fig, axs=plt.subplots(2,2, figsize = (15, 10))

ax = axs[0,0]
industry_prior=ax.plot(dfr.date[:27], dfr.industrial_c[:27], 'c')
industry_post=ax.plot(dfr.date[26:], dfr.industrial_c[26:], 'm')
ax.set_xlabel('Time', fontsize = 18)
ax.set_ylabel('Industrial Use',fontsize = 18)
ax.set_title('Industrial Energy Use',fontsize = 22, pad = 8)
ax.grid(axis='y')
ax.tick_params(labelrotation=45, axis='x')

ax = axs[0,1]
transport_prior=ax.plot(dfr.date[:27], dfr.transportation_c[:27], 'c')
transport_post=ax.plot(dfr.date[26:], dfr.transportation_c[26:], 'm')
ax.set_xlabel('Time', fontsize = 18)
ax.set_ylabel('Transportation Use',fontsize = 18)
ax.set_title('Transportation Energy Use',fontsize = 22, pad = 8)
ax.grid(axis='y')
ax.tick_params(labelrotation=45, axis='x')

ax = axs[1,0]
residency_prior=ax.plot(dfr.date[:27], dfr.residential_c[:27], 'c')
residency_post=ax.plot(dfr.date[26:], dfr.residential_c[26:], 'm')
ax.set_xlabel('Time', fontsize = 18)
ax.set_ylabel('Residential Use',fontsize = 18)
ax.set_title('Residential Energy Use',fontsize = 22, pad = 8)
ax.grid(axis='y')
ax.tick_params(labelrotation=45, axis='x')

ax = axs[1,1]
commercial_prior=ax.plot(dfr.date[:27], dfr.commercial_c[:27], 'c')
commercial_post=ax.plot(dfr.date[26:], dfr.commercial_c[26:], 'm')
ax.set_xlabel('Time', fontsize = 18)
ax.set_ylabel('Commercial Use',fontsize = 18)
ax.set_title('Commercial Energy Use',fontsize = 22, pad = 8)
ax.grid(axis='y')
ax.tick_params(labelrotation=45, axis='x')

plt.tight_layout()


#Total use graph
fig, ax=plt.subplots(figsize = (12, 8))

pre_covid=ax.plot(dfr.date[:27], dfr.total_c[:27], 'c', label='Pre Covid')
during_covid=ax.plot(dfr.date[26:], dfr.total_c[26:], 'm', label='During Covid')
ax.set_xlabel('Time', fontsize = 18)
# fig.autofmt_xdate(which='both')
ax.set_ylabel('Energy Use, Trillion BTUs',fontsize = 18)
ax.set_title('Total Energy Use',fontsize = 22, pad = 8, loc='left')
ax.grid(axis='y')
ax.legend(shadow=1, fontsize='large',loc=0)

fig.autofmt_xdate(rotation=45)
#turning border box off
for spine in plt.gca().spines.values():
    spine.set_visible(False)
# plt.rcParams["font.family"] = "Palatino"

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
#fossil vs revewables graph
fig, ax=plt.subplots(figsize = (12, 8))

pc_fossil=ax.plot(dfr.date[:27], dfr.tot_fossil_prcnt[:27],'b', linestyle= '-.', label='Pre Fossil')
dc_fossil=ax.plot(dfr.date[26:], dfr.tot_fossil_prcnt[26:], 'r', linestyle= '-.', label='During Covid Fossil')

pc_renew=ax.plot(dfr.date[:27], dfr.tot_renew_prcnt[:27], 'c', linestyle= '--', label='Pre Renewable')
dc_renew=ax.plot(dfr.date[26:], dfr.tot_renew_prcnt[26:], 'm', linestyle= '--', label='During Covid Renewable')

ax.set_xlabel('Time', fontsize = 18)
# fig.autofmt_xdate(which='both')
ax.set_ylabel('Percentage',fontsize = 18)
ax.set_title('Percentage of Total Energy Generation',fontsize = 22, pad = 8, loc='left')
ax.grid(axis='y')
ax.legend(shadow=1, fontsize='large', bbox_to_anchor=(1.01, 1))
# plt.ylim((0,1))
plt.yticks(np.arange(0, 1.1, 0.1))
fig.autofmt_xdate(rotation=45)
#turning border box off
for spine in plt.gca().spines.values():
    spine.set_visible(False)

# Title: energy use data analysis
# Author: Doug
# Date Created: 8/18/2020
# Last Updated: 8/18/2020

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#in jupyter
# %matplotlib inline
from cleaning import first_diff, clean_to_pickle

# either load pickle:
df = pd.read_pickle('Data/energy_820.pkl', compression='zip')

# or load csv and manually run clean function:
clean_to_pickle(Data/use_gen_data.csv, pickle_df=False)

#making date variable for graphing, dropping first row
def make_date(val1, val2):
    '''
    For creating date variable from existing year, month data
    
    val1: year
    val2: month
    '''
    date_var = datetime.date(int(val1), int(val2), 1)
    return date_var
df['date'] = 0
for i in range(df.shape[0]):
    df.date[i] = make_date(df.year[i],df.month[i])

df.drop(0, axis=0, inplace = True)

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

#graphing trends for most recent years
dfr = df[df['year'] > 2017]

#grahping total use and change in total use by month
fig, axs=plt.subplots(2, figsize = (8, 10))

ax = axs[0]
gdp=ax.plot(dfr.date, dfr.total_c)
ax.set_xlabel('Time', fontsize = 18)
ax.set_ylabel('Energy Use',fontsize = 18)
ax.set_title('Total Energy Use',fontsize = 22, pad = 8)
ax.tick_params(labelrotation=45, axis='x')
ax = axs[1]
gdp=ax.plot(dfr.date, dfr.total_cdiff )
ax.set_xlabel('Time', fontsize = 18)
ax.set_ylabel('Use Change From Last Month',fontsize = 18)
ax.set_title('Monthly Change in Energy Use',fontsize = 22, pad = 8)
ax.tick_params(labelrotation=45, axis='x')
plt.tight_layout()

#Graphing monthly use by sector, excluding generation sector
fig, axs=plt.subplots(2,2, figsize = (15, 10))

ax = axs[0,0]
gdp=ax.plot(dfr.date, dfr.industrial_c)
ax.set_xlabel('Time', fontsize = 18)
ax.set_ylabel('Industrial Use',fontsize = 18)
ax.set_title('Industrial Energy Use',fontsize = 22, pad = 8)
ax.tick_params(labelrotation=45, axis='x')

ax = axs[0,1]
gdp=ax.plot(dfr.date, dfr.transportation_c)
ax.set_xlabel('Time', fontsize = 18)
ax.set_ylabel('Transportation Use',fontsize = 18)
ax.set_title('Transportation Energy Use',fontsize = 22, pad = 8)
ax.tick_params(labelrotation=45, axis='x')

ax = axs[1,0]
gdp=ax.plot(dfr.date, dfr.residential_c)
ax.set_xlabel('Time', fontsize = 18)
ax.set_ylabel('Residential Use',fontsize = 18)
ax.set_title('Residential Energy Use',fontsize = 22, pad = 8)
ax.tick_params(labelrotation=45, axis='x')

ax = axs[1,1]
gdp=ax.plot(dfr.date, dfr.commercial_c)
ax.set_xlabel('Time', fontsize = 18)
ax.set_ylabel('Commercial Use',fontsize = 18)
ax.set_title('Commercial Energy Use',fontsize = 22, pad = 8)
ax.tick_params(labelrotation=45, axis='x')

plt.tight_layout()


'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~Generation analysis~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''


#drop values prior to 1985 to avoid nan values for solar, wind. 144 rows dropped
df= df[df["year"] >= 1985]
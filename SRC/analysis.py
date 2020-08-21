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
df['date'] = 0
for i in range(df.shape[0]):
    dt_string = str(df.year[i])+ '-' + str(df.month[i])
    df.date[i] = pd.Period(dt_string, 'M')
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

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~Generation analysis~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''


#drop values prior to 1985 to avoid nan values for solar, wind. 144 rows dropped
df= df[df["year"] >= 1985]
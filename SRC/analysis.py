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
'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~Consumption analysis~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
# average monthly for comparisson
df.groupby('month').mean()
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
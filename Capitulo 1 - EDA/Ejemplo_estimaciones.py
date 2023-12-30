
# %%
import pandas as pd 
import numpy as np
import os
import wquantiles
from scipy import stats

# %%

p = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','data'))
print(p)

# %%

state  = pd.read_csv(p+'\state.csv')
state

# %%
state['Población'].mean()
# %%
stats.trim_mean(state['Población'], 0.1) # trim ignora el 10 de cada extremo
# %%
state['Población'].median()
# %%
np.average(state['Homicidios'], weights=state['Población'])
# %%
wquantiles.median(state['Homicidios'], weights=state['Población'])
# %%

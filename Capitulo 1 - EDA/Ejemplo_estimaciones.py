
# %%
import pandas as pd 
import numpy as np
import os
import wquantiles

from statsmodels import robust
from scipy import stats

#%%

import common
from pathlib import Path

#DATA = common.dataDirectory()
DATA = Path().resolve() / 'data'
DATA

# %%

p = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','data'))
print(p)

# %%

state  = pd.read_csv(p+'\state.csv')
state

# %%

# Media 
state['Población'].mean()

# %%

# Media truncada
stats.trim_mean(state['Población'], 0.1) # trim ignora el 10 de cada extremo

# %%

# Mediana
state['Población'].median()

# %%

# Media ponderada
np.average(state['Homicidios'], weights=state['Población'])

# %%

# Mediana ponderada
wquantiles.median(state['Homicidios'], weights=state['Población'])

# %%

# desvición estándar
state['Población'].std()
# %%

# IQR
state['Población'].quantile(0.75) - state['Población'].quantile(0.25)

# %%

# MAD
robust.scale.mad(state['Población'])

# %%

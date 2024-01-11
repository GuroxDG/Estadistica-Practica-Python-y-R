
# %%

import matplotlib.pylab as plt
import numpy as np
import os
import pandas as pd 
import wquantiles
import seaborn as sns

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

# Percentiles
state['Homicidios'].quantile([0.05, 0.25, 0.5, 0.75, 0.95])


# %%

# Tabla, Percentiles de tasa de omicidios por estados
percentages = [0.05, 0.25, 0.5, 0.75, 0.95]
df = pd.DataFrame(state['Homicidios'].quantile(percentages))
df.index = [f'{p * 100}%' for p in percentages]
print(df.transpose())

# %%

#Boxplot
ax = (state['Población']/1_000_000).plot.box(figsize=(3, 4))
ax.set_ylabel('Population (millions)')

plt.tight_layout()
plt.show()


# %%

# Tabla de frecuencias
binnedPopulation = pd.cut(state['Población'], 10)
binnedPopulation

# %%

binnedPopulation.value_counts()

# %%

binnedPopulation.name = 'binnedPopulation'
df = pd.concat([state, binnedPopulation], axis=1)
df = df.sort_values(by='Población')

groups = []
for group, subset in df.groupby(by='binnedPopulation'):
    groups.append({
        'BinRange': group,
        'Count': len(subset),
        'States': ','.join(subset.Abrebiatura)
    })

print(pd.DataFrame(groups))


# %%

# Histograma

ax = (state['Población']/1_000_000).plot.hist(figsize=(4,4))
ax.set_xlabel('Población (millions)')

# %%

ax = state['Homicidios'].plot.hist(density=True, xlim=[0, 12], bins=(range(1,12)))
state['Homicidios'].plot.density(ax=ax)
ax.set_xlabel('Murder rate (100.000)')

# %%

dfw  = pd.read_csv(p+'\dfw_airline.csv')
dfw

# %%

ax = dfw.transpose().plot.bar(figsize=(4, 4), legend=False)
ax.set_xlabel('Cause of delay')
ax.set_ylabel('Count')

# %%

sp500_sym = pd.read_csv(p+'\sp500_sectors.csv')
sp500_px = pd.read_csv(p+'\sp500_data.csv.gz', index_col=0)

# %%
telecomSymbols = sp500_sym[sp500_sym['sector'] == 'telecommunications_services']['symbol']

telecom = sp500_px.loc[sp500_px.index >= '2012-07-01', telecomSymbols]
telecom.corr()
print(telecom)

# %%

etfs = sp500_px.loc[sp500_px.index > '2012-07-01', 
                    sp500_sym[sp500_sym['sector'] == 'etf']['symbol']]
print(etfs.head())

# %%

fig, ax = plt.subplots(figsize=(5, 4))
ax = sns.heatmap(etfs.corr(), vmin=-1, vmax=1, 
                 cmap=sns.diverging_palette(20, 220, as_cmap=True),
                 ax=ax)

plt.tight_layout()
plt.show()


# %%

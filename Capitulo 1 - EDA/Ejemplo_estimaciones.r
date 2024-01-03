library(readr)

# root
print(getwd())

s = paste(getwd(),"/data/state.csv", sep="")
print(s)

p = "C:/Users/gurox/Estudios/Python/Estadística Práctica Python y R/data/state.csv"
print(p)

#install.packages("str_diff")
#library(str_diff)

s == p
tolower(p) == tolower(s)

# state  <- read.csv(s)
state <- read_csv(p)
state

mean(state[['Población']])

# Media truncada
mean(state[['Población']], trim=0.1) # trim ignora el 10 de cada extremo

median(state[['Población']])

#install.packages("matrixStats")
library("matrixStats")

# Media ponderada
weighted.mean(state[['Homicidios']], w=state[['Población']])

# Mediana ponderada
weightedMedian(state[['Homicidios']], w=state[['Población']])

# Desviación estandar
sd(state[['Población']])

# Rango Intercuartilico
IQR(state[['Población']])

#MAD
mad(state[['Población']])

# Percentiles
quantile(state[['Homicidios']], p=c(.05, .25, .5, .75, .95))

#Boxplot
boxplot(state[['Población']]/1000000, ylab='Population (millions)')

# Tabla de frecuencias
breaks <- seq(from=min(state[['Población']]), to=max(state[['Población']]), length=11)
breaks

pop_freq <- cut(state[['Población']], breaks=breaks, right=TRUE, include.lowest=TRUE)
pop_freq

table(pop_freq)

# Histogram
options(scipen=5)
hist(state[['Población']], breaks=breaks)

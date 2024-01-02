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

mean(state[['Población']], trim=0.1) # trim ignora el 10 de cada extremo

median(state[['Población']])

#install.packages("matrixStats")
library("matrixStats")

weighted.mean(state[['Homicidios']], w=state[['Población']])

weightedMedian(state[['Homicidios']], w=state[['Población']])

# Desviación estandar
sd(state[['Población']])

# Rango Intercuartilico
IQR(state[['Población']])

#MAD
mad(state[['Población']])

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

# Density
hist(state[['Población']], freq=FALSE)
lines(density(state[['Homicidios']]), lwd=3, col='blue')

# Data
s = paste(getwd(),"/data/dfw_airline.csv", sep="")
print(s)
dfw <- read.csv(s)
dfw

# Diagrama de barras
barplot(as.matrix(dfw)/6, ces.axis=0.8, cex.names=0.7, xlab='Cause of delay', ylab='Count')

# Correlación
PSDS_PATH <- file.path(dirname(dirname(getwd())))
print(PSDS_PATH)

p = paste(getwd(),"/data/sp500_data.csv.gz", sep="")
sp500_px <- read.csv(p, row.names=1)

p = paste(getwd(),"/data/sp500_sectors.csv", sep="")
sp500_sym <- read.csv(p, stringsAsFactors = FALSE)

# Correlación entre variables

telecom <- sp500_px[, sp500_sym[sp500_sym$sector == 'telecommunications_services', 'symbol']]
telecom <- telecom[row.names(telecom) > '2012-07-01',]
telecom_cor <- cor(telecom)
telecom_cor

# Diagrama de correlación

etfs <- sp500_px[row.names(sp500_px) > '2012-07-01', 
                 sp500_sym[sp500_sym$sector == 'etf', 'symbol']]

#install.packages("corrplot")
library('corrplot')

corrplot(cor(etfs), method='ellipse')

# Diagrama de dispersión

plot( telecom$T, telecom$VZ, xlab="ATT (T)", ylab="Verizon (VZ)")


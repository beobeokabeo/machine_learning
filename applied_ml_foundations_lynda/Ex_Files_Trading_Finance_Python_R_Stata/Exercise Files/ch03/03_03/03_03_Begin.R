#03_03_Begin
#Installing Quantmod
#if(require("quantmod",quietly=TRUE))
#  install.packages("quantmod",dependencies=TRUE,repos=c(CRAN="http://cran.rstudio.com"))
library("quantmod")

getSymbols('AAPL')
barChart(AAPL, subset='last 28 days')
rm(AAPL)


getSymbols('MSFT', subset='last 100 days')
chartSeries(MSFT)
addMACD()
addBBands()
add_RSI()
add_EMA(n=200)
MSFT
chartSeries(MSFT, subset='last 60 days')
addMACD()
addBBands()

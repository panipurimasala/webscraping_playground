# options(repos = "https://cloud.r-project.org")
`%T>%` <- magrittr::`%T>%`

## We're Firefox now (or at least some magic words)
UA <- httr::user_agent("Mozilla/5.0 Firefox")

html <- httr::GET("https://finance.yahoo.com/quote/AMD/financials", UA) 
# %T>%
   print(html)
# options(repos = "https://cloud.r-project.org")
# install.packages("languageserver")
# install.packages("evaluate")
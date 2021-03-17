import yfinance

df = yfinance.download('GLW', start = '2020-02-01', end = '2020-02-29')
df.to_csv('GLW2020.csv')
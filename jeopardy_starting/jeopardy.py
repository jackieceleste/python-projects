import pandas as pd
pd.set_option('display.max_colwidth', -1)


#read tha data from jeopardy.csv
df=pd.read_csv("jeopardy.csv")
print(df[' Category'].head())
import csv
import pandas as pd
pd.set_option('display.max_rows',20)
pd.set_option('display.max_columns',None)
pd.set_option('display.width',None)
pd.set_option('display.max_colwidth',None)
df=pd.read_csv("sales_data_sample.csv",encoding='latin1')
print(df)

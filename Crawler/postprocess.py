import pandas as pd
import math

df = pd.read_csv("india.csv",encoding= 'unicode_escape')
print("Before cleaning: length =",len(df))

df = df.drop_duplicates(subset=['name'], keep=False)

counter=0
for count,rows in enumerate(df['prefix']):
    try:
        if  pd.isnull(df['prefix'][count]) or pd.isnull(df['name'][count]) or df['name'][count].isnumeric()==True or df['prefix'][count].isnumeric()==True:
            df.drop(count,axis=0,inplace=True)
            counter+=1
    except:
        pass

print("After cleaning: length =",len(df))
df.to_csv("clean_database.csv",index=False)
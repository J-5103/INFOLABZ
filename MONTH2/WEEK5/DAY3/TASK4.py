import requests
import pandas as pd

data=requests.get("https://isro.vercel.app/api/spacecrafts")
mydata=data.json()

name=[]
id=[]

for i in range(0,len(mydata["spacecrafts"])):
    name.append(mydata["spacecrafts"][i]["name"])
    id.append(mydata["spacecrafts"][i]["id"])

print(name)

spacecraft_series=pd.Series(name,index=id)
print(spacecraft_series)
print(spacecraft_series.head())
print(spacecraft_series.tail())
print(spacecraft_series.sample(5))
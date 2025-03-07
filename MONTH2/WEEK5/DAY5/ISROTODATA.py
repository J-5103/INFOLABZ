import pandas as pd
import requests

data=requests.get("https://isro.vercel.app/api/spacecrafts")
mydata=data.json()

name=[]
id=[]
for i in range(0,len(mydata)):
    name.append(mydata["spacecrafts"][i]["name"])
    id.append(mydata["spacecrafts"][i]["id"])

df=pd.DataFrame(name,index=id)
print(df)
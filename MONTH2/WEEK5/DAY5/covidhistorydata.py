import requests
import pandas as pd

data=requests.get("https://api.rootnet.in/covid19-in/stats/history")
mydata=data.json()

records=[]

for data in mydata["data"]:
    date=data["day"]
    regional=data["regional"]
    row={}
    row["date"]=date
    for i in regional:
        loc=i["loc"]
        cases=i["totalConfirmed"]
        row[loc]=cases
    records.append(row)

df=pd.DataFrame(records)
print(df)

df.fillna(0,inplace=True)
print(df)

df.to_csv("coviddata.csv")
print("coviddata.csv is saved")
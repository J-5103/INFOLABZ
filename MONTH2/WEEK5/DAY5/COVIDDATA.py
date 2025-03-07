import pandas as pd
import requests

data=requests.get("https://api.rootnet.in/covid19-in/stats/latest")
mydata=data.json()

dict={"states":[],"cases":[]}

for i in range(0,len(mydata["data"]["regional"])):
    states=mydata["data"]["regional"][i]["loc"]
    cases=mydata["data"]["regional"][i]["totalConfirmed"]
    dict["states"].append(states)
    dict["cases"].append(cases)

print(dict)

df=pd.DataFrame(dict)
print(df)


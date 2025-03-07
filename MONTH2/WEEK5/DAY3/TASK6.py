import pandas as pd
import requests
import numpy as np

data=requests.get("https://api.mfapi.in/mf")
mydata=data.json()

scheme_name=[]


for i in range(0,len(mydata)):
    scheme_name.append(mydata[i]["schemeName"])


scheme_id=np.random.randint(0,len(mydata),36616)

scheme_series=pd.Series(scheme_name,index=scheme_id)
print(scheme_series)
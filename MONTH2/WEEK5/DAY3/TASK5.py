import requests
import pandas as pd

data=requests.get("https://api.rootnet.in/covid19-in/stats/latest")
mydata=data.json()

c_states=[]
s_cases=[]
for i in range(0,len(mydata["data"]["regional"])):
    c_states.append(mydata["data"]["regional"][i]["loc"])
    s_cases.append(mydata["data"]["regional"][i]["totalConfirmed"])

#covid series
covid_series=pd.Series(c_states,index=s_cases)
print("covid series:",covid_series)

#cases mean
cases_mean=pd.Series(s_cases).mean()
print("cases mean:",cases_mean)

#cases sort
cases_sort=pd.Series(s_cases).sort_values(ascending=True)
print("sorted cases:",cases_sort)

#cases sum
cases_sum=pd.Series(s_cases).sum()
print("sum of cases:",cases_sum)

#cases top 5
top5_case=pd.Series(s_cases).head()
print("top 5 cases:",top5_case)

#cases last 5
last5_case=pd.Series(s_cases).tail()
print("last 5 cases:",last5_case)

#cases random 5
random_case=pd.Series(s_cases).sample(5)
print("random 5 cases:",random_case)
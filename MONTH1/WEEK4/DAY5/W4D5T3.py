
import matplotlib.pyplot as plt
import requests


#Create graphs as shown in below output,  to compare for state wise confirmed cases and state wise death cases from below API.

data = requests.get(" https://api.rootnet.in/covid19-in/stats/latest")
mydata=data.json()

states=[]
death=[]
confirmed=[]

for i in range(0,len(mydata["data"]["regional"])):
    states.append(mydata["data"]["regional"][i]["loc"])
    death.append(mydata["data"]["regional"][i]["deaths"])
    confirmed.append(mydata["data"]["regional"][i]["totalConfirmed"])

print(states)
print(death)
print(confirmed)

fig,axes = plt.subplots(1,2,figsize=(12,6),gridspec_kw={'wspace':1.5})
axes[0].barh(states,confirmed,color="blue")
axes[0].set_title("COVID-19 Confirmed Cases by States")
axes[0].set_xlabel("Confirmed")

axes[1].barh(states,death,color="red")
axes[1].set_title("COVID-19 Death Cases by States")
axes[1].set_xlabel("Deaths")
plt.show()
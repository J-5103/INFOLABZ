import matplotlib.pyplot as plt
import requests

#CREATE HORIZONTAL BAR GRAPH ( Y AXES STATE NAMES, X AXES TOTAL CASES ) FROM BELOW API ( API/REQUESTS PACKAGE + BAR GRAPH )

data=requests.get("https://api.rootnet.in/covid19-in/stats/latest")
mydata=data.json()

states=[]
total_cases=[]

for i in range(0,len(mydata["data"]["regional"])):
    states.append(mydata["data"]["regional"][i]["loc"])
    total_cases.append(mydata["data"]["regional"][i]["totalConfirmed"])

plt.xticks([1000000 * i for i in range(0,20)],[f"{i}M" for i in range(0,20)])
plt.barh(states,total_cases)
plt.show()


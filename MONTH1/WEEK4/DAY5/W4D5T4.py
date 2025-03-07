from operator import index

import matplotlib.pyplot as plt
import requests

#Allow user to insert correct names of 4 states, print 4 graphs ( 2 in first row, 2 in second row )

data=requests.get("https://api.rootnet.in/covid19-in/stats/latest")
mydata=data.json()

states=[]
death=[]
confirmed=[]

for i in range(0,len(mydata["data"]["regional"])):
    print(mydata["data"]["regional"][i]["loc"])
    states.append(mydata["data"]["regional"][i]["loc"])
    death.append(mydata["data"]["regional"][i]["deaths"])
    confirmed.append(mydata["data"]["regional"][i]["totalConfirmed"])

selected_states=[]
selected_death=[]
selected_confirmed=[]
for _ in range(4):
    user_enter_state=input("enter state name:")
    if user_enter_state==states:
        index=states.index(states)
        selected_states.append(user_enter_state)
        selected_death.append(death[index])
        selected_confirmed.append(confirmed[index])
else:
    print("invalid state name ! try again")

print(selected_states)
print(selected_death)
#
# fig,axes=plt.subplots(2,2,figsize=(10,8))
#
# axes[0,0].bar(selected_states,selected_confirmed,color="red")
# axes[0,0].set_title("States v/s confirmed")
# axes[0,0].set_xlabel("states")
# axes[0,0].set_ylabel("confirmed case")
#
#
# axes[0,1].bar(selected_states,selected_death,color="green")
# axes[0,1].set_title("States v/s death")
# axes[0,1].set_xlabel("states")
# axes[0,1].set_ylabel("deaths")
#
# axes[1,0].pie(selected_confirmed,labels=selected_states,autopct="%.2f%%")
# axes[1,0].set_title("selected Confirmed")
#
#
# axes[1,1].pie(selected_death,labels=selected_states,autopct="%.2f%%")
# axes[1,1].set_title("selected deaths")
#
# plt.tight_layout()
# plt.show()

import matplotlib.pyplot as plt
import requests


#Allow user to insert 5 different pincodes. Print bar graph and bar graph and pie graph in single column
# ( up and down ) to compare. Which pincode covers how many area ( count ).
areas=[]
pincode=[]

for _ in range(5):
    user_enter_pincode = input("enter unique pincode:")
    data = requests.get("https://api.postalpincode.in/pincode/" + user_enter_pincode)
    mydata = data.json()
    pincode.append(user_enter_pincode)
    for j in range(0,len(mydata)):
        arra=mydata[j]["PostOffice"]
        areas.append(len(arra))


print(areas)

fig,ax=plt.subplots(2,1,figsize=(10,8),gridspec_kw={'hspace':0.5})

ax[0].bar(pincode,areas)
ax[0].set_title("pincode v/s areas")
ax[0].set_xlabel("pincode")
ax[0].set_ylabel("areas")

ax[1].pie(areas,labels=pincode,autopct="%.2f%%")
ax[1].set_title("areas of pincode")

plt.show()

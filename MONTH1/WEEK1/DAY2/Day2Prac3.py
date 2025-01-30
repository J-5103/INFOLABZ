import requests

data = requests.get("https://isro.vercel.app/api/spacecrafts")
mydata = data.json()

#Q1 Allow user to enter ID. Print that space craft’s name
user_enter_id = str(input("Enter ID:"))
for i in range(0,len(mydata["spacecrafts"])):
    if user_enter_id==str(mydata["spacecrafts"][i]["id"]):
        print("Spacecraft name:",mydata["spacecrafts"][i]["name"])
        break
else:
    print("not found")

#Q2 Allow user to insert name of space craft. Print that spacecraft is launched by isro or not.
user_enter_name= str(input("enter Spacecraft name:"))
for i in range(0,len(mydata["spacecrafts"])):
    if user_enter_name==str(mydata["spacecrafts"][i]["name"]):
        print("yes,this spacecraft is launched by isro")
        break
else:
    print("no,this spacecraft is not launched by isro")

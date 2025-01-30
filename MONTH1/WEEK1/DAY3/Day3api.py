import requests

data = requests.get("http://universities.hipolabs.com/search?country=india")
mydata = data.json()

##print the university data in list

university = []

for i in range(0,len(mydata)):
    university.append(mydata[i]["name"])

print(university)

##print user new university with mydata

user_enter_name = input("enter university name:")

if user_enter_name in university:
        print(" university already exists")
else:
  mydata.append(user_enter_name)
  print(university)
  print("university added successfully")






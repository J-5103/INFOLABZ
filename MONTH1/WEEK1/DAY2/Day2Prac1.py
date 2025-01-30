import requests

data = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population")
mydata=data.json()

##Q1 how many key are in the api
key_count = len(mydata.keys())
print(f"{key_count} keys are in this api")

##Q1 print names of all main keys
print(mydata.keys())

##Q3 print 2021
print(mydata["data"][1]["Year"])

##Q4 how many years of data
print(len(mydata["data"]))

##Q5 for loop
count=0
for i in mydata["data"]:
    print(count+1,"year",mydata["data"][count]["Year"],"","POPULATION",mydata["data"][count]["Population"])
    count+=1

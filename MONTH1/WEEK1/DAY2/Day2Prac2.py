import requests

data = requests.get("http://universities.hipolabs.com/search?country=india")
mydata = data.json()

##Q1 how maany keys in this api
##this api is a list

##Q2 How many univercities data is available
print("in this api",len(mydata),"univercites data is available")

##Q3 atharv college of eng.
print("print atharv colg eng.:",mydata[0]["name"])

##for loop
for i in range(0,len(mydata)):
    print(i,")","univercity name:",mydata[i]["name"],"\n","    website:",mydata[i]["web_pages"][0],"\n","    region:",mydata[i]["state-province"])
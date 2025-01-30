import requests

data = requests.get("https://isro.vercel.app/api/spacecrafts")
mydata = data.json()

mydict = {}

for i in range(0,len(mydata["spacecrafts"])):
    mydict[ mydata["spacecrafts"][i]["id"]] = mydata["spacecrafts"][i]["name"]

print(mydict)

import requests

data=requests.get("https://api.postalpincode.in/pincode/380009")
mydata=data.json()

##how many keys in api
##this api is list

##print Ashram road
print("print Ashram road:",mydata[0]["PostOffice"][0]["Name"])

##count areas under this pin
print("Total areas of 380009 pin:",len(mydata[0]["PostOffice"]))

##print areas name
count=0
for i in mydata[0]["PostOffice"]:
    print(count+1,"area names:",mydata[0]["PostOffice"][count]["Name"])
    count+=1
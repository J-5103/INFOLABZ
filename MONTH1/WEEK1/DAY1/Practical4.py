import requests

data=requests.get(" https://api.mfapi.in/mf")
mydata=data.json()

##total numbers of key in api
##this api is list

##print total number of mutual funds
total_mutual_funds = len(mydata)
print("Total number of mutual funds:",total_mutual_funds)

##print name of first mutual fund
print("name of first mutual fund:",mydata[0]["schemeName"])

##print scheme name and code
count=0
for i in mydata:
    print(count+1,":","schemecode:",mydata[count]["schemeCode"]," ","schemeName:",mydata[count]["schemeName"])
    count+=1

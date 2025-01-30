import requests

data=requests.get(" https://api.coindesk.com/v1/bpi/currentprice.json")
mydata=data.json()

##how many keys are there in the api
key = mydata.keys()
print("Total keys name:",key)

##print total count of main keys
key_count = len(key)
print("Total count of main keys:",key_count)

##print bitcoin price in usd
print("Bitcoin price in USD:",mydata["bpi"]["USD"]["rate"])
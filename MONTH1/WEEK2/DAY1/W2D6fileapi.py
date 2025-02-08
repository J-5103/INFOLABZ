import requests


data = requests.get("https://isro.vercel.app/api/spacecrafts")
mydata = data.json()

##print api data into list
apilist = []

for i in range(0,len(mydata["spacecrafts"])):
    apilist.append(mydata["spacecrafts"][i]["name"])
print(apilist)

##write list into file

file= open("apilist.txt", "w")

for i in apilist:
    file.write(f"{i}\n")
file.close()



import requests

#q1 Allow user to input country name
user_enter_country=str(input("enter country name:"))


data = requests.get("http://universities.hipolabs.com/search?country=" + user_enter_country)
mydata = data.json()

#Q2 Print number of universities in that country
print("total number of universities in this country:",len(mydata))

#Q3 Print name and websites of all universities of that country using for loop.
for i in range(0,len(mydata)):
    print(i,")","univercity name:",mydata[i]["name"],"\n","    website:",mydata[i]["web_pages"][0],)
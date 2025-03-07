import matplotlib.pyplot as plt
import requests

#Completely dynamic graph. Allow user to insert names of countries until user enter stop. When user enters stop,
#print bar graph of countries vs total universities in that country of all inserted countries.

country=[]
total_uni=[]

while True:
    user_enter_country=input("enter country name:")
    if user_enter_country!="stop":
        url=("http://universities.hipolabs.com/search?country=")+user_enter_country
        data=requests.get(url)
        mydata=data.json()
        country.append(user_enter_country)
        total_uni.append(len(mydata))
    else:
        print(country)
        print(total_uni)
        plt.bar(country,total_uni)
        plt.xlabel("country")
        plt.ylabel("University")
        plt.title("University Analysis")
        plt.grid(alpha=0.5)
        plt.show()
        break


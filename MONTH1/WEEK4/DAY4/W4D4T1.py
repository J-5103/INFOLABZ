
import matplotlib.pyplot as plt
import requests

#From above API create pie chart of count of universities in following countries.
#India, Pakistan, China, Nepal, Japan

country=["india","pakistan","china","nepal","japan"]
total_uni=[]

for i in country:
    url=f"http://universities.hipolabs.com/search?country={i}"
    response=requests.get(url)
    mydata=response.json()
    total_uni.append(len(mydata))

plt.pie(total_uni,labels=country,autopct="%.2f%%")
plt.title("University Analysis")
plt.show()

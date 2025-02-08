import requests
import numpy as np
import random


data = requests.get("http://universities.hipolabs.com/search?country=india")
mydata = data.json()

#a. Fetch the list of universities.

university_arr = np.array([])
for i in range(0,len(mydata)):
    university_arr=np.append(university_arr,mydata[i]["name"])
print(university_arr)

#b. Determine the number of universities.

print("total university:",len(university_arr))

#c. Generate unique random numbers as indices.
indices = random.sample(range(1,463),462)
print(indices)

#d. Store university names in a NumPy array.
for i in range(0,len(mydata)):
    university_arr=np.append(university_arr,mydata[i]["name"])
#print(university_arr)

#e. Create a NumPy structured array with the generated indices and university names.
# university_arry=np.append(indices,university_arr)
# print(university_arry)

##2.a. Fetch the university data from the API.
print(mydata)

##2.b. Generate unique random numbers as Unicode indices.

##2.c. Store university names in a NumPy array.
for i in range(0,len(mydata)):
    university_arr=np.append(university_arr,mydata[i]["name"])
#print(university_arr)

##2.d. Save the NumPy array to an Excel file using numpy.savetxt) in CSV format.
np.savetxt("data.csv", university_arr, fmt="%s")

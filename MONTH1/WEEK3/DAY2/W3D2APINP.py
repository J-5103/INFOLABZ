import requests
import numpy as np

data = requests.get("https://api.rootnet.in/covid19-in/stats/latest")
mydata = data.json()
print(mydata.keys())
print(mydata.values())

#cases append in to a list

cases=[]
for i in range(0,len(mydata["data"]["regional"])):
    cases.append(mydata["data"]["regional"][i]["totalConfirmed"])
print(cases)

#convert list into a array

cases_arr = np.array(cases)
print(cases_arr)

#sum of all cases

sum = np.sum(cases_arr)
print("sum of total cases:",sum)

#print 100000 above cases

index = np.where(cases_arr> 100000)
print(cases_arr[index])
#
# #print index of user entered value
# user_enter_case= int(input("enter case value:"))
# index2 = np.where(user_enter_case==cases_arr)
# print(index2[0])
#
# #average of all cases
# avg = np.mean(cases_arr)
# print("average of all cases:",avg)

#print top 10 highest cases
cases_arr2=np.sort(cases_arr)[::-5 ]
print(cases_arr2)

#replace the 100000 less value with -1

cases_arr[cases_arr<100000]=-1
print(cases_arr)

#print maximum and minimum

maximum = np.argmax(cases_arr)
#print(maximum)
print("maximum:",cases_arr[maximum])

minimum = np.argmin(cases_arr)
#print(minimum)
print("minimum:",cases_arr[minimum])

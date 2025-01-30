import requests

data = requests.get("https://api.rootnet.in/covid19-in/stats/latest")
mydata = data.json()
#
# ## main keys in api
# print(mydata.keys())
# print(len(mydata))
#
# ## how many states data
# print(len(mydata["data"]["regional"]))
#
# ##print data using for loop
# for i in range(0,len(mydata["data"]["regional"])):
#     print(i+1,")"," state name:",mydata["data"]["regional"][i]["loc"],"   no of indian cases:",mydata["data"]["regional"][i]["confirmedCasesIndian"],"   no of forein cases:",mydata["data"]["regional"][i]["confirmedCasesForeign"])
#
# ##print how many states are having cases > 1000000
# count = 0
# for i in range(0,len(mydata["data"]["regional"])):
#     if mydata["data"]["regional"][i]["confirmedCasesIndian"] > 1000000:
#         count+=1
# print(count)
#
# ##user range with states name
#
# minrange = int(input("enter minrange:"))
# maxrange = int(input("enter maxrange:"))
# for i in range(0,len(mydata["data"]["regional"])):
#     if  mydata["data"]["regional"][i]["confirmedCasesIndian"] > minrange and  mydata["data"]["regional"][i]["confirmedCasesIndian"] < maxrange:
#         print(mydata["data"]["regional"][i]["loc"])


##print highets cases (digits)
# max_cases = mydata["data"]["regional"][0]["totalConfirmed"]
# for i in range(0,len(mydata["data"]["regional"])):
#     if max_cases < mydata["data"]["regional"][i]["totalConfirmed"]:
#        max_cases=mydata["data"]["regional"][i]["totalConfirmed"]
#
# print(max_cases)
#
# ##print name of the state which has highest cases
#
# for i in range(0,len(mydata["data"]["regional"])):
#     if max_cases == mydata["data"]["regional"][i]["totalConfirmed"]:
#         print(mydata["data"]["regional"][i]["loc"])

##which state is having lowest death case
# lowest_death_case = mydata["data"]["regional"][0]["deaths"]
# for i in range(0,len(mydata["data"]["regional"])):
#     if lowest_death_case > mydata["data"]["regional"][i]["deaths"]:
#         lowest_death_case=mydata["data"]["regional"][i]["deaths"]
#
#
# for i in range(0,len(mydata["data"]["regional"])):
#     if lowest_death_case == mydata["data"]["regional"][i]["deaths"]:
#         print(mydata["data"]["regional"][i]["loc"],":",lowest_death_case)
#
##allow user to enter states ,print death rate of that state in percentage
user_enter_state = input("enter your state:")

for i in range(0,len(mydata["data"]["regional"])):
    if user_enter_state==mydata["data"]["regional"][i]["loc"]:
        print(f"{user_enter_state} death rate:{(mydata["data"]["regional"][i]["deaths"]*100)/mydata["data"]["regional"][i]["totalConfirmed"]}%")
        break
else:
    print("state is not exist")














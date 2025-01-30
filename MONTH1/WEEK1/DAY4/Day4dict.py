# mydict = {
#     "name" : "jimi",
#     "age" : 22,
#     "address" : "ahemdabad",
#     "college" : "modasa"
# }
#
# #user enter key and print value
# user_enter_key = input("enter your key:")
# for i in mydict.keys():
#     if user_enter_key == i:
#         print(mydict[i])
#         break
# else:
#     print("key not found")


##if

mydict2 = {
    "ahemdabad" : 150,
    "surat" : 152,
    "patan" : 620,
    "modasa" : 56,
    "bopal" : 89
}

Is_stop = False

while True:
    if Is_stop==False:
        user_enter_key = input("enter your key:")
        if user_enter_key in mydict2:
            print("this key is already exists")
            break
        user_enter_value = int(input("enter your value:"))
        mydict2[user_enter_key] = user_enter_value
        print("new key and value is added successfully")
        print(mydict2)
    else:
        break

    stop = input("do you want to stop this process(Y/N):")
    if stop=="N":
        Is_stop = False
    elif stop =="Y":
        Is_stop =True
    else:
        print("invalid input")


















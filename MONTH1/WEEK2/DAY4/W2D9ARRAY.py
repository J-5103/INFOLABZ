import numpy as np

# #print list for create array
# list1 =  []
# for i in range(1,101):
#     list1.append(i)
#
# print(list1)
#
# #convert list into array
# arr1 = np.array(list1)
# print(arr1)
# print(arr1.shape)
#
# #change the shape of arr1
# arr2 = arr1.reshape(10,10)
# print(arr2)
#
# #change arr2 into 3D array
# arr3 = arr1.reshape(2,5,10)#2 is 2d array,row,col
# print(arr3)
# print(len(arr3))
#
# #arange the array with out create a list
# arr4 = np.arange(1,101)
# print(arr4)
# print(arr4)

#print array with random numbers
arr5 = np.random.randint(100000,200000,(500))
arr6 = arr5.reshape(5,10,10)
print(arr6)

user_enter_num = int(input("enter a random number:"))
found=False
for i in arr6:
    for j in i:
        for k in j:
            if user_enter_num==k:
                print("number is found")
                found=True
                break
if found==False:
    print("number is not found")





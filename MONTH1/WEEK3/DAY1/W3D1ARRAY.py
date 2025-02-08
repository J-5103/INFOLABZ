import numpy as np

arr = np.random.randint(1000,10000,(10,10,10))
print(arr)
##using for loop
#user_enter_price = int(input("enter a price:"))
# is_found = False
#
# for i in arr:
#     for j in i:
#         for k in j:
#             if user_enter_price==k:
#                 print("price found:",k)
#                 is_found=True
#                 break
#
# if is_found==False:
#      print("price not found")

##using numpy library
#
# index = np.where(arr==user_enter_price)
#
# if index[0].size>0:
#     print("price found at index:",index[0][0])
# else:
#     print("price not found")

##print value between 1000 to 5000
index = np.where((arr>=1000) & (arr<=5000))
print(arr[index])

#print max and min
maximum = np.max(arr)
print("maximum:",maximum)

index = np.where(arr == maximum )
print(index)

minimum = np.min(arr)
print("minimum:",minimum)

id = np.where(arr == minimum)
print(id)


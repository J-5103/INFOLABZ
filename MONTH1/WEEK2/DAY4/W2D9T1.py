import numpy as np

##array manipulation
##1)create 5*5 numpy array with integers between 10 and 50

arr =np.random.randint(10,50,25)
print(arr)
arr1 = arr.reshape(5,5)
print(arr1)

##2) replace all even numbers in the array with-1
# arr1[arr1 % 2 ==0]=-1
# print(arr1)

##3) reshape the array into a 1d array and then back into a 5*5 array
arr2 = arr1.reshape(25)
print(arr2)
print(arr2.reshape(5,5))





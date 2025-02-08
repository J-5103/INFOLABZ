import numpy as np


arr1 = np.array([4,5,6,7])
print(arr1)

arr2 = np.array([[4,5,6,8],[5,6,8,7]])
print(arr2)

arr3 = np.array([[[4,5,6,7],[4,6,8,7]],[[4,5,6,7],[4,5,6,8]]])
print(arr3)

##type of array
print(type(arr1))
print(type(arr2))
print(type(arr3))

##diamention of array
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

##accessing array
print(arr1[2])
print(arr2[1][3])
print(arr3[1][0][2])

##print array one by one
print("arr1 element:")
for i in arr1:
    print(i)
print("arr2 element:")
for i in arr2:
    for j in i:
        print(j)
print("arr3 element:")
for i in arr3:
    for j in i:
        for z in j:
            print(z)

##print array one by one using numpy method
print("arr1 element:")
for i in np.nditer(arr1):
    print(i)
print("arr2 element:")
for i in np.nditer(arr2):
    print(i)
print("arr3 element:")
for i in np.nditer(arr3):
    print(i)

##sorting an array
print("sorted arr1:")
arr1.sort(axis=0)
print(arr1)

print("sorted arr2:")
arr2.sort()
print(arr2)

print("sorted arr2 with axis=0")
arr2.sort(axis=0)
print(arr2)

print("sorted arr2 with axis=1")
arr2.sort(axis=1)
print(arr2)

print("sorted arr3 with axis=1")
arr3.sort(axis=1)
print(arr3)

##sum of array
print("sum of arr1:",arr1.sum())
print("sum of arr2:",arr2.sum())
print("sum of arr3:",arr3.sum())

##array filtering
print("array masking:")
arr1 = arr1 > 5
print(arr1)

print("array filtering:")
arr1 = arr1[arr1>6]
print(arr1)




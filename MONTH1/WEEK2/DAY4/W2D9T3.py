import numpy as np

## indexing & slicing
##1) create an 8*8 numpy array with value from 1 to 64
arr=np.arange(1,65)
arr1=arr.reshape(8,8)
print(arr1)

##2)extraxt the third row and fifth column separately
third_row=arr1[2,:]
print("third column is:",third_row)

fifth_colm=arr1[:,4:5]
print(fifth_colm)

##3)extract the corner element(top-right,top-left,bottom-left,bottom-right)

##4)reverse the order of element along the rows
reverse_row=arr1[::-1]
print(reverse_row)



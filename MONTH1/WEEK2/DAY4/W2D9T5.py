import numpy as np

##boolean masking and filtering
##1)create an array of 20 random integers between 1 and 100

arr=np.random.randint(1,101,20)
print(arr)

##2)extract only the numbers that are greater than 50
number = np.extract(arr[arr>50],arr)
print(number)
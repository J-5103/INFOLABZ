
import numpy as np
from PIL import Image
import os

##-------------------------------Numpy Image----------------------

##1. Generate a script where the user can input the directory of an image, convert the
##image into grayscale, and save it into another folder.

user_enter_image=input("enter full path of an image:")

img=Image.open(user_enter_image).convert("L")

output_path=input("enter saved path:")

os.makedirs(output_path,exist_ok=True)

filename=os.path.basename(user_enter_image)
out_path=os.path.join(output_path,f"grayscale_{filename}")

img.save(out_path)

##-----------------------Conditional Filtering & Boolean Indexing--------------------------

#1. Replace all negative values in an array with 0.

arr=np.random.randint(-5,10,(4,4))
print(arr)

arr[arr<0]=0
print(arr)

#2. Count how many elements in an array are greater than a given number 25.

array=np.random.randint(1,100,(5,5))

count=np.sum(array>25)
print(f"array numbers are greater than 25 is:{count}")

#3. Extract all odd numbers from an array

arr1=np.where(array%2 !=0)
print("odd numbers in array:",array[arr1])




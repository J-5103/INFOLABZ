import numpy as np

##1.Create a 100x5 NumPy array representing 100 customers and their S most recent purchases.

arr=np.random.uniform(1,50000,(5,100))
print(arr)

##2.The purchase amoants should be random floats between ₹100 and ¥50,000

index = np.where(arr>=100&50000)
print(arr[index])

##3.Find and print the highest and lowest purchase amounts
maximum = np.max(arr)
print("maximum:",maximum)

lowest = np.min(arr)
print("lowest:",lowest)

##4 . Compute the average purchase amount per customer and store it in a new aray.
average = np.mean(arr)
print("average:",average)
result = np.append(arr,average)
print("average:",result)

##S. Dctarmine the customer who spent the most overall and print their index

index2 = np.where(arr==maximum)
print(index2)

##6.Find the total revenue generated from all purchases.
sum = np.sum(arr)
print("sum:",sum)

##7.Identify and print the number of purchases above ₹25,000 (high-value transactions).

index3 = np.where(arr>25000)
print("above 25000:",arr[index3])

##8 . Replace all purchases below ₹500 with ₹500 (to simulate a minimum spending policy.)

arr[arr<500] = 500
print("replace with 500:",arr)

##9. Sort each customer's purchase history in desceading order (most expensive purchase first.)
arr=np.sort(arr,axis=1)[:,::-1]
print(arr)

##10.Print the updated datasct.
print(arr)

##11.Find the top S castomers who spent the most in total.
customer_5top = arr[:5]
for i in customer_5top:
    print(f" top 5 customer:{i[0]}")

##12.Compute the percentage of high-value transactions (above ₹25,000).

index4 = np.where(arr>25000)
arr1 = arr[index4]
for i in arr1:
    print((i/500)*100,"%")

##13.Classify customers into three spending categories

index5 = np.where(arr>25000)
print("above 25000:", arr[index5])

index6 = np.where(arr<25000)
print("below 25000:",arr[index6])

index7 = np.where(arr==25000)
print("equal to 25000:",arr[index7])












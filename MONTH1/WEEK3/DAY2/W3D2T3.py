import numpy as np

customer_arr=np.array([[101, 250.50, 10, 1],
[102, 120.00, 5, 2],
[103, 310.75, 15, 3],
[104, 90.25, 0, 1],
[105, 500.00, 20, 4],
[106, 75.50, 0, 2],
[107, 150.00, 10, 3],
[108, 600.00, 25, 4],
[109, 220.00, 5, 1],
[110, 130.00, 8, 2]
])

#5.a. Find all transactions where the purchase amount is greater than $200.
filtered_arr=customer_arr[customer_arr[:,1]>200]
print(filtered_arr)

#5.b. Extract all transactions where a discount of more than 10% was applied.
filtered_trans=customer_arr[customer_arr[:,2]>10]
print(filtered_trans)

#6.a. Find the indices of transactions where the purchase amount is exactly $150
index=np.where(customer_arr[::1]==150)
print("index of transaction for purchase is excatly 150:",index[0])

#6.b. Identify the index of the highest purchase amount
max_purchase=np.max(customer_arr[::1])
index2=np.where(customer_arr==max_purchase)
print("index of highest purchase amount:",index2[0])

#7.a. Extract all transactions that belong to Category Code 3.
filtered_arr2=customer_arr[customer_arr[:,3]==3]
print(filtered_arr2)

#7.b. Find the total purchase amount for each category.

code3=customer_arr[customer_arr[:,3]==3]
code3_sum=np.sum(code3[:,1])
print("total purchase amount for code=3",code3_sum)

code2=customer_arr[customer_arr[:,3]==2]
code2_sum=np.sum(code2[:,1])
print("total purchase amount for code=2",code2_sum)

code1=customer_arr[customer_arr[:,3]==1]
code1_sum=np.sum(code1[:,1])
print("total purchase amount for code=1",code1_sum)

code4=customer_arr[customer_arr[:,3]==4]
code4_sum=np.sum(code4[:,1])
print("total purchase amount for code=4",code4_sum)

#8.a. Find the total amount spent by a specific customer (e.g., Customer ID 105)

id1=customer_arr[customer_arr[:,0]==101]
id1_sum=np.sum(id1[:,1])
print("total purchase amount for id=1",id1_sum)

#8.b. Identify customers who made multiple transactions (if applicable).

#9.a. Sort the transactions based on purchase amount in descending order.
sorted_arr=customer_arr[customer_arr[:,1].argsort()[::-1]]
print(sorted_arr)

#10.a. Identify transactions where the purchase amount is between $100 and $300.
filtered_arr3=customer_arr[(customer_arr[:,1]>=100) & (customer_arr[:,1]<=300)]
print(filtered_arr3)




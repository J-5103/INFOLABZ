import numpy as np
import pandas as pd

#1)Load the dataset into a NumPy array using np.genfromtxt().
data=np.genfromtxt("Sales_Data.csv", dtype=None, delimiter=",", names=True)
print(data)

product=data["Product"]
transactionid=data["TransactionID"]
quantity=data["Quantity"]
price=data["Price"]
date=data["Date"]

#1.1.1)Find the total number of transactions.
print(f"numbers of transactions:",len(data))

#1.1.2)Identify the unique products sold.
unique_product=np.unique(product)
print("unique product:",unique_product)

#1.1.3)Check for missing values and handle them (e.g., replace with 0 or remove rows).
data[np.where(np.isnan(price))]=0
data[np.where(np.isnan(transactionid))]=0

#2.1)Calculate the total revenue for each transaction (Revenue = Quantity * Price).
total_revenue=0
for i in range(0,len(transactionid)):
    total_revenue+=quantity[i]*price[i]
    print(f"total revenue of transactionid {transactionid[i]}, {product[i]}:{quantity[i]*price[i]}")

#2.2)Compute the total revenue for the entire dataset.
print("total revenue:",total_revenue)

#2.3)Find the average price of products sold.
avg_price=np.mean(price)
print("average price of product sold",avg_price)

#2.4)Calculate the total quantity sold for each product.

for i in unique_product:
    total_quantity=np.sum(quantity[product==i])
    print(f"product {i}`s total quantity:{total_quantity}")

#3.1)Find the product with the highest total revenue.
max_rev=np.argmax(quantity*price)
print("product with highest revenue:",product[max_rev])


#3.2)Compute the total revenue for each day (group by Date).
unique_date=np.unique(date)
print(unique_date)

total_revenue2=0
for i in range(0,len(unique_date)):
    total_revenue2+=quantity[i]*price[i]
    print(f"date {i}`s total revenue:{quantity[i]*price[i]}")

#3.3)Find the day with the highest total revenue.
max_rev=np.argmax(quantity*price)
print("day with highest revenue:",date[max_rev])


#4.1)Filter the dataset to find transactions where the quantity sold is greater than 10.
index=np.where(quantity>10)
print(data[index])

#4.2)Filter the dataset to find transactions for a specific product (e.g., "Laptop").
index=np.where(product=="Laptop")
print(data[index])






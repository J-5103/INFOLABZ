##---------------------------------Sales Data Analysis using NumPy--------------------------------------------
##--------------Objective:---------------
import numpy as np
import matplotlib.pyplot as plt

#Analyze and visualize sales data for a company’s products across four quarters using
#NumPy arrays. You will compute key metrics like total sales, average sales per product,
#and identify the best-performing product.

#1. Create a NumPy Array for Sales Data: Convert the sales data into a 2D NumPy array

data = [
    ["A", 12000, 15000, 17000, 20000],
    ["B", 18000, 22000, 24000, 28000],
    ["C", 10000, 12000, 14000, 16000],
    ["D", 9000, 11000, 13000, 15000]
]
sales_data = np.array([row[1:] for row in data], dtype=int)

print(sales_data)

#2. Compute Total Sales for Each Product: Calculate the total sales for each product
#by summing across the quarters.
total_sales_per_product = np.sum(sales_data, axis=1)
print(total_sales_per_product)

#3. Compute Average Quarterly Sales for Each Product: Find the average sales per
#quarter for each product

average_sales_per_product = np.mean(sales_data, axis=1)
print(average_sales_per_product)

#4. Find the Best-Performing Product: Identify the product with the highest total sales.
products = ["A", "B", "C", "D"]
total_sales_per_product = np.sum(sales_data, axis=1)
best_product_index = np.argmax(total_sales_per_product)

best_product = products[best_product_index]
best_sales = total_sales_per_product[best_product_index]

print(f"Best-Performing Product: {best_product} with Total Sales of {best_sales}")


#5. Visualize the Data (optional): If you'd like, use matplotlib to create a bar
#chart for the total sales and average quarterly sales of each product

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].bar(products, total_sales_per_product, color='royalblue')
axes[0].set_title("Total Sales per Product")
axes[0].set_xlabel("Products")
axes[0].set_ylabel("Total Sales")

axes[1].bar(products, average_sales_per_product, color='seagreen')
axes[1].set_title("Average Quarterly Sales per Product")
axes[1].set_xlabel("Products")
axes[1].set_ylabel("Average Sales")

plt.tight_layout()
plt.show()
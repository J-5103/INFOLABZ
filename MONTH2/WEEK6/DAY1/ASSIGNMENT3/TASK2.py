#----------------------------------------2: Retail Sales Data Analysis--------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt

#You are working as a data analyst in a retail company. The company wants insights into its sales data. Given the
# following dataset, answer the questions below:

sale_df=pd.read_csv("sales_data_large.csv")
df=pd.DataFrame(sale_df)
print(df.info())

#Task 1: Calculate the total sales for each product and rank the products based on sales performance.

total=df.groupby("Product")["Sales"].sum()

df["Rank"]=df["Sales"].rank(ascending=False).astype(int)
print(df.sort_values(by="Rank"))

#Task 2: Find the region with the highest total sales and the region with the lowest sales.

sale=df.groupby("Region")["Sales"].sum()
print("Region with highest sales:",sale.idxmax())
print("Region with lowest sales:",sale.idxmin())

#Task 3: Determine the product with the highest profit margin (profit as a percentage of sales)
# and compare it with the lowest profit margin product.

df["Profit margin(%)"]=(df["Profit"]/df["Sales"])*100
print(df.loc[df["Profit margin(%)"].idxmax()])
print(df.loc[df["Profit margin(%)"].idxmin()])

#Task 4: Identify the product that contributes the most to the total profit and the product with the lowest
# profit contribution.

print(df.loc[df["Profit"].idxmax()])
print(df.loc[df["Profit"].idxmin()])

#Task 5: Create a new column Revenue assuming the profit is 20% of the revenue and compare revenue per product.
df["Revenue"]=df["Profit"]/0.2
print(df.groupby("Product")["Revenue"].sum())

#Task 6: Sort the sales data by profit in descending order and display the top 3 most profitable sales transactions.
sorted=df.sort_values(by="Profit",ascending=False)
print(sorted.head(3))

#Task 7: Find the total sales and total profit for each region and visualize this using a pie chart.
region=df.groupby("Region")[["Sales","Profit"]].sum().reset_index()

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.pie(region["Sales"],labels=region["Region"],autopct="%.2f%%")
plt.title("Total Sales By Region")

plt.subplot(1,2,2)
plt.pie(region["Profit"],labels=region["Region"],autopct="%.2f%%")
plt.title("Total Profit By Region")

plt.show()

#Task 8: Identify regions where the total profit is below the average profit and suggest potential strategies
# to improve sales.

region_profit=df.groupby("Region")["Profit"].sum().reset_index()

avg_profit=region_profit["Profit"].mean()

low=region_profit[region_profit["Profit"] < avg_profit]

print("average profit across region:",avg_profit)
print("region with below average profit:")
print(low)
print("1. Increase Customer Reach")
print("2. Optimize Pricing Strategy")

#Task 9: Calculate the percentage contribution of each product to total sales and display the top 3 highest
# contributing products.

total_sale=df["Sales"].sum()

df["Sales_percentage"]=(df["Sales"]/total_sale)*100
df_sorted=df.sort_values(by="Sales_percentage",ascending=False)
print(df_sorted.head(3))

#Task 10: Create a grouped bar chart to compare total sales and total profit for each product using Matplotlib or Seaborn.

product=df.groupby("Product")[["Sales","Profit"]].sum().reset_index()

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.pie(product["Sales"],labels=product["Product"],autopct="%.2f%%")
plt.title("Total Sales By Product")

plt.subplot(1,2,2)
plt.pie(product["Profit"],labels=product["Product"],autopct="%.2f%%")
plt.title("Total Profit By Product")

plt.show()
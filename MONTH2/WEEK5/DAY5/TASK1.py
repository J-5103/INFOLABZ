import pandas as pd

data=pd.read_csv("ecommerce_sales_large.csv")

df=pd.DataFrame(data)
print(df)

#------------------------------1. Data Cleaning & Preprocessing--------------------
#Check for missing values and handle them appropriately.
print(df.isnull().sum())

#Detect and remove duplicate rows, if any.
print(df.duplicated().sum())

#Convert the Order_Date column into a datetime format for analysis.
df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce', dayfirst=True)
print(df["Order_Date"])

#-------------------------------2. Advanced Filtering & Querying-------------------------
#Find all orders where:
#The Total_Amount is above $1000 and the Delivery_Status is "Delivered".

print(df[(df["Total_Amount"] > 1000) & (df["Delivery_Status"]=="Delivered")])

#The customer used PayPal but the order was canceled.

print(df[(df["Payment_Method"]=="PayPal") & (df["Delivery_Status"]=="Canceled")])

#The Product_Category is "Electronics" and the order quantity is more than 2.

print(df[(df["Product_Category"]=="Electronics") & (df["Quantity"] > 2)])

#Identify the top 10 most expensive orders in the dataset.

sorted=df.sort_values(by="Total_Amount",ascending=False)
print(sorted.head(10))

#-----------------------------------3. Aggregation & Grouping-------------------------
#Find the total revenue generated from each Product_Category.

print(df.groupby("Product_Category")["Total_Amount"].sum())

#Identify the top 5 best-selling products by the number of orders.

print(df["Product_Name"].value_counts().head())

#Calculate the average order value (AOV) per payment method.

print(df.groupby("Payment_Method")["Total_Amount"].mean())

#Find the most frequently used payment method for each product category.
count=df.groupby(["Product_Category","Payment_Method"]).size().reset_index(name="count")
fre=count.loc[count.groupby("Product_Category")["count"].idxmax()]
print(fre)

#---------------------------------4. Date-Based Analysis---------------------------------
#Extract the year, month, and day from Order_Date and create new columns.
df['Order_Date']=pd.to_datetime(df["Order_Date"])
df['Year'] = df['Order_Date'].dt.year
df['Month'] = df['Order_Date'].dt.month
df['Day'] = df['Order_Date'].dt.day
print(df)

#Find out which month had the highest total sales.

month=df.groupby("Month")["Total_Amount"].sum()
print(month.idxmax())

#Identify the top 3 best-selling days of the week based on total revenue.
df["day_name"]=df["Order_Date"].dt.day_name()
print(df.groupby("day_name")["Total_Amount"].sum().nlargest(3))

#Count the number of orders placed in the last 3 months of the dataset.
last=df["Order_Date"].max()
monthago= last - pd.DateOffset(months=3)

print(df[df["Order_Date"] >= monthago].shape[0])

#---------------------------------------5. Customer Behavior Analysis---------------------------
#Find the top 10 customers who have spent the most money.
print(sorted.head(10))

#Calculate the average number of orders per customer.
total_order=df["Order_ID"].count()
unique_customer=df["Customer_ID"].nunique()
avg=total_order/unique_customer
print(avg)

#Identify customers who have placed more than 10 orders.
order_count=df["Customer_ID"].value_counts()
print(order_count[order_count > 10])

#Find how many unique customers used each payment method.
print(df.groupby("Payment_Method")["Customer_ID"].nunique())

#------------------------------------------6. Delivery Status Insights-------------------------
#Calculate the percentage of orders that were delivered, pending, or canceled.
statas=df["Delivery_Status"].value_counts()
print((statas/len(df))*100)

#Find the average order value for each Delivery_Status.
print(df.groupby('Delivery_Status')['Total_Amount'].mean())

#Identify which Product_Category has the highest cancellation rate.
total_orders = df.groupby('Product_Category').size()
canceled_orders = df[df['Delivery_Status'] == 'Canceled'].groupby('Product_Category').size()
cancellation_rate = (canceled_orders / total_orders * 100).fillna(0)
highest_cancellation_category = cancellation_rate.idxmax()
print(f"{highest_cancellation_category} has the highest cancellation rate.")
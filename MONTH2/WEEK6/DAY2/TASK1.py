import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#------------------------------------------------EDA ---------------------------------------------------------
#-------------------------------------1. Load and Inspect Data ---------------------------------------------
# Read the dataset into a Pandas DataFrame and check for
#missing values, data types, and basic statistics.

swiggy=pd.read_csv("swiggy.csv")
df=pd.DataFrame(swiggy)
print(df.isnull().sum())
print(df.dtypes)
print(df.describe())

#-----------------------------------------2. Summary Statistics --------------------------------------------------
#Generate summary statistics for Price, Avg ratings, and Total ratings.

print(df[["Price","Avg ratings","Total ratings"]].describe())

#---------------------------------------3. Handle Missing Values-------------------------------------------------
# Identify and fill or remove missing values if any.

#--------------------------------------------4. Convert Data Types -----------------------------------------------
# Ensure numerical columns (Price, Avg ratings, Total ratings) are in the correct format.
print(df[["Price","Avg ratings","Total ratings"]].dtypes)
df['Price'] = pd.to_numeric(df['Price']).astype('Int64')
print(df["Price"].dtypes)

#----------------------------------------------5. Standardize Column Names -----------------------------------------
# Convert column names to lowercase and replace spaces with underscores.
df.columns=df.columns.str.lower().str.replace(' ',"_")
print(df.columns)

#---------------------------------------------6. Top 5 Expensive Restaurants --------------------------------------
#Find the five most expensive restaurants based on Price.
sorted=df.sort_values(by="price",ascending=False)
print(sorted.head())

#-------------------------------------------7. Top Rated Restaurants-----------------------------------------------
#List restaurants with an Avg ratings of 4.5 and above.
print(df[df["avg_ratings"] >= 4.5])

#--------------------------------------------8. Average Price by Food Type ------------------------------------------
#Calculate the average price of different Food type categories.
print(df.groupby("food_type")["price"].mean())

#----------------------------------------------9. Most Popular Cities-----------------------------------------------
# Find which cities have the most restaurants.
city_count=df["city"].value_counts().reset_index()
print(city_count)

# #----------------------------------------------10. Fastest Delivery Restaurant----------------------------------------
#Identify the restaurant with the least Delivery time.
least=df.sort_values(by="delivery_time",ascending=True)
print(least.head(1))

# #----------------------------------------------Visualization ------------------------------------------------------
# #------------------------------------------------11. Price Distribution--------------------------------------------
# #Create a histogram or box plot of Price.
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.histplot(df['price'], bins=6, kde=True, color='blue')
plt.title('Price Distribution')
plt.xlabel('Price')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
#
# #-------------------------------------------12. Top Food Types ---------------------------------------------
# # Create a bar chart showing the number of restaurants per Food type.
foood_count=df["food_type"].value_counts().head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=foood_count.index,y=foood_count, palette="viridis")
plt.xlabel("Food type")
plt.ylabel("numbers of restaurant")
plt.title("numbers of restaurants as per food type")
plt.xticks(rotation=45)
plt.show()

# #-------------------------------------------13. City-wise Avg Ratings ------------------------------------------
# Plot a bar chart showing the average rating of restaurants in each city.
city_avg=df.groupby("city")["avg_ratings"].mean().reset_index()
print(city_avg)

plt.figure(figsize=(10,5))
sns.barplot(x=city_avg["city"],y=city_avg["avg_ratings"], palette="viridis")
plt.xlabel("city")
plt.ylabel("average ratings")
plt.title("average restaurants ratings by city")
plt.xticks(rotation=45)
plt.ylim(3.0,5.0)
plt.show()

#---------------------------------------------14. Top 10 Cities with the Most Restaurants ----------------------
# A bar chart showing the number of restaurants per city.
city=df.groupby("city")["restaurant"].count().reset_index()
print(city)

sns.barplot(x=city["city"],y=city["restaurant"],palette="viridis")
plt.xlabel("city")
plt.ylabel("numbers of restaurants")
plt.title("total restaurants per city")
plt.show()

#---------------------------------------------15. City-wise Average Price : -------------------------------------
#A grouped bar chart showing the average Price for restaurants in each city.
city_price_avg=df.groupby("city")["price"].mean().reset_index()

plt.bar(city_price_avg["city"],city_price_avg["price"])
sns.barplot(x=city_price_avg["city"],y=city_price_avg["price"],palette="viridis")
plt.xlabel("city")
plt.ylabel("average price")
plt.title("average price per city")
plt.show()

#---------------------------------------------16. Top 10 Most Expensive Restaurants -------------------------------
#A horizontal bar chart showing the top 10 most expensive restaurants.

expensive= df.sort_values(by="price",ascending=False).head(10)
df2=pd.DataFrame(expensive)
print(expensive)

sns.barplot(y=expensive["restaurant"],x=expensive["price"],palette="viridis",legend=False)
plt.xlabel("price")
plt.ylabel("restaurant")
plt.title("10 most expensive restaurant")
plt.show()



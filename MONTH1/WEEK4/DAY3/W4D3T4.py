import  matplotlib.pyplot as plt

#Crate a scatter plot graph for year wise car brand’s sales data.
#( it is used to identify which company had highest selling in particular year )

years = [2018, 2019, 2020, 2021, 2022]
toyota_sales = [1200, 1300, 1100, 1400, 1500]
honda_sales = [950, 1050, 1000, 1100, 1200]
ford_sales = [800, 900, 850, 950, 1000]

plt.scatter(toyota_sales,years,label="Toyota")
plt.scatter(honda_sales,years,label="Honda")
plt.scatter(ford_sales,years,label="Ford")
plt.legend()
plt.xlabel("Sales")
plt.ylabel("Years")
plt.title("Car`s sales Analysis By Year")
plt.show()
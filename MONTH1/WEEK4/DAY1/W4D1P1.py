import matplotlib.pyplot as plt

car_brands = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan"]
sales = [1200, 950, 800, 700, 600]


#CREATE A BAR GRAPH OF CAR_BRANDS VS SALES FROM ABOVE DATA.

plt.bar(car_brands,sales,color="green")
plt.xlabel("car brands")
plt.ylabel("sales")
plt.title("car sales analysis")
plt.show()
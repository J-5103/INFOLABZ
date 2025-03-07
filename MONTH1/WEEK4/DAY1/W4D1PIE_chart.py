import matplotlib.pyplot as plt

car_sales=["maruti","toyota","hyundai","tata"]
car_units=[100,500,480,621]
colors=["red","pink","blue","green"]

plt.pie(car_units,labels=car_sales,colors=colors,autopct="%.2f%%",explode=[0.1,0,0,0])

plt.show()
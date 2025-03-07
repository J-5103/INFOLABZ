import  matplotlib.pyplot as plt

#Create a horizontal bar graph as shown in below output from given data.

clothing_items = ['Trousers', 'Shirts', 'Jeans', 'T-Shirts']
sales = [120, 180, 150, 200]


plt.barh(clothing_items,sales)
plt.ylabel("Cloth Items")
plt.xlabel("Sales")
plt.title("Cloth Items Analysis")
plt.show()
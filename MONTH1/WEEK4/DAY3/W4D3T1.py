import matplotlib.pyplot as plt


#Create histogram of following data
price = [180,187,174,160,155,157,140,145,148,155]

plt.hist(price,bins=30,color="pink",alpha=0.7,edgecolor="black")
plt.xlabel("price")
plt.title("Histogram Example")
plt.show()


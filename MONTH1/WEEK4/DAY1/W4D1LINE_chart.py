import  matplotlib.pyplot as plt

time=['9:15','9:20','9:25','9:30','9:35','9:40','9:45','9:50','9:55','9:60']
price=[25,86,256,512,456,325,236,254,124,852]

plt.plot(time,price,color="red")
plt.xlabel("Time")
plt.ylabel("Price")
plt.title("Share Marcket Analysis")
plt.show()
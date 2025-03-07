import matplotlib.pyplot as plt

#Create a scatter plot of following data
matches = [1,2,3,4,5]
rohit = [25,15,45,70,65]

plt.scatter(matches,rohit,color="green",alpha=0.5,edgecolors="black")
plt.xlabel("Matches")
plt.ylabel("Rohit Score")
plt.title("Rohit Match Score Analysis")
plt.show()

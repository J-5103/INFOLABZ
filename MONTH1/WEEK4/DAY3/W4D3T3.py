import matplotlib.pyplot as plt

#Create a scatter plot for multiple parameters against values from following data
matches = [1,2,3,4,5]
rohit = [25,15,45,70,65]
kohli = [17,12,55,42,35]
dhavan =  [10,47,23,17,94]

plt.scatter(matches,rohit,label="Rohit")
plt.scatter(matches,kohli,label="Kohli")
plt.scatter(matches,dhavan,label="Dhavan")
plt.xlabel("Matches")
plt.ylabel("Scores")
plt.title("Players Scores Analysis")
plt.legend()
plt.show()

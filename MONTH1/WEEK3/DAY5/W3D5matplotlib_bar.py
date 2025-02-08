from matplotlib import pyplot as plt

players=["dhoni","rohit","virat"]
runs=[52,451,36]

plt.bar(players,runs)
plt.xlabel("player name")
plt.ylabel("score")
plt.title("cricket player analytics")
plt.show()
import matplotlib.pyplot as plt

matches=[1,2,3,4,5]
Rohit=[52,65,45,85,25]
Kohli=[52,89,56,120,74]
Dhoni=[52,63,48,98,130]

plt.plot(matches,Rohit,color="red",label="ROHIT")
plt.plot(matches,Kohli,color="green",label="KOHLI")
plt.plot(matches,Dhoni,color="blue",label="DHONI")
plt.xlabel("MATCHES")
plt.ylabel("RUNS")
plt.title("CRICKET DATA ANALYSIS")
plt.legend()
plt.show()
import matplotlib.pyplot as plt
import numpy as np

matches=[1,2,3,4,5]
Rohit=[52,65,45,85,25]
Kohli=[52,89,56,120,74]
Dhoni=[52,63,48,98,130]
bar_width=0.15

plt.bar(np.arange(len(matches)),Rohit,color="red",width=bar_width,label="ROHIT")
plt.bar(np.arange(len(matches))+0.15,Kohli,color="pink",width=bar_width,label="KOHLI")
plt.bar(np.arange(len(matches))+0.30,Dhoni,color="green",width=bar_width,label="DHONI")
plt.xlabel("MATCHES")
plt.ylabel("RUNS")
plt.title("CRICKET DATA ANALYSIS")
plt.show()
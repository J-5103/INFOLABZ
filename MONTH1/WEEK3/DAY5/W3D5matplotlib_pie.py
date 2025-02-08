from matplotlib import  pyplot as plt
import numpy as np

branches=["IT","CE","EC","CIVIL","ELE","MECH"]
seats=[41,52,12,23,56,89]

print(np.array(seats).sum())
plt.pie(seats,labels=branches,autopct="%.2f%%")
plt.show()

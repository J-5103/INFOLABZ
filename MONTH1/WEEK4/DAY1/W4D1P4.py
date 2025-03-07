import matplotlib.pyplot as plt
import xlrd
import numpy as np


sheet=xlrd.open_workbook("mydata (1).xlsx")
sheet=sheet.sheet_by_index(0)


#CREATE A MULTIPLE BAR GRAPH OF ALL PLAYERS IN MATCH VS SCORE PATTERN. ( MULTIPLE BAR GRAPH + XLRD )

matches=[]
Rohit=[]
Kohli=[]
Dhoni=[]

for i in range(1,sheet.nrows):
    matches.append(sheet.cell_value(i,0))
    for j in range(1,sheet.ncols):
        Rohit.append(sheet.cell_value(i,j))
        break
    for k in range(1, sheet.ncols):
        Kohli.append(sheet.cell_value(i,2))
        break
    for k in range(1, sheet.ncols):
        Dhoni.append(sheet.cell_value(i,3))
        break

print(Rohit)
print(Kohli)
print(Dhoni)
bar_width=0.15

plt.bar(np.arange(len(matches)),Rohit,width=bar_width,label="ROHIT")
plt.bar(np.arange(len(matches))+0.15,Kohli,width=bar_width,label="KOHLI")
plt.bar(np.arange(len(matches))+0.30,Dhoni,width=bar_width,label="DHONI")
plt.legend()
plt.xlabel("MATCHES")
plt.ylabel("RUNS")
plt.title("CRICKET DATA ANALYSIS")
plt.show()




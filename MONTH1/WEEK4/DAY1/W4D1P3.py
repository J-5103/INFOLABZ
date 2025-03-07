import matplotlib.pyplot as plt
import xlrd

#CREATE PIE CHART OF PLAYER WISE CONTRIBUTION IN ENTIRE SERIES FROM BELOW EXCEL DATA ( XLRD + PIE CHART )


sheet=xlrd.open_workbook("mydata (1).xlsx")
sheet=sheet.sheet_by_index(0)

players=[]
total_score=[]


for i in range(1,sheet.ncols):
    players.append(sheet.cell_value(0,i))
for i in range(1,sheet.ncols):
    total_score_each=0
    for j in range(1,sheet.nrows):
        total_score_each+=sheet.cell_value(j,i)
    total_score.append(total_score_each)

plt.pie(total_score,labels=players,autopct="%.2f%%",explode=[0.05,0.05,0.05])
plt.title("players Contribution Analysis")
plt.show()
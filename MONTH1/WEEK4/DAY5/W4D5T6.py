import matplotlib.pyplot as plt
import xlrd


#Print 2 graphs in a single row ( side by side ) Bar graph of match wise total of ( Virat+Rohit+Dhoni )
# and pie chart of total scores of Virat, Rohit and Dhoni.


sheet=xlrd.open_workbook("mydata (1).xlsx")
sheet=sheet.sheet_by_index(0)

players=[]
total_score=[]

for i in range(1,sheet.ncols):
    players.append(sheet.cell_value(0,i))
for i in range(1,sheet.ncols):
    total_score_rach=0
    for j in range(1,sheet.nrows):
        total_score_rach+=sheet.cell_value(j,i)
    total_score.append(total_score_rach)


fig,ex=plt.subplots(1,2)

ex[0].bar(players,total_score)
ex[0].set_xlabel("Players")
ex[0].set_ylabel("Score")
ex[0].set_title("Players Score Analysis")

ex[1].pie(total_score,labels=players,autopct="%.2f%%")
ex[1].set_title("player score percentage")
plt.show()
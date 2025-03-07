
import matplotlib.pyplot as plt
import xlrd


#excel link:https://docs.google.com/spreadsheets/d/1dWZm_w9sb88TNmykPuJd3yVxQxhRCzB2YRSCKfJo4iI/edit?usp=sharing

#Allow user to insert name of the player. Generate bar graph of match vs runs of that player.

sheet=xlrd.open_workbook("mydata (1).xlsx")
sheet=sheet.sheet_by_index(0)


print("players: ROHIT, KOHLI ,DHONI")
user_enter_player=input("Enter Player Name:")

for i in range(0,sheet.ncols):
    if user_enter_player==sheet.cell_value(0,i):
        for j in range(1,sheet.nrows):
            plt.bar(sheet.cell_value(j,0),sheet.cell_value(j,i))
            plt.xlabel("Matches")
            plt.ylabel("Scores")
            plt.title("Player score Analysis")
            plt.show()
            break
else:
    print("player not found")

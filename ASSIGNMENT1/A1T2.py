#--------------CRICKET DATA ANALYTICS------------------

import  xlrd


xlrd.xlsx.ensure_elementtree_imported(False,None)
xlrd.xlsx.Element_has_iter = True

loc = ("cricket.xlsx")
sheet = xlrd.open_workbook("cricket.xlsx")
sheet = sheet.sheet_by_index(0)

print(sheet)
print(sheet.cell_value(0,0))

#1)Print total number of rows.
print("Total numbers of rows:",sheet.nrows)

#2)Print total number of columns.
print("Total numbers of columns:",sheet.ncols)

#3)Print total number of matches
print("Total numbers of matches:",sheet.ncols-1)

#4)Print total number of players
print("Total numbers of players:",sheet.nrows-1)

#5)Print name of all players

for i in range(1,sheet.nrows):
    print(f"Name of {i} player:{sheet.cell_value(i,0)}")

#6)Print score of all matches of VIRAT
for i in range(1,sheet.ncols):
    print(f"VIRAT {i} matches scores are:{sheet.cell_value(2,i)}")

#7)Allow user to insert player name, print found or not found
user_enter_player=input("enter player name:")
for i in range(1,sheet.nrows):
    if user_enter_player==sheet.cell_value(i,0):
        print("player is found")
        break
else:
    print("player is not found")

#8)Allow user to insert player name, print latest score of that player
user_enter_player=input("enter player name:")
for i in range(1,sheet.nrows):
    if user_enter_player==sheet.cell_value(i,0):
        print(f"{user_enter_player}`s latest match score is:{sheet.cell_value(i, sheet.ncols - 1)}")
        break
else:
    print("player is not found")

#9)Allow user to insert name of player, print score of all matches of that player.
user_enter_player=input("enter player name:")
for i in range(1,sheet.nrows):
    if user_enter_player==sheet.cell_value(i,0):
        for j in range(1,sheet.ncols):
            print(sheet.cell_value(i,j))
        break
else:
    print("player is not found")

#10)Allow user to insert player name, store all matches data fo that player in a list.
user_enter_player=input("enter player name:")
score_list=[]
for i in range(1,sheet.nrows):
    if user_enter_player==sheet.cell_value(i,0):
        for j in range(1,sheet.ncols):
            score_list.append(sheet.cell_value(i,j))
        break
else:
    print("player is not found")
print(f"{user_enter_player}`s score list:{score_list}")

#11)Allow user to insert player name, print High score, Low Score, Average score of that player.
user_enter_player=input("enter player name:")
high_score=0
for i in range(1,sheet.nrows):
    if user_enter_player==sheet.cell_value(i,0):
        for j in range(1,sheet.ncols):
            if high_score < sheet.cell_value(i,j):
                high_score=sheet.cell_value(i,j)
        break
else:
    print("player is not found")

print(f"{user_enter_player}`s high score is:{high_score}")

for i in range(1,sheet.nrows):
    if user_enter_player == sheet.cell_value(i, 0):
        lowest_score=sheet.cell_value(i,1)
        for j in range(1,sheet.ncols):
            if lowest_score > sheet.cell_value(i,j):
                lowest_score = sheet.cell_value(i,j)
        break
else:
    print("player is not found")

print(f"{user_enter_player}`s lowest score is:{lowest_score}")

sum=0
for i in range(1,sheet.nrows):
    if user_enter_player == sheet.cell_value(i, 0):
        for j in range(1,sheet.ncols):
            sum+=sheet.cell_value(i,j)
        break
else:
    print("player is not found")

print(f"{user_enter_player}`s average score is:{sum/sheet.ncols-1}")








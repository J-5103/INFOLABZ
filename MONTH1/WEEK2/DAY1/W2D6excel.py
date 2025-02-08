import xlrd


xlrd.xlsx.ensure_elementtree_imported(False,None)
xlrd.xlsx.Element_has_iter = True

loc = ("example.xlsx")
sheet = xlrd.open_workbook("example.xlsx")
sheet = sheet.sheet_by_index(0)

print(sheet)
print(sheet.cell_value(0,0))
#
# ##peint number of colms and rows
# print("number of rows:",sheet.nrows)
# print("number of columns:", sheet.ncols)
#
# ##print numbers of all players
# for i in range(1,sheet.ncols):
#     print(sheet.cell_value(0,i))
#
# ##print score of rohit in all matches
# for i in range(1,sheet.nrows):
#     print(sheet.cell_value(i,1))
#
# ##allow user to enter name of player print player found or not
# user_enter_name = input("enter player name:")
# for i in range(1,sheet.ncols):
#     if user_enter_name==sheet.cell_value(0,i):
#         print("player found")
#         break
# else:
#     print("player not found")
#
# ## players last matvhes score
#
# user_enter_name = input("enter player name:")
# for i in range(1,sheet.ncols):
#     if user_enter_name==sheet.cell_value(0,i):
#         print("player found")
#         print(f"{user_enter_name}`s last match score is: {sheet.cell_value(sheet.nrows-1,i)}")
#         break
# else:
#     print("player not found")

# ##alloe user to enter name of the player and print all matches score
# user_enter_name = input("enter player name:")
# for i in range(1,sheet.ncols):
#     if user_enter_name==sheet.cell_value(0,i):
#         for j in range(1,sheet.nrows):
#             print(sheet.cell_value(j,i))
#         break
# else:
#     print("player not found")

# ##print all data in bellow formate
# for i in range(1,sheet.nrows):
#     print(f"MATCH {sheet.cell_value(i,0)}\n Score of: ROHIT is {sheet.cell_value(i,1)}\n Score of : KOHALI is {sheet.cell_value(i,2)}\n Score of : DHONI is {sheet.cell_value(i,3)} ")


##allow user to insert name pf player and print total and avarage of all the score of that player
# user_enter_name = input("enter player name:")
# sum=0
# for i in range(1,sheet.ncols):
#     if user_enter_name==sheet.cell_value(0,i):
#         for j in range(1,sheet.nrows):
#             sum+=sheet.cell_value(j,i)
#     break
# print(f"{user_enter_name}`s total score is:{sum}\n aevrage score is :{sum/sheet.nrows-1}")

##print highets score of user player
# user_enter_name=input("enter player name:")
# highest =0
#
# for i in range(1,sheet.ncols):
#     if user_enter_name==sheet.cell_value(0,i):
#         for j in range(1,sheet.nrows):
#             if highest <= sheet.cell_value(j,i):
#                 highest = sheet.cell_value(j,i)
#         break
#
# else:
#     print("player not found")
#
# print(f"{user_enter_name}`s highest value is : {highest}")

##allow user to insert player name and store all score data in temp data structure

# user_enter_name = input("enter player name:")
# playerscore = []
#
# for i in range(1,sheet.ncols):
#     if user_enter_name == sheet.cell_value(0,i):
#         for j in range(1,sheet.nrows):
#             playerscore.append(sheet.cell_value(j,i))
#         break
# else:
#     print("player not found")
#
# print(F"{user_enter_name}`s score is:",playerscore)

##allow user to insert player name,print lowest score of that player

# user_enter_name = input("enter player name:")
#
# for i in range(1,sheet.ncols):
#     if user_enter_name==sheet.cell_value(0,i):
#         lowestscore = sheet.cell_value(1,i)
#         for j in range(1,sheet.nrows):
#             if lowestscore > sheet.cell_value(j,i):
#                 lowestscore= sheet.cell_value(j,i)
#         break
# else:
#     print("player not found")
#
# print(f"{user_enter_name}`s lowestscore is:",lowestscore)

##allow user to insert player name ,store it in a variable
# players = []
#
# while True:
#     user_enter_name = input("enter player name:")
#     if user_enter_name!="stop":
#         players.append(user_enter_name)
#     else:
#         break
# print(players)

##print latest score of inserted two  players
playername = []

while True:
    user_enter_name = input("enter player name:")
    if user_enter_name!= "stop":
        for i in range(1,sheet.ncols):
            if user_enter_name==sheet.cell_value(0,i):
              playername.append(user_enter_name)
              break
        else:
            print("player not found")
    elif user_enter_name=="stop":
        for i in range(1,sheet.ncols):
            for j in range(0,len(playername)):
                if playername[j]==sheet.cell_value(0,i):
                        latestscore = sheet.cell_value(sheet.nrows-1,i)
                        print(f"{playername[j]}`s latest match score is:{latestscore}")
        break

print(playername)























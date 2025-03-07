import matplotlib.pyplot as plt
import xlrd
import numpy as np

sheet=xlrd.open_workbook("hotel_revies.xlsx")
sheet=sheet.sheet_by_index(0)

#1) Load hotel reviews dataset and Print first hotel’s name.
#
# print(sheet.cell_value(1,11))
#
# #2) Print total number of rows.
#
# print(sheet.nrows)
#
# #3) Print total number of Columns.
#
# print(sheet.ncols)
#
#
# #4) Allow user to insert hotel Name, Print hotel found or Not found
#
# user_enter_hotel_name=input("enter hotel name:")
#
# for i in range(1,sheet.nrows):
#     if user_enter_hotel_name==sheet.cell_value(i,11):
#         print("hotel found")
#         break
# else:
#     print("hotel not found")
#
# ##5) Allow user to insert hotel name, print hotel's details. For example Categories, city, state province ‘ address etc.
#
# user_enter_hotel_name=input("enter hotel name:")
#
#
# for i in range(1,sheet.nrows):
#     if user_enter_hotel_name==sheet.cell_value(i,11):
#         print(f"Categories:{sheet.cell_value(i,4)}")
#         print(f"Review Rating:{sheet.cell_value(i,17)}")
#         print(f"Country:{sheet.cell_value(i, 7)}")
#         print(f"State province:{sheet.cell_value(i, 13)}")
#         print(f"City:{sheet.cell_value(i,6)}")
#         print(f"Address:{sheet.cell_value(i,3)}")
#         break
# else:
#     print("hotel not found")
#
# ##6)Allow user to insert hotel name print total rating average of that hotel.
#
# user_enter_hotel_name=input("enter hotel name:")
# total_rating=[]
# is_found=False
#
# for i in range(1,sheet.nrows):
#     if user_enter_hotel_name==sheet.cell_value(i,11):
#         total_rating.append(sheet.cell_value(i,17))
#         is_found=True
#
# if is_found==False:
#     print("hotel not found")
# else:
#     print(f"{np.mean(total_rating)} is average rating.")

##7)Allow user to insert hotel name print pie chart and bar graph of that hotel's Star wise rating count.
#For Example 1 star - 12, 2 star - 8, 3 star - 23, 4 star - 35, 5 star - 120
#Bae graph and pie graph of above counts.

#
#
# user_enter_hotel_name=input("enter hotel name:")
# total_rating=[]
# is_found=False
# rating=[]
# star=["1⚡","2⚡","3⚡","4⚡","5⚡"]
#
# for i in range(1,sheet.nrows):
#     if user_enter_hotel_name==sheet.cell_value(i,11):
#         total_rating.append(sheet.cell_value(i,17))
#         is_found=True
#
# if is_found==False:
#     print("hotel not found")
# else:
#     for i in range(1,6):
#         rating.append(total_rating.count(i))
#     print(rating)
#
#     fig ,ax= plt.subplots(1, 2,figsize=(10,8),gridspec_kw={'wspace':0.5})
#     ax[0].bar(star,rating)
#     ax[0].set_xlabel("Star")
#     ax[0].set_ylabel("rating")
#     ax[0].set_title(f"Star wise rating of{user_enter_hotel_name}")
#
#     ax[1].pie(rating,labels=star,autopct="%.2f%%")
#     ax[1].set_title(f"Star wise rating of{user_enter_hotel_name}")
#     plt.show()


#8)Allow user to insert hotel names until User inserts stop. Print bar graph of Average rating of those entered hotel's.

rating=[]
is_stop=False
is_found=False
avg_rating=[]
hotels=[]

while True:
    if is_stop==False:
        user_enter_hotel_name=input("enter hotel name:")
        hotels.append(user_enter_hotel_name)
        for i in range(1,sheet.nrows):
            if user_enter_hotel_name==sheet.cell_value(i,11):
                rating.append(sheet.cell_value(i,17))
                is_found=True
        if is_found==False:
            print("hotel not found")
        else:
            avg=np.mean(rating)
            avg_rating.append(avg)
            plt.bar(hotels, avg_rating,color="blue")
            plt.title("hotel`s review rating")
            plt.xlabel("hotel")
            plt.ylabel("rating")
            is_stop=True

        if is_stop==True:
            user = input("do you want to stop this process?---yes/no:")
            if user == "yes":
                break
            if user == "no":
                is_stop = False

plt.show()

##9)Allow user to insert any 3 hotel names. Print pie chart of all 3 hotel's rating wise count
# ( same as question  7 ) in single frame. ( 3 pie chart of 3 hotels for comparison  ).

total_rating=[]
is_found=False
rating=[]
star=["1⚡","2⚡","3⚡","4⚡","5⚡"]
hotels=[]
first=[]
second=[]
third=[]


for _ in range(3):
    user_enter_hotel_name=input("enter hotel name:")
    hotels.append(user_enter_hotel_name)
    for i in range(1,sheet.nrows):
        if user_enter_hotel_name==sheet.cell_value(i,11):
            total_rating.append(sheet.cell_value(i, 17))
            is_found=True

    if is_found == False:
        print("hotel not found")

    else:
        for i in range(0,15):
            rating.append(total_rating.count(i))
            first.append(rating[0:5])
            second.append(rating[5:10])
            third.append(rating[10:15])

        fig,ax=plt.subplots(1,3,figsize=(10,8),gridspec_kw={'wspace':0.5})

        ax[0].pie(first,labels=star,autopct="%.2f%%")
        ax[0].set_title(f"{hotels[0]}")

        ax[1].pie(second,labels=star,autopct="%.2f%%")
        ax[1].set_title(f"{hotels[1]}")

        ax[2].pie(third,labels=star,autopct="%.2f%%")
        ax[2].set_title(f"{hotels[2]}")

        plt.show()










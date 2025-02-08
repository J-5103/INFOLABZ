#-----------------------SALES DATA ANALYSIS-------------------
#------------------------ELECTRONICS STORE DATA ANALYSIS ----------------------

import xlrd

from W3DAY1.W3D1 import lowest

xlrd.xlsx.ensure_elementtree_imported(False,None)
xlrd.xlsx.Element_has_iter = True

loc = ("storedata.xlsx")
sheet = xlrd.open_workbook("storedata.xlsx")
sheet = sheet.sheet_by_index(0)

print(sheet)
print(sheet.cell_value(0,0))

#1)PRINT TOTAL NUMBER OF ROWS
print(f"Total numbers of rows:{sheet.nrows}")

#2)PRINT TOTAL NUMBER OF COLUMNS
print(f"Total numbers of columns:{sheet.ncols}")

#3)PRINT 61
for i in range(1,sheet.nrows):
    for j in range(1,sheet.ncols):
        if sheet.cell_value(i,j)==61:
            print("print 61:","61")


#4)PRINT NAMES OF ALL MONTHS
for i in range(1,sheet.ncols):
    print(f"name of {i} month:{sheet.cell_value(0,i)}")

#5)PRINT NAMES OF ALL PRODUCTS
for i in range(1,sheet.nrows):
    print(f"name of {i} product:{sheet.cell_value(i,0)}")

#6)PRINT TOTAL NUMBER OF PRODUCTS SOLD IN MARCH MONTH
sum=0
for i in range(1,sheet.nrows):
    sum+=sheet.cell_value(i,3)
print(f"total products sold in march month is:{sum}")

#7)WHICH PRODUCT SOLD HIGHEST IN MARCH MONTH.  ( ANS MOBILES )

high_sold=0

for i in range(1,sheet.ncols):
    if sheet.cell_value(0,i)=="MARCH":
        for j in range(1,sheet.nrows):
            if high_sold<sheet.cell_value(j,i):
               high_sold=sheet.cell_value(j,i)

        for k in range(1,sheet.nrows):
            if sheet.cell_value(k,i) == high_sold :
                print("Highest sold product in march month:",sheet.cell_value(k,0))

#8)ALLOW USER TO INSERT NAME OF THE MONTH PRINT NAME OF HIGHEST AND LOWEST NUMBER OF PRODUCTS SOLD IN THAT MONTH
user_enter_month=input("enter month:").upper()
high_sold=0

for i in range(1,sheet.ncols):
    if user_enter_month==sheet.cell_value(0,i):
        lowest_sold=sheet.cell_value(1,i)
        for j in range(1, sheet.nrows):
            if high_sold < sheet.cell_value(j, i):
                high_sold = sheet.cell_value(j, i)
            if lowest > sheet.cell_value(j,i):
                lowest_sold=sheet.cell_value(j,i)

        for k in range(1,sheet.nrows):
            if sheet.cell_value(k,i)==high_sold:
                print(f"max sold product in {sheet.cell_value(0,i)} is :{sheet.cell_value(k,0)}")
            if sheet.cell_value(k,i)==lowest_sold:
                print(f"lowest sold product in {sheet.cell_value(0,i)} is :{sheet.cell_value(k,0)}")
        break
else:
    print("month is not defined")

#9)IN WHICH MONTH REFRIGERATOR SOLD HIGHEST.

max_sale_of_refrigerator=0

for i in range(1,sheet.nrows):
    if sheet.cell_value(i,0)=="REFRIGERATOR":
        for j in range(1,sheet.ncols):
            if max_sale_of_refrigerator<sheet.cell_value(i,j):
                max_sale_of_refrigerator=sheet.cell_value(i,j)

        for k in range(1,sheet.ncols):
            if sheet.cell_value(i,k)==max_sale_of_refrigerator:
                print("In this month refrigerator sold highest:",sheet.cell_value(0,k))


#10)ALLOW USER TO INSERT NAME OF ELECTRONIC DEVICE. PRINT IN WHICH MONTH IT SOLD HIGHEST.


for i in range(1,sheet.nrows):
    print(sheet.cell_value(i,0),end=" | ")
print()

user_electric_device=input("Enter Electric Device Name:").upper()
max_sale=0

for i in range(1,sheet.nrows):
    if sheet.cell_value(i,0)==user_electric_device:
        for j in range(1,sheet.ncols):
            if max_sale<sheet.cell_value(i,j):
                max_sale=sheet.cell_value(i,j)

        for k in range(1,sheet.ncols):
            if sheet.cell_value(i,k)==max_sale:
                print(f"Highest {sheet.cell_value(i,0)} Sold In",sheet.cell_value(0,k))
        break
else:
    print("Electric Device Not Found")













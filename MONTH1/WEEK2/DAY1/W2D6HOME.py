import xlrd

xlrd.xlsx.ensure_elementtree_imported(False,None)
xlrd.xlsx.Element_has_iter = True

loc = ("example2.xlsx")
sheet = xlrd.open_workbook("example2.xlsx")
sheet = sheet.sheet_by_index(0)

print(sheet)
print(sheet.cell_value(0,0))

##print number of colms and rows
print("number of rows:",sheet.nrows)
print("number of columns:",sheet.ncols)

##print numbers of all vegetables

for i in range(1,sheet.ncols):
    print(sheet.cell_value(0,i))

##print potato price in all years

for i in range(1,sheet.nrows):
    print(sheet.cell_value(i,5))

##allow user to enter name of vegetables and print this is found orr not
user_enter_name = input("enter vegetable name:")
for i in range(0,sheet.ncols):
    if user_enter_name==sheet.cell_value(0,i):
        print("vegetable is found")
        break
else:
    print("vegetable not found")

## vegetables current price
user_enter_name = input("enter vegetable name:")
for i in range(0,sheet.ncols):
    if user_enter_name==sheet.cell_value(0,i):
        print("vegetable is found")
        print(f"{user_enter_name}`s current price is {sheet.cell_value(sheet.nrows-1,i)}")
        break
else:
    print("vegetable not found")




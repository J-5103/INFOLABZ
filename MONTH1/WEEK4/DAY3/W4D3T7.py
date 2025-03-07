import matplotlib.pyplot as plt
import xlrd

#excel link:https://docs.google.com/spreadsheets/d/1xg2YId701Z4fa43gIcpgE9AHbQVHstvFYS9nJk7bKS8/edit?usp=sharing

#Allow user to insert product name. Print month wise pie chart along with percentage sales of that product.


sheet=xlrd.open_workbook("storedata (1).xlsx")
sheet=sheet.sheet_by_index(0)

print("LAPTOPS, MOBILES,TV,AC,OVEN,REFRIGERATOR,HEATERS")
user_enter_product=input("enter product name:")

label=[]
sale=[]

for i in range(0,sheet.nrows):
    if user_enter_product==sheet.cell_value(i,0):
        for j in range(1,sheet.ncols):
            label.append(sheet.cell_value(0, j))
            sale.append(sheet.cell_value(i,j))
        break
else:
    print("product not found")

plt.pie(sale, labels=label, autopct="%.2f%%")
plt.title("Product Sales Analysis")
plt.show()



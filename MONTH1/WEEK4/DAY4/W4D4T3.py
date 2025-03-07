import xlrd
import matplotlib.pyplot as plt

sheet=xlrd.open_workbook("RESULT1.xlsx")
sheet1=sheet.sheet_by_index(0)

sheet=xlrd.open_workbook("RESULT2.xlsx")
sheet2=sheet.sheet_by_index(0)

# Can we load two xlsx file in a single python program ? ----YES

# If yes print RAMESH and KATHAN

print(sheet1.cell_value(1,2))
print(sheet2.cell_value(3,2))

#Print horizontal bar graph of all 10 students. Y axes student name, X axes total.

student_name=[]
total=[]

for i in range(1,sheet1.nrows):
    student_name.append(sheet1.cell_value(i,2))
    total.append(sheet1.cell_value(i,3))
for i in range(1,sheet2.nrows):
    student_name.append(sheet2.cell_value(i,2))
    total.append(sheet2.cell_value(i,3))

plt.barh(student_name,total)
plt.xlabel("Total")
plt.ylabel("Student Name")
plt.title("Student Result Analysis")
plt.show()





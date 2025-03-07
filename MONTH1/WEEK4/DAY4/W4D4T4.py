
import matplotlib.pyplot as plt
import xlrd


sheet=xlrd.open_workbook("customer.xlsx")
sheet=sheet.sheet_by_index(0)

#Pie Chart 1 : Percentage of male and female from gender column.
person=["Female","Male"]
Female=[]
Male=[]
for i in range(1,sheet.nrows):
    if sheet.cell_value(i,1)=="Female":
        Female.append(sheet.cell_value(i,1))
    if sheet.cell_value(i,1)=="Male":
        Male.append(sheet.cell_value(i,1))
count1=[]
count1.append(len(Female))
count2=[]
count2.append(len(Male))

count=count1 + count2
print(count)

plt.pie(count,labels=person,autopct="%.2f%%")
plt.title("Female and Male Analysis")
plt.show()


#Pie Chart 2 : Percentage of Average, Poor and Good from review column.

review=["Average","Poor","Good"]
avg=[]
poor=[]
good=[]

for i in range(1,sheet.nrows):
    if sheet.cell_value(i,2)=="Average":
        avg.append(sheet.cell_value(i,2))
    if sheet.cell_value(i,2)=="Poor":
        poor.append(sheet.cell_value(i,2))
    if sheet.cell_value(i,2)=="Good":
        good.append(sheet.cell_value(i,2))

avgcount=[]
avgcount.append(len(avg))
poorcount=[]
poorcount.append(len(poor))
goodcount=[]
goodcount.append(len(good))

count= avgcount + poorcount + goodcount
print(count)

plt.pie(count,labels=review,autopct="%.2f%%")
plt.title("analysis of review")
plt.show()


#Pie Chart 3 : Percentage of School, UG and PG from education column.

education=["School","UG","PG"]
school=[]
ug=[]
pg=[]

for i in range(1,sheet.nrows):
    if sheet.cell_value(i,3)=="School":
        school.append(sheet.cell_value(i,3))
    if sheet.cell_value(i,3)=="UG":
        ug.append(sheet.cell_value(i,3))
    if sheet.cell_value(i,3)=="PG":
        pg.append(sheet.cell_value(i,3))

schoolcount=[]
schoolcount.append(len(school))
ugcount=[]
ugcount.append(len(ug))
pgcount=[]
pgcount.append(len(pg))

count= schoolcount + ugcount + pgcount
print(count)

plt.pie(count,labels=education,autopct="%.2f%%")
plt.title("analysis of Education")
plt.show()


#--------------------------------------1: Employee Data Analysis---------------------------------
import pandas as pd
import matplotlib.pyplot as plt


#Task 1: Read the employee dataset from a CSV file:

data = pd.read_csv('employee_data_large.csv')
df=pd.DataFrame(data )
print(df.info())

#Task 2: Add a new column Bonus where the bonus is 10% of the salary if the employee has more than 5
# years of experience, otherwise 5%.

df["bonus"]=df["Salary"]*df["Experience"].apply(lambda x:0.10 if x > 5 else 0.05)
print(df.info())

#Task 3: Find the average salary for each department and compare it with the overall company average salary.
dept_salary=df.groupby("Department")["Salary"].mean()
com_avg_salary=df["Salary"].mean()

comparison=dept_salary.to_frame().reset_index()
comparison["difference"]=comparison["Salary"]-com_avg_salary

print(f"department wise avg salary:{dept_salary}")
print(f"company overall average salary:{com_avg_salary}")
print(f"{comparison}")

# #Task 4: Identify the employee with the highest salary and the lowest salary in each department.
print(df.loc[df.groupby("Department")["Salary"].idxmax()])
print(df.loc[df.groupby("Department")["Salary"].idxmin()])

#Task 5: Create a new column Salary after Tax assuming a tax deduction of 12% from the Salary, and rank
# employees based on their post-tax salary.

df["salary_aft_tax"]=df["Salary"]*0.88
df["rank"]=df["salary_aft_tax"].rank(ascending=False)

print(df.sort_values(by="rank"))

#Task 6: Sort the employees by experience in descending order and filter the top 3 most experienced employees.

sorted=df.sort_values(by="Experience",ascending=False)
print(sorted.head(3))

#Task 7: Count the number of employees in each department and visualize this using a bar chart.
filter=df.groupby("Department")["Employee"].count()
df2=pd.DataFrame(filter,columns=["Employee"])
print(df2)

plt.bar(["Finance","HR","IT","Martketing","Operations"],df2["Employee"])
plt.xlabel("Departments")
plt.ylabel("Employees")
plt.title("Employees in each Department")
plt.show()

#Task 8: Find the department with the highest average experience and the lowest average experience.

avg=df.groupby("Department")["Experience"].mean()

print("Department with the highest average experience:",avg.idxmax())
print("Department with the lowest average experience:",avg.idxmin())

#Task 9: Identify employees earning above the department average salary and display only their names and salaries.

average=df.groupby("Department")["Salary"].mean()
above_avg=df[df.apply(lambda x:x["Salary"] > average[x["Department"]], axis=1)]
name=above_avg[["Employee","Salary"]]
print(name)

#Task 10: Create a pivot table summarizing the total salary, average experience, and total bonus per department.

pivot_table = df.pivot_table(
    index='Department',
    values=['Salary', 'Experience', 'bonus'],
    aggfunc={'Salary': 'sum', 'Experience': 'mean', 'bonus': 'sum'}
)

pivot_table.rename(columns={'Salary': 'Total Salary', 'Experience': 'Avg Experience', 'Bonus': 'Total Bonus'}, inplace=True)

print(pivot_table)



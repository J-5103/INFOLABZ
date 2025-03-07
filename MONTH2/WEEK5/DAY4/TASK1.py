import pandas as pd

df1=pd.read_csv("20_feb.csv")

#-------------Create a DataFrame--------------
#Create a Pandas DataFrame with columns: Name, Age, City, and Salary for 5 employees.

df=pd.DataFrame(df1,columns=["Name","Age","City","Salary"])
print(df.head())

##----------------------Basic Information & Summary------------------
#Display the first 3 rows of the DataFrame.

print(df.head(3))

#Show the column names, data types, and summary statistics.

print(df.info())

##----------------------------Indexing & Selecting Data------------------
#Retrieve all employees who live in New York.
name=df[df["City"]=="New York"]
print(name)

#Extract the Name and Salary columns only.
print(df.iloc[:,[0,-1]])

##-----------------------------Filtering Data-------------------------
#Find employees who earn more than $5000.
salary=df[df["Salary"]>5000]
print(salary)

#Find employees whose name starts with 'A'.
start=df[df["Name"].str.startswith("A",na=False)]
print(start)

##-------------------------------Handling Missing Data------------------------
#Introduce some NaN values in the Salary column and replace them with the column’s mean.
#
# print(df.isnull().sum())
# avg=df["Salary"].mean()
#
# df.fillna(avg,inplace=True)
# print(df)

#Drop any rows where Age is missing.
# df.dropna(inplace=True)
# print(df)

##--------------------------------Sorting Data------------------------------
#Sort the DataFrame by Salary in descending order.

print(df.sort_values(by="Salary", ascending=False))

##--------------------------GroupBy & Aggregations--------------------------
#Group employees by City and find the average salary in each city.

print(df.groupby("City")["Salary"].mean())

#-----------------------------Apply Functions------------------------
#Create a new column Salary_After_Tax, where each employee's salary is reduced by 10%.
df["Salary_After_Tax"] = df["Salary"] * 0.90
print(df)

##-----------------------------------Merging & Joining Data---------------------
#Create another DataFrame containing Department information and merge it with the existing employee DataFrame.

df_departments = pd.DataFrame(df1,columns=["Name","Department"])
print(df_departments)

df_merged = pd.merge(df, df_departments,on="Name", how="left")

print(df_merged)

##---------------------------------Filtering Data--------------------
#Find all employees who work in the "IT" department.
print(df_merged[df_merged["Department"]=="IT"])

#Retrieve employees earning more than $6000.
salary=df_merged[df_merged["Salary"]>6000]
print(salary)
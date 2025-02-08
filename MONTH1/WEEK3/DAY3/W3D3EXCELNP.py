import numpy as np

data=np.genfromtxt("numpy_analysis_data.csv", dtype=None, delimiter=",", names=True)
print(data)

#store data title into a variable
department=data["Department"]
salary=data["Salary"]
id=data["ID"]
experience = data["Experience"]
age=data["Age"]

#print unique departments
unique_departments= np.unique(department)
print(f"unique departments:{unique_departments}")

#print average salary
avg_salary=np.mean(salary)
print(f"average salary:{avg_salary}")

#print min and max salary
max_salary=np.max(salary)
print(f"maximum salary:{max_salary}")

min_salary=np.min(salary)
print(f"minimum salary:{min_salary}")

#print department and total salary of each department into dictionary
depart_dict={}
for i in unique_departments:
    total_salary=np.sum(salary[department==i])
    depart_dict[i]=total_salary
print(depart_dict)

for d,s in depart_dict.items():
    print(d,s)

#print salary between 50000 to 80000
salary_1=salary[(salary>50000) & (salary<80000)]
print(salary_1)

#print persentage of every department total salary with sum of all
total = np.sum(salary)
for d,s in depart_dict.items():
    print(f"department {d},percentange:{(s/total)*100}%")




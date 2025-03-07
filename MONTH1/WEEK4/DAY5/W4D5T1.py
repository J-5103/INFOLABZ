import matplotlib.pyplot as plt

#Generate pie chart from below dictionary data. Print college name in graph title.

Newdata = {"college":"Shree Raviraj",
           "seats":890,
           "branches":7,
           "data":[
               {"name":"CE","allocated":90},{"name":"IT","allocated":120},
               {"name":"MECH","allocated":40},{"name":"CSE","allocated":100},
               {"name":"CIVIL","allocated":70},{"name":"EC","allocated":15},
               {"name":"ELECTRONICS","allocated":45}]
}
branch=[]
seats=[]
collegename=Newdata["college"]
for i in range(0,len(Newdata["data"])):
    branch.append(Newdata["data"][i]["name"])
    seats.append(Newdata["data"][i]["allocated"])

print(branch)
print(seats)


plt.pie(seats,labels=branch,autopct="%.2f%%")
plt.title(collegename)
plt.show()



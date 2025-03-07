import matplotlib.pyplot as plt

#Generate 3 bar graphs in a single row for comparison of all players ( matches vs score ).
# chart from below dictionary data. Print college name in graph title.

Matchdata = {
  "Format": "ODI",
  "MATCHES": 5,
  "data": [
    {
      "Match": "Match 1",
      "ROHIT": 75,
      "KOHLI": 21,
      "DHAVAN": 40
    },
    {
      "Match": "Match 2",
      "ROHIT": 15,
      "KOHLI": 111,
      "DHAVAN": 10
    },
    {
      "Match": "Match 3",
      "ROHIT": 25,
      "KOHLI": 4,
      "DHAVAN": 70
    },
    {
      "Match": "Match 4",
      "ROHIT": 45,
      "KOHLI": 15,
      "DHAVAN": 80
    },
    {
      "Match": "Match 5",
      "ROHIT": 5,
      "KOHLI": 78,
      "DHAVAN": 20
    }
  ]
}
matches=[]
players=["ROHIT","KOHLI","DHAVAN"]
ROHIT=[]
KOHLI=[]
DHAVAN=[]

for i in range(0,len(Matchdata["data"])):
    matches.append(Matchdata["data"][i]["Match"])
    ROHIT.append(Matchdata["data"][i]["ROHIT"])
    KOHLI.append(Matchdata["data"][i]["KOHLI"])
    DHAVAN.append(Matchdata["data"][i]["DHAVAN"])

print(matches)
print(ROHIT)
print(KOHLI)
print(DHAVAN)

fig,ax=plt.subplots(1,3)

ax[0].bar(matches,ROHIT)
ax[0].set_xlabel("matches")
ax[0].set_title("Rohit Score")


ax[1].bar(matches,KOHLI)
ax[1].set_xlabel("matches")
ax[1].set_title("Kohli Score")


ax[2].bar(matches,DHAVAN)
ax[2].set_xlabel("matches")
ax[2].set_title("Dhavan Score")

plt.show()




from matplotlib import pyplot as plt

mydata={"guj_city":["ahemdabad","surat","rajkot"],
        "guj_cases":[50,78,63]}

city=list[mydata.keys()[0]]
case=list[mydata.keys()[1]]


plt.bar(city,case)
plt.show()
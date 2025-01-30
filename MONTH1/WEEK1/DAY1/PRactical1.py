mydata= {
"maharashtra":{"mumbai":{"city":"metro city","metro":"yes"}, "population":"20 cr"},
"gujarat": ["AHMEDABAD","SURAT","RAJKOT"],
"rajasthan":["AJMER","JAISALMER",{"capital":"jaipur"},["MEWAD","RJ","INR"]]
}

##print metro city
print("print metro city:",mydata["maharashtra"]["mumbai"]["city"])

##print jaipur
print("print jaipur:",mydata["rajasthan"][2]["capital"])

##print rajkot
print("print rajkot:",mydata["gujarat"][2])

##print Rj
print("print Rj:",mydata["rajasthan"][3][1])

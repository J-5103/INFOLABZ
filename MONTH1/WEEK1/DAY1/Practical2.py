mydata= {"category":[{"A":"FIRST","package":{"data":"2lacs"}},
{"B":"Second","data":{"new":[100]}},{"C":"Third","Tests":[45,75,25]}]};

##print 2lacs
print("print 2lacs:",mydata["category"][0]["package"]["data"])

##print 25
print("print 25:",mydata["category"][2]["Tests"][2])

##print 100
print("print 100:",mydata["category"][1]["data"]["new"][0])
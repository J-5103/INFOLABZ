# file = open("file.txt" , "w")
# file.write("this is a file")
# print(file)
# file.close()
#
# rfile = open("file.txt" , "r")
# print(rfile.read())
#
# afile= open("file.txt" ,"a")
# afile.write("\n this is a file methods of python")
# afile.close()
#
# rafile = open("first.txt" , "r")
# print(rafile.read())

import  os

if os.path.exists("file.txt"):
    os.remove("file.txt")
    print("file removed")
else:
    print("file dose not exist")
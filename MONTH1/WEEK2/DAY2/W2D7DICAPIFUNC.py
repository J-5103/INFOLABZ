##print word meaning what argument is passed

import requests

def dicapi(word):
    data = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + word)
    mydata = data.json()
    x = mydata[0]["meanings"][0]["definitions"][0]["definition"]
    return x
print(dicapi("banana"))



import requests

def api(url):
    data = requests.get(url)
    mydata=data.json()
    return mydata
print(api("https://isro.vercel.app/api/spacecrafts"))
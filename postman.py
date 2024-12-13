import requests
url = "https://www.omdbapi.com/?t=avatar&apikey=b50f00d8"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
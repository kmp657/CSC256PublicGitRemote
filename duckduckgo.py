import requests
url = "https://api.duckduckgo.com"
response = requests.get(url)
print(response.json())

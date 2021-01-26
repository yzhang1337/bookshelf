import requests

url = "http://localhost:5000/"

resp = requests.get(url)

print(resp.text)


resp = requests.post(url+"login",)
print(resp.text)

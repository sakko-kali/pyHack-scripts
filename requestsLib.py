import requests

url = "https://httpbin.org/post"
data = {"username": "admin", "password": "admin"}
response = requests.post(url, data=data)

print("Status code: ", response.status_code)
print("headers:", response.headers)
print("Body: ", response.text[:200])
print(response.json())
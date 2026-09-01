import requests

response = requests.get("https://api.github.com")

print(response)
print(type(response))
print(response.status_code)

api_data = response.json()
print(type(api_data))
print(api_data)

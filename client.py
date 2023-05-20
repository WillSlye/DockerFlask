import requests

response = requests.get('http://localhost:5001/microservice')
print(response.text)

import requests

base_Url = 'http://127.0.0.1:8000/product-list'

response =  requests.get(url=base_Url)
data     =  response.json()
print(data)
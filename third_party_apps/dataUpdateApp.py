import requests
import json

base_Url = 'http://127.0.0.1:8000/product-create/'

data ={
    'id':4
    'product_name' : 'napa',
    'product_amount':20
}

json_data = json.dumps(data)
response  = requests.put(url = base_Url, data = json_data)
data = response.json()
print(data)
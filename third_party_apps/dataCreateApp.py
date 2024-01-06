import requests
import json

base_Url = 'http://127.0.0.1:8000/product-create/'

data ={
    'product_name' : 'napa',
    'group_name':'talet',
    'product_price': 10,
    'product_amount':200
}

json_data = json.dumps(data)
response  = requests.post(url = base_Url, data = json_data)
data = response.json()
print(data)

import requests
import json
id = 411
url = f'http://localhost:5000/api/allowance/{id}'

data = {
    "amount":2222,
    "type_id":302

}
response = requests.put(url,json=data)
print(json.dumps(response.json()))
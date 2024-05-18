import requests
import json
url = 'http://localhost:5000/api/allowance'
data = {
    "amount":2137,
    "type_id":303
}
response = requests.post(url,json=data)
print(json.dumps(response.json()))
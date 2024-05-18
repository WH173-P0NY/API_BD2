import requests
import json
allowance_id = 401
url = f'http://localhost:5000/api/allowance/{allowance_id}'

response = requests.get(url)
print(json.dumps(response.json()))
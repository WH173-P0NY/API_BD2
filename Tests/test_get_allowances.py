import requests
import json
url = 'http://localhost:5000/api/allowance'

response = requests.get(url)
print(json.dumps(response.json()))
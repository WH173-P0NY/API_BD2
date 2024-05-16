import requests
import json
url = 'http://localhost:5000/api/overtime'

response = requests.get(url)
print(json.dumps(response.json()))
import requests
import json
allowanacetype_id = 3001
url = f'http://localhost:5000/api/allowancetype/{allowanacetype_id}'

response = requests.get(url)
print(json.dumps(response.json()))
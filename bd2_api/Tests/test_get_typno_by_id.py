import requests
import json
absencetype_id = 701
url = f'http://localhost:5000/api/absencetype/{absencetype_id}'

response = requests.get(url)
print(json.dumps(response.json()))
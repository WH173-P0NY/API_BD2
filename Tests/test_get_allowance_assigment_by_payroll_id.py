import requests
import json
payroll_id = 1002
url = f'http://localhost:5000/api/allowanceassignment/{payroll_id}'

response = requests.get(url)
print(json.dumps(response.json()))
import requests
import json
payroll_id = 30001
url = f'http://localhost:5000/api/payroll/{payroll_id}'

response = requests.get(url)
print(json.dumps(response.json()))
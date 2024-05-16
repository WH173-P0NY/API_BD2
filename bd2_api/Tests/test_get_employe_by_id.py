import requests
import json
employee_id = 1002
url = f'http://localhost:5000/api/employee/{employee_id}'

response = requests.get(url)
print(json.dumps(response.json()))
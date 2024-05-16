import requests
import json
id = 808
url = f'http://localhost:5000/api/absences/{id}'

data = {
    "start_date": "Sat, 08 Apr 2024 00:00:00 GMT",
    "end_date": "Wed, 10 Apr 2024 00:00:00 GMT",
    "employee_id": 107,
    "absence_type_id": 702

}
response = requests.put(url,json=data)
print(json.dumps(response.json()))
import requests
import json
url = 'http://localhost:5000/api/employee'
data = {
    "first_name": "Janina",
    "last_name": "Kowalska",
    "date_of_employment": "2023-04-01",
    "superior_id": None,
    "part_time": 1,
    "hourly_rate": 100.00,
    "department_id": 5001,
    "position_id": 6001
}
response = requests.post(url,json=data)
print(json.dumps(response.json()))
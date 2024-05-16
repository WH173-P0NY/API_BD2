import requests
import json
id = 113
url = f'http://localhost:5000/api/employee/{id}'

data = {
    "first_name": "Janusz",
    "last_name": "Kowalski",
    "date_of_employment": "2023-04-01",
    "superior_id": None,
    "activity": "A",
    "remaining_leave": 20,
    "salary": 5000.00,
    "hourly_rate": 100.00,
    "department_id": 501,
    "position_id": 601
}
response = requests.put(url,json=data)
print(json.dumps(response.json()))
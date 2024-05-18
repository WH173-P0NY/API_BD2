import requests
import json
url = 'http://localhost:5000/api/absences'
data = {
  "start_date": "2024-04-06",
  "end_date": "2024-04-10",
  "employee_id": 1002,
  "absence_type_id": 7003
}
response = requests.post(url, json=data)

# Sprawdź kod statusu odpowiedzi
print("Status code:", response.status_code)

# Wypisz surową treść odpowiedzi, jeśli status nie jest 200 OK
if response.status_code != 201:
    print("Response body:", response.text)

# Spróbuj przekształcić odpowiedź na JSON i ją wydrukować
try:
    print(json.dumps(response.json(), indent=4))
except json.JSONDecodeError:
    print("Odpowiedź nie jest w formacie JSON.")
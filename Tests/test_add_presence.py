import requests
import json
url = 'http://localhost:5000/api/presence'
data = {
  "date": "2024-04-06",
  "time_of_entry": "2024-04-06T08:00:00",
  "time_of_exit": "2024-04-06T16:00:00",
  "comment": "Normalny dzień pracy",
  "employee_id": 107
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
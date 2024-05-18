import requests
import json
url = 'http://localhost:5000/api/allowanceassignment'
data = {
  "allowance_id":4003,
  "payroll_id":10008
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
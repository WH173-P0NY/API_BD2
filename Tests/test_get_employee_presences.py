import requests
import json
employee_id = 107
url = f'http://localhost:5000/api/presence/{employee_id}'

response = requests.get(url)
if response.status_code == 200 and response.text:
    try:
        data = response.json()
        print(json.dumps(data))
    except json.decoder.JSONDecodeError:
        print("Odpowiedź nie zawiera danych w formacie JSON.")
else:
    print(f"Serwer zwrócił kod statusu: {response.status_code}")
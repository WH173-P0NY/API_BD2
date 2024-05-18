import requests
import json
id = 8006
url = f'http://localhost:5000/api/absences/{id}'
response = requests.delete(url)
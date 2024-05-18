import requests
import json
id = 411
url = f'http://localhost:5000/api/allowance/{id}'
response = requests.delete(url)
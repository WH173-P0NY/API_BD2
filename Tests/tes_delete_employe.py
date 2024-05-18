import requests
import json
id = 1035
url = f'http://localhost:5000/api/employee/delete/{id}'
response = requests.delete(url)
import requests
import json

def call_payroll_calculation(api_url, year_month, employees):
    data = {
        "year_month": year_month,
        "employees": employees
    }

    response = requests.post(api_url, json=data)

    if response.status_code == 200:
        print("Payroll calculated successfully!")
        print("Response:", response.json())
    else:
        print("Failed to calculate payroll.")
        print("Status Code:", response.status_code)
        print("Error Response:", response.text)

# URL endpointa
api_url = 'http://localhost:5000/api/calculate-monthly-payroll'

# Przykładowe dane wejściowe
year_month = '2024-03'
employees = [
    {"id": 1003, "allowance_ids": [4002, 4003]}
]

# Wywołanie funkcji
call_payroll_calculation(api_url, year_month, employees)
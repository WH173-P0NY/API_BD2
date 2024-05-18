import requests

url = 'http://localhost:5000/api/generate-report'

# Parametry, które chcesz przekazać
params = {
    'department_id': '502',  # Przykładowe ID działu
    'superior_id': '102',    # Przykładowe ID przełożonego
    'start_date': '2024-01-01',  # Data początkowa
    'end_date': '2024-02-01'     # Data końcowa
}

response = requests.get(url, params=params)

if response.status_code == 200:
    with open('downloaded_report.xlsx', 'wb') as f:
        f.write(response.content)
    print("Raport został pobrany i zapisany jako 'downloaded_report.xlsx'.")
else:
    print("Nie udało się pobrać raportu. Status code:", response.status_code)

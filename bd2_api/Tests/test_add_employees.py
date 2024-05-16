import requests

def add_presences_bulk():
    url = 'http://localhost:5000/api/presences/bulk' 
    data = {
        "presences": [
            {
                "date": "2024-05-06",
                "time_of_entry": "08:00:00",
                "time_of_exit": "16:00:00",
                "comment": "Delegacja",
                "employee_id": 1002
            },
            {
                "date": "2024-05-06",
                "time_of_entry": "09:00:00",
                "time_of_exit": "17:00:00",
                "comment": "Dzień jak co dzień",
                "employee_id": 1003
            }
        ]
    }
    response = requests.post(url, json=data)
    if response.status_code == 201:
        result = response.json()
        print("Bulk presences added successfully:", result)
    else:
        print("Failed to add presences:", response.status_code, response.text)

if __name__ == "__main__":
    add_presences_bulk()

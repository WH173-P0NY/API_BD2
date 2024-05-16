import requests

def get_managers():
    url = 'http://localhost:5000/api/managers'
    response = requests.get(url)
    if response.status_code == 200:
        managers = response.json()
        print("Managers:", managers)
    else:
        print("Failed to retrieve managers:", response.status_code)

if __name__ == "__main__":
    get_managers()

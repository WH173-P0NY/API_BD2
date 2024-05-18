from . import create_app
from .models import db, Employee

app = create_app()
app.app_context().push()  # Aktywuje kontekst aplikacji

try:
    employee = Employee.query.all()
    if employee:
        print(f"Połączenie z bazą danych działa! Pierwszy pracownik: {employee}")
    else:
        print("Połączenie z bazą danych działa, ale nie znaleziono pracowników.")
except Exception as e:
    print(f"Błąd połączenia z bazą danych: {e}")
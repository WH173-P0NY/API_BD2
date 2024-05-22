import json
import random
from datetime import datetime, timedelta

# Lista pracowników
employees = [
    {
        "activity": "1",
        "date_of_employment": "1999-03-23",
        "department": "HR",
        "first_name": "Haleigh",
        "hourly_rate": "100",
        "id": 1001,
        "last_name": "Spencer",
        "part_time": "1",
        "position": "Specjalista ds. Rekrutacji",
        "remaining_leave": 26,
        "superior": None,
    },
    {
        "activity": "1",
        "date_of_employment": "2002-07-15",
        "department": "IT",
        "first_name": "Kelvin",
        "hourly_rate": "95",
        "id": 1002,
        "last_name": "Simon",
        "part_time": "1",
        "position": "Administrator Systemow",
        "remaining_leave": 26,
        "superior": None,
    },
    {
        "activity": "1",
        "date_of_employment": "2000-01-08",
        "department": "R&D",
        "first_name": "Audrina",
        "hourly_rate": "90",
        "id": 1003,
        "last_name": "Patterson",
        "part_time": "1",
        "position": "Analityk ds. Rozwoju Tras",
        "remaining_leave": 26,
        "superior": None,
    },
    {
        "activity": "1",
        "date_of_employment": "2010-05-08",
        "department": "Inzynierii Hyperloop",
        "first_name": "Jacquelyn",
        "hourly_rate": "105",
        "id": 1004,
        "last_name": "Allen",
        "part_time": "1",
        "position": "Inzynier ds. Trakcji",
        "remaining_leave": 26,
        "superior": None,
    },
    {
        "activity": "1",
        "date_of_employment": "2008-11-12",
        "department": "Konstrukcji i Projektowania",
        "first_name": "Jefferson",
        "hourly_rate": "110",
        "id": 1005,
        "last_name": "Bernard",
        "part_time": "1",
        "position": "Projektant ds. Infrastruktury",
        "remaining_leave": 26,
        "superior": None,
    },
    {
        "activity": "1",
        "date_of_employment": "2012-12-11",
        "department": "Testow i Bezpieczenstwa",
        "first_name": "Gracie",
        "hourly_rate": "100",
        "id": 1006,
        "last_name": "Wilcox",
        "part_time": "1",
        "position": "Koordynator Testow",
        "remaining_leave": 26,
        "superior": None,
    },
    {
        "activity": "1",
        "date_of_employment": "2008-06-01",
        "department": "Technologii Trakcyjnej",
        "first_name": "Janelle",
        "hourly_rate": "95",
        "id": 1007,
        "last_name": "Bolton",
        "part_time": "1",
        "position": "Inzynier ds. Napedu",
        "remaining_leave": 26,
        "superior": None,
    },
    {
        "activity": "1",
        "date_of_employment": "2009-07-01",
        "department": "Logistyki i Zaopatrzenia",
        "first_name": "Jeremy",
        "hourly_rate": "90",
        "id": 1008,
        "last_name": "Schneider",
        "part_time": "1",
        "position": "Specjalista ds. Logistyki",
        "remaining_leave": 26,
        "superior": None,
    },
    {
        "activity": "1",
        "date_of_employment": "2007-10-10",
        "department": "Utrzymania Infrastruktury",
        "first_name": "Felipe",
        "hourly_rate": "105",
        "id": 1009,
        "last_name": "Rasmussen",
        "part_time": "1",
        "position": "Koordynator ds. Zarządzania",
        "remaining_leave": 26,
        "superior": None,
    },
    {
        "activity": "1",
        "date_of_employment": "2002-05-04",
        "department": "Finansow",
        "first_name": "Jovanni",
        "hourly_rate": "110",
        "id": 1010,
        "last_name": "Moss",
        "part_time": "1",
        "position": "Analityk Finansowy",
        "remaining_leave": 26,
        "superior": None,
    },
    {
        "activity": "1",
        "date_of_employment": "2014-04-22",
        "department": "HR",
        "first_name": "Brooklyn",
        "hourly_rate": "50",
        "id": 1011,
        "last_name": "Sosa",
        "part_time": "1",
        "position": "Doradca ds. Rozwoju",
        "remaining_leave": 26,
        "superior": "Haleigh Spencer",
    },
    {
        "activity": "1",
        "date_of_employment": "2022-06-16",
        "department": "HR",
        "first_name": "Campbell",
        "hourly_rate": "55",
        "id": 1012,
        "last_name": "Webster",
        "part_time": "0.5",
        "position": "Analityk ds. Wynagrodzen",
        "remaining_leave": 26,
        "superior": "Haleigh Spencer",
    },
    {
        "activity": "1",
        "date_of_employment": "2020-02-07",
        "department": "IT",
        "first_name": "Brian",
        "hourly_rate": "60",
        "id": 1013,
        "last_name": "Bentley",
        "part_time": "0.75",
        "position": "Inzynier Oprogramowania",
        "remaining_leave": 26,
        "superior": "Kelvin Simon",
    },
    {
        "activity": "1",
        "date_of_employment": "2020-04-09",
        "department": "IT",
        "first_name": "Nathan",
        "hourly_rate": "65",
        "id": 1014,
        "last_name": "Mcdonald",
        "part_time": "0.25",
        "position": "Specjalista Cybersecurity",
        "remaining_leave": 26,
        "superior": "Kelvin Simon",
    },
    {
        "activity": "1",
        "date_of_employment": "2018-10-01",
        "department": "R&D",
        "first_name": "Landon",
        "hourly_rate": "50",
        "id": 1015,
        "last_name": "Cortez",
        "part_time": "1",
        "position": "Koordynator Projektow",
        "remaining_leave": 26,
        "superior": "Audrina Patterson",
    },
    {
        "activity": "1",
        "date_of_employment": "2022-11-12",
        "department": "R&D",
        "first_name": "Sadie",
        "hourly_rate": "45",
        "id": 1016,
        "last_name": "Mendoza",
        "part_time": "0.5",
        "position": "Asystent Naukowy",
        "remaining_leave": 26,
        "superior": "Audrina Patterson",
    },
    {
        "activity": "1",
        "date_of_employment": "2018-06-01",
        "department": "Inzynierii Hyperloop",
        "first_name": "Zane",
        "hourly_rate": "40",
        "id": 1017,
        "last_name": "Barajas",
        "part_time": "0.75",
        "position": "Inzynier ds. Aerodynamiki",
        "remaining_leave": 26,
        "superior": "Jacquelyn Allen",
    },
    {
        "activity": "1",
        "date_of_employment": "2019-07-01",
        "department": "Inzynierii Hyperloop",
        "first_name": "Davin",
        "hourly_rate": "60",
        "id": 1018,
        "last_name": "Macias",
        "part_time": "1",
        "position": "Inzynier ds. Bezpieczenstwa",
        "remaining_leave": 26,
        "superior": "Jacquelyn Allen",
    },
    {
        "activity": "1",
        "date_of_employment": "2017-10-10",
        "department": "Konstrukcji i Projektowania",
        "first_name": "Lilah",
        "hourly_rate": "65",
        "id": 1019,
        "last_name": "Ferrell",
        "part_time": "0.25",
        "position": "Geodeta ds. Pomiarow",
        "remaining_leave": 26,
        "superior": "Jefferson Bernard",
    },
    {
        "activity": "1",
        "date_of_employment": "2022-04-03",
        "department": "Konstrukcji i Projektowania",
        "first_name": "Hamza",
        "hourly_rate": "50",
        "id": 1020,
        "last_name": "Casey",
        "part_time": "0.5",
        "position": "Specjalista ds. Materialow",
        "remaining_leave": 26,
        "superior": "Jefferson Bernard",
    },
    {
        "activity": "1",
        "date_of_employment": "2016-06-24",
        "department": "Testow i Bezpieczenstwa",
        "first_name": "Cailyn",
        "hourly_rate": "60",
        "id": 1021,
        "last_name": "Cuevas",
        "part_time": "1",
        "position": "Inspektor ds. Kontroli",
        "remaining_leave": 26,
        "superior": "Gracie Wilcox",
    },
    {
        "activity": "1",
        "date_of_employment": "2017-03-10",
        "department": "Testow i Bezpieczenstwa",
        "first_name": "Chaya",
        "hourly_rate": "55",
        "id": 1022,
        "last_name": "Small",
        "part_time": "0.5",
        "position": "Technik ds. Diagnostyki",
        "remaining_leave": 26,
        "superior": "Gracie Wilcox",
    },
    {
        "activity": "1",
        "date_of_employment": "2021-01-15",
        "department": "Technologii Trakcyjnej",
        "first_name": "Ronnie",
        "hourly_rate": "40",
        "id": 1023,
        "last_name": "Shannon",
        "part_time": "0.75",
        "position": "Specjalista ds. Zasilania",
        "remaining_leave": 26,
        "superior": "Janelle Bolton",
    },
    {
        "activity": "1",
        "date_of_employment": "2019-02-04",
        "department": "Technologii Trakcyjnej",
        "first_name": "Ahmed",
        "hourly_rate": "50",
        "id": 1024,
        "last_name": "Underwood",
        "part_time": "1",
        "position": "Technik ds. Maszyn",
        "remaining_leave": 26,
        "superior": "Janelle Bolton",
    },
    {
        "activity": "1",
        "date_of_employment": "2018-05-10",
        "department": "Logistyki i Zaopatrzenia",
        "first_name": "Kayley",
        "hourly_rate": "70",
        "id": 1025,
        "last_name": "Allison",
        "part_time": "0.5",
        "position": "Specjalista ds. Planowania",
        "remaining_leave": 26,
        "superior": "Jeremy Schneider",
    },
    {
        "activity": "1",
        "date_of_employment": "2020-10-02",
        "department": "Logistyki i Zaopatrzenia",
        "first_name": "Jaidyn",
        "hourly_rate": "45",
        "id": 1026,
        "last_name": "Kemp",
        "part_time": "0.75",
        "position": "Koordynator Zaopatrzenia",
        "remaining_leave": 26,
        "superior": "Jeremy Schneider",
    },
    {
        "activity": "1",
        "date_of_employment": "2015-02-01",
        "department": "Utrzymania Infrastruktury",
        "first_name": "Sullivan",
        "hourly_rate": "55",
        "id": 1027,
        "last_name": "Ortiz",
        "part_time": "1",
        "position": "Technik ds. Konserwacji",
        "remaining_leave": 26,
        "superior": "Felipe Rasmussen",
    },
    {
        "activity": "1",
        "date_of_employment": "2021-05-05",
        "department": "Utrzymania Infrastruktury",
        "first_name": "Ralph",
        "hourly_rate": "65",
        "id": 1028,
        "last_name": "Levine",
        "part_time": "0.5",
        "position": "Specjalista ds. Infrastruktury",
        "remaining_leave": 26,
        "superior": "Felipe Rasmussen",
    },
    {
        "activity": "1",
        "date_of_employment": "2019-11-11",
        "department": "Finansow",
        "first_name": "Jaelyn",
        "hourly_rate": "50",
        "id": 1029,
        "last_name": "Odonnell",
        "part_time": "0.75",
        "position": "Specjalista ds. Rachunkowosci",
        "remaining_leave": 26,
        "superior": "Jovanni Moss",
    },
    {
        "activity": "1",
        "date_of_employment": "2022-10-02",
        "department": "Finansow",
        "first_name": "Micaela",
        "hourly_rate": "40",
        "id": 1030,
        "last_name": "Brennan",
        "part_time": "1",
        "position": "Księgowy ds. Rozliczen",
        "remaining_leave": 26,
        "superior": "Jovanni Moss",
    },
]


# Funkcja do generowania listy dni roboczych w danym miesiącu
def generate_workdays(year, month):
    start_date = datetime(year, month, 1)
    end_date = (start_date + timedelta(days=32)).replace(day=1)
    current_date = start_date
    workdays = []

    while current_date < end_date:
        if current_date.weekday() < 5:  # Monday to Friday are workdays
            workdays.append(current_date.strftime("%Y-%m-%d"))
        current_date += timedelta(days=1)

    return workdays


def generate_presences(employees, year, month):
    presences = []
    workdays = generate_workdays(year, month)

    for employee in employees:
        for day in workdays:
            # Randomly generate entry and exit times
            start_hour = random.randint(0, 23)
            start_minute = random.choice([0, 15, 30, 45])
            entry_time_str = f"{start_hour:02}:{start_minute:02}:00"
            entry_time = datetime.strptime(
                f"{day} {entry_time_str}", "%Y-%m-%d %H:%M:%S"
            )

            # Work duration (8 hours +/- up to 2 hours)
            work_duration = timedelta(hours=8) + timedelta(
                minutes=random.randint(-120, 120)
            )
            exit_time = entry_time + work_duration
            exit_time_str = exit_time.strftime("%H:%M:%S")

            # Random absences
            if random.random() < 0.1:  # 10% chance of absence
                comment = "Nieobecny"
                continue
            else:
                comment = "Dzień jak co dzień"

            presence = {
                "time_of_entry": entry_time.strftime("%Y-%m-%d %H:%M:%S"),
                "time_of_exit": exit_time.strftime("%Y-%m-%d %H:%M:%S"),
                "comment": comment,
                "employee_id": employee["id"],
            }
            presences.append(presence)

    return {"presences": presences}


year = 2024
month = 5

presence_data = generate_presences(employees, year, month)
# Zapis do pliku JSON
with open("presence_data.json", "w", encoding="utf-8") as f:
    json.dump(presence_data, f, ensure_ascii=False, indent=4)

print("Dane obecności zostały zapisane do pliku presence_data.json")

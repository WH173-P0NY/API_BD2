from . import db


class Department(db.Model):
    __tablename__ = 'dzialy'

    id = db.Column('id_dzialu', db.Integer, primary_key=True)
    name = db.Column('nazwa_dzialu', db.String(30))
    description = db.Column('opis_dzialu', db.Text)

    # Relacja z pracownikami 
    employees = db.relationship('Employee', backref='department', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }

    def __repr__(self):
        return f'<Department {self.name}>'


class Position(db.Model):
    __tablename__ = 'stanowiska'

    id = db.Column('id_stanowiska', db.Integer, primary_key=True)
    name = db.Column('nazwa_stanowiska', db.String(30))
    description = db.Column('opis_stanowiska', db.Text)

    # Relacja z pracownikami 
    employees = db.relationship('Employee', backref='position', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }

    def __repr__(self):
        return f'<Position {self.name}>'


class Employee(db.Model):
    __tablename__ = 'pracownicy'

    id = db.Column('id_pracownika', db.Integer, primary_key=True)
    first_name = db.Column('imie', db.String(30))
    last_name = db.Column('nazwisko', db.String(30))
    date_of_employment = db.Column('data_zatrudnienia', db.Date)
    activity = db.Column('aktywnosc', db.String(1))
    superior_id = db.Column('id_przelozonego', db.Integer, db.ForeignKey('pracownicy.id_pracownika'), nullable=True)
    remaining_leave = db.Column('pozostaly_urlop', db.Integer)
    part_time = db.Column('etat', db.Numeric)
    hourly_rate = db.Column('podstawa_godzinowa', db.Numeric)
    department_id = db.Column('dzial_id_dzialu', db.Integer, db.ForeignKey('dzialy.id_dzialu'))
    position_id = db.Column('stanowisko_id_stanowiska', db.Integer, db.ForeignKey('stanowiska.id_stanowiska'))

    # Relacja do samodosiebie jako przelozony
    subordinates = db.relationship('Employee', backref=db.backref('superior', remote_side=[id]))

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_employment": self.date_of_employment.isoformat() if self.date_of_employment else None,
            "activity": self.activity,
            "superior_id": self.superior_id,
            "remaining_leave": self.remaining_leave,
            "part_time": str(self.part_time), 
            "hourly_rate": str(self.hourly_rate),
            "department_id": self.department_id,
            "position_id": self.position_id
        }
    def to_dict_full(self):
        superior_name = None
        if self.superior:
            superior_name = f"{self.superior.first_name} {self.superior.last_name}"
        
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_employment": self.date_of_employment.isoformat() if self.date_of_employment else None,
            "activity": self.activity,
            "superior": superior_name,
            "remaining_leave": self.remaining_leave,
            "part_time": str(self.part_time), 
            "hourly_rate": str(self.hourly_rate),
            "department": self.department.name,
            "position": self.position.name
        }
    def __repr__(self):
        return f'<Employee {self.first_name} {self.last_name}>'


class Presence(db.Model):
    __tablename__ = 'obecnosci'

    id = db.Column('id_obecnosci', db.Integer, primary_key=True)
    date = db.Column('data_obecnosci', db.Date)
    time_of_entry = db.Column('godzina_wejscia', db.Time)
    time_of_exit = db.Column('godzina_wyjscia', db.Time)
    comment = db.Column('komentarz', db.Text)
    employee_id = db.Column('pracownik_id_pracownika', db.Integer, db.ForeignKey('pracownicy.id_pracownika'))

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "time_of_entry": self.time_of_entry.isoformat(),
            "time_of_exit": self.time_of_exit.isoformat(),
            "comment": self.comment,
            "employee_id": self.employee_id
        }

    def __repr__(self):
        return f'<Presence {self.date} for Employee ID: {self.employee_id}>'


class Overtime(db.Model):
    __tablename__ = 'nadgodziny'

    id = db.Column('id_nadgodzin', db.Integer, primary_key=True)
    year_month = db.Column('rok_miesiac', db.Date)
    number_of_hours = db.Column('liczba_godzin', db.Numeric)
    hour_multiplier = db.Column('wspolczynnik_nadgodzin', db.Numeric)
    confirmation = db.Column('potwierdzenie_przelozonego', db.String(1))
    employee_id = db.Column('pracownik_id_pracownika', db.Integer, db.ForeignKey('pracownicy.id_pracownika'))
    employee = db.relationship('Employee', backref='overtimes')
    def to_dict(self):
        return {
            "id": self.id,
            "year_month": self.year_month.strftime('%Y-%m') if self.year_month else None,
            "number_of_hours": str(self.number_of_hours),
            "hour_multiplier": str(self.hour_multiplier),
            "confirmation": self.confirmation,
            "employee_id": self.employee_id,
            "employee_name": f"{self.employee.first_name} {self.employee.last_name}" if self.employee else None
        }

    def __repr__(self):
        return f'<Overtime {self.number_of_hours} hours in {self.year_month.strftime("%Y-%m")} for Employee ID: {self.employee_id}>'


class Absence(db.Model):
    __tablename__ = 'nieobecnosci'

    id = db.Column('id_nieobecnosci', db.Integer, primary_key=True)
    start_date = db.Column('poczatek_nieobecnosci', db.Date)
    end_date = db.Column('koniec_nieobecnosci', db.Date)
    employee_id = db.Column('pracownik_id_pracownika', db.Integer, db.ForeignKey('pracownicy.id_pracownika'))
    absence_type_id = db.Column('typ_nob_id_typu_nob', db.Integer, db.ForeignKey('typy_nob.id_typu_nob'))

    def to_dict(self):
        return {
            "id": self.id,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "employee_id": self.employee_id,
            "absence_type_id": self.absence_type_id
        }

    def __repr__(self):
        return f'<Absence {self.id} Type: {self.absence_type_id} Employee: {self.employee_id}>'


class AbsenceType(db.Model):
    __tablename__ = 'typy_nob'
    id = db.Column('id_typu_nob', db.Integer, primary_key=True)
    name = db.Column('nazwa_nieobecnosci', db.String(30))
    is_paid = db.Column('czy_platny', db.String(1))
    payment_percentage = db.Column('procent_platnosci', db.SmallInteger)
    is_in_allowance = db.Column('czy_w_puli_urlopow', db.String(1))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "is_paid": self.is_paid,
            "payment_percentage": self.payment_percentage,
            "is_in_allowance": self.is_in_allowance
        }

    def __repr__(self):
        return f'<AbsenceType {self.name}>'


class Payroll(db.Model):
    __tablename__ = 'wynagrodzenia'

    id = db.Column('id_wynagrodzenia', db.Integer, primary_key=True)
    year_month = db.Column('rok_miesiac', db.Date)
    base = db.Column('podstawa', db.Numeric)
    overtime = db.Column('nadgodziny', db.Numeric)
    additional = db.Column('dodatki', db.Numeric)
    deductions = db.Column('potracenia', db.Numeric)
    sum = db.Column('suma', db.Numeric)
    employee_id = db.Column('pracownik_id_pracownika', db.Integer, db.ForeignKey('pracownicy.id_pracownika'))

    def to_dict(self):
        return {
            "id": self.id,
            "year_month": self.year_month,
            "base": self.base,
            "overtime": self.overtime,
            "additional": self.additional,
            "deductions": self.deductions,
            "sum": self.sum,
            "employee_id": self.employee_id

        }

    def __repr__(self):
        return f'<Payroll for Employee ID: {self.employee_id} Year-Month: {self.year_month}>'


class Allowance(db.Model):
    __tablename__ = 'dodatki'

    id = db.Column('id_dodatku', db.Integer, primary_key=True)
    amount = db.Column('kwota_dodatku', db.Numeric)
    type_id = db.Column('typ_dodatku_id_typu_dodatku', db.Integer, db.ForeignKey('typy_dodatkow.id_typu_dodatku'))

    def to_dict(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "type_id": self.type_id

        }

    def __repr__(self):
        return f'<Allowance ID: {self.id} Amount: {self.amount}>'


class AllowanceType(db.Model):
    __tablename__ = 'typy_dodatkow'

    id = db.Column('id_typu_dodatku', db.Integer, primary_key=True)
    name = db.Column('nazwa_dodatku', db.String(30))
    description = db.Column('opis_dodatku', db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description

        }

    def __repr__(self):
        return f'<AllowanceType {self.name}>'


class AllowanceAssignment(db.Model):
    __tablename__ = 'przydzialy_dodatkow'

    payroll_id = db.Column('wynagrodzenie_id_wynagrodzenia', db.Integer,
                           db.ForeignKey('wynagrodzenia.id_wynagrodzenia'), primary_key=True)
    allowance_id = db.Column('dodatki_id_dodatku', db.Integer, db.ForeignKey('dodatki.id_dodatku'), primary_key=True)

    def to_dict(self):
        return {
            "payroll_id": self.payroll_id,
            "allowance_id": self.allowance_id

        }

    def __repr__(self):
        return f'<AllowanceAssignment Payroll ID: {self.payroll_id} Allowance ID: {self.allowance_id}>'

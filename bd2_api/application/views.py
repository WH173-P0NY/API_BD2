from flask import Blueprint, request, jsonify, make_response, send_file
from . import db
from .models import Employee, Department, Position, Presence, Absence, Overtime, Payroll, Allowance, AbsenceType, \
    AllowanceType, AllowanceAssignment
from datetime import datetime
from sqlalchemy import func, extract, cast, Date, Numeric,Float
from decimal import Decimal
import pandas as pd
import os

api = Blueprint('api', __name__)


@api.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.join(Employee.department).join(Employee.position).filter(Employee.activity == '1').all()
    return jsonify([employee.to_dict_full() for employee in employees]), 200


@api.route('/employee/<int:id>', methods=['GET'])
def get_employee(id):
    employee = Employee.query.get_or_404(id)
    return jsonify(employee.to_dict()), 200


@api.route('/employee', methods=['POST'])
def add_employee():
    data = request.get_json()
    new_employee = Employee(
    first_name = data['first_name'],
    last_name = data['last_name'],
    date_of_employment=datetime.strptime(data['date_of_employment'], '%Y-%m-%d').isoformat(),
    superior_id = data.get('superior_id'),
    activity = 1,
    remaining_leave = 26,
    part_time=data['part_time'],
    hourly_rate = data['hourly_rate'],
    department_id = data['department_id'],
    position_id = data['position_id']
    
    )
    db.session.add(new_employee)
    db.session.commit()
    return make_response(jsonify(new_employee.to_dict()), 201)


@api.route('/employee/<int:id>', methods=['PUT'])
def update_employee(id):
    employee = Employee.query.get_or_404(id)
    data = request.get_json()
    employee.first_name = data['first_name']
    employee.last_name = data['last_name']
    employee.date_of_employment = datetime.strptime(data['date_of_employment'], '%Y-%m-%d').isoformat(),
    employee.superior_id = data ['superior_id'],
    employee.part_time=data['part_time'],
    employee.hourly_rate = data['hourly_rate'],
    employee.department_id = data['department_id'],
    employee.position_id = data['position_id']

    db.session.commit()
    return jsonify(employee.to_dict()), 200

@api.route('/employee/delete/<int:id>', methods=['PUT'])
def delete_employee(id):
    employee = Employee.query.get_or_404(id)
    if employee:
        employee.activity = '0'
        db.session.commit()
        return make_response(jsonify({"message": "Employee deactivated"}), 200)
    else:
        return jsonify({"error": "Employee not found"}), 404

@api.route('/employee/activate/<int:id>', methods=['PUT'])
def activate_employee(id):
    employee = Employee.query.get_or_404(id)
    if employee:
        employee.activity = '1'
        db.session.commit()
        return make_response(jsonify({"message": "Employee activated"}), 200)
    else:
        return jsonify({"error": "Employee not found"}), 404


@api.route('/department', methods=['GET'])
def get_departments():
    departments = Department.query.all()
    return jsonify([department.to_dict() for department in departments]), 200


@api.route('/position', methods=['GET'])
def get_position():
    positions = Position.query.all()
    return jsonify([position.to_dict() for position in positions]), 200


@api.route('/presences', methods=['GET'])
def get_presences():
    presences = db.session.query(Presence, Employee.first_name, Employee.last_name).join(Employee, Presence.employee_id == Employee.id).all()
    return jsonify([{
        "presence_id": presence[0].id,
        "date": presence[0].date,
        "time_of_entry": presence[0].time_of_entry.isoformat(),
        "time_of_exit": presence[0].time_of_exit.isoformat(),
        "comment": presence[0].comment,
        "employee_id": presence[0].employee_id,
        "first_name": presence[1],
        "last_name": presence[2]
    } for presence in presences]), 200


@api.route('/presence/<int:employee_id>', methods=['GET'])
def get_employee_presences(employee_id):
    presences = Presence.query.filter_by(employee_id=employee_id).all()
    return jsonify([presence.to_dict() for presence in presences]), 200


@api.route('/presence', methods=['POST'])
def add_presence():
    """
    {
        "id": self.id,
        "date": self.date,
        "time_of_entry": self.time_of_entry.isoformat(),
        "time_of_exit": self.time_of_exit.isoformat(),
        "comment": self.comment,
        "employee_id": self.employee_id
    }
    """
    data = request.get_json()
    new_presence = Presence(
        date=datetime.strptime(data['date'], '%Y-%m-%d').isoformat(),
        time_of_entry=datetime.strptime(data['time_of_entry'], '%Y-%m-%dT%H:%M:%S').time(),
        time_of_exit=datetime.strptime(data['time_of_exit'], '%Y-%m-%dT%H:%M:%S').time(),
        comment=data['comment'],
        employee_id=data['employee_id']
    )
    db.session.add(new_presence)
    db.session.commit()
    return make_response(jsonify(new_presence.to_dict()), 201)


@api.route('/absences/<int:employee_id>', methods=['GET'])
def get_employee_absences(employee_id):
    absences = Absence.query.filter_by(employee_id=employee_id).all()
    return jsonify([absence.to_dict() for absence in absences]), 200


@api.route('/overtime/<int:employee_id>', methods=['GET'])
def get_employee_overtime(employee_id):
    overtime_list = Overtime.query.filter_by(employee_id=employee_id).all()
    return jsonify([overtime.to_dict() for overtime in overtime_list]), 200


@api.route('/payroll/<int:employee_id>', methods=['GET'])
def get_payroll(employee_id):
    payroll_list = Payroll.query.filter_by(employee_id=employee_id).all()
    return jsonify([payroll.to_dict() for payroll in payroll_list]), 200


@api.route('/allowance/<int:id>', methods=['GET'])
def get_allowance(id):
    allowance = Allowance.query.get_or_404(id)
    return jsonify(allowance.to_dict()), 200


@api.route('/absencetype/<int:id>', methods=['GET'])
def get_absencetype(id):
    absencetype = AbsenceType.query.get_or_404(id)
    return jsonify(absencetype.to_dict()), 200


@api.route('/allowancetype/<int:id>', methods=['GET'])
def get_allowancetype(id):
    allowancetype = AllowanceType.query.get_or_404(id)
    return jsonify(allowancetype.to_dict()), 200


@api.route('/allowanceassignment/<int:payroll_id>', methods=['GET'])
def get_allowanceassignment(payroll_id):
    allowanceassignment = AllowanceAssignment.query.filter_by(payroll_id=payroll_id).all()
    return jsonify([allowance.to_dict() for allowance in allowanceassignment]), 200

@api.route('/absences', methods=['POST'])
def add_absence():
    data = request.get_json()
    start_date = datetime.strptime(data['start_date'], '%Y-%m-%d')
    end_date = datetime.strptime(data['end_date'], '%Y-%m-%d')
    employee_id = data['employee_id']
    absence_type_id = data['absence_type_id']
    num_days = (end_date - start_date).days + 1

    employee = Employee.query.get(employee_id)
    if employee:
        # Pobierz typ nieobecności
        absence_type = AbsenceType.query.get(absence_type_id)
        if absence_type and absence_type.is_paid == '1':  # Zakładamy, że tylko płatne nieobecności zmniejszają urlop
            employee.remaining_leave -= num_days

        new_absence = Absence(
            start_date=start_date.isoformat(),
            end_date=end_date.isoformat(),
            employee_id=employee_id,
            absence_type_id=absence_type_id
        )
        db.session.add(new_absence)
        db.session.commit()
        return make_response(jsonify(new_absence.to_dict()), 201)
    else:
        return jsonify({"error": "Employee not found"}), 404


@api.route('/absences/<int:id>', methods=['PUT'])
def update_absence(id):
    absence = Absence.query.get_or_404(id)
    data = request.get_json()
    absence.start_date = data['start_date']
    absence.end_date = data['end_date']
    absence.employee_id = data['employee_id'],
    absence.absence_type_id = data['absence_type_id']

    db.session.commit()
    return jsonify(absence.to_dict()), 200


@api.route('/absences/<int:id>', methods=['DELETE'])
def delete_absence(id):
    absence = Absence.query.get_or_404(id)
    employee = Employee.query.get(absence.employee_id)
    if not employee:
        return jsonify({"error": "Employee not found"}), 404
    num_days = (absence.end_date - absence.start_date).days + 1

    # Sprawdź, czy nieobecność była płatna
    absence_type = AbsenceType.query.get(absence.absence_type_id)
    if absence_type and absence_type.is_paid == '1': 
        employee.remaining_leave += num_days

    # Usuń nieobecność
    db.session.delete(absence)
    db.session.commit()
    return make_response(jsonify({"message": "Absence deleted"}), 204)


@api.route('/allowance', methods=['POST'])
def add_allowance():
    """
    {
        "id": self.id,
        "amount": self.amount,
        "type_id": self.type_id
    }
    """
    data = request.get_json()
    new_allowance = Allowance(
        amount=data['amount'],
        type_id=data['type_id']
    )
    db.session.add(new_allowance)
    db.session.commit()
    return make_response(jsonify(new_allowance.to_dict()), 201)


@api.route('/allowance/<int:id>', methods=['PUT'])
def update_allowance(id):
    allowance = Allowance.query.get_or_404(id)
    data = request.get_json()
    allowance.amount = data['amount'],
    allowance.type_id = data['type_id']

    db.session.commit()
    return jsonify(allowance.to_dict()), 200

@api.route('/allowance', methods=['GET'])
def get_all_employee_allowances():
    employees = Employee.query.all()
    all_allowances = []

    for employee in employees:
        employee_info = {
            "first_name": employee.first_name,
            "last_name": employee.last_name
        }
        allowances = db.session.query(
            Allowance.amount,
            AllowanceType.name.label('allowance_type'),
            AllowanceType.description.label('allowance_description'),
            Payroll.year_month.label('allowance_date')
        ).select_from(Payroll).join(
            AllowanceAssignment, Payroll.id == AllowanceAssignment.payroll_id
        ).join(
            Allowance, AllowanceAssignment.allowance_id == Allowance.id
        ).join(
            AllowanceType, Allowance.type_id == AllowanceType.id
        ).filter(
            Payroll.employee_id == employee.id
        ).all()

        for allowance in allowances:
            allowance_dict = {
                "first_name": employee_info["first_name"],
                "last_name": employee_info["last_name"],
                "amount": float(allowance.amount),  # Convert Decimal to float
                "allowance_type": allowance.allowance_type,
                "allowance_date": allowance.allowance_date.strftime('%Y-%m-%d'),
                "allowance_description": allowance.allowance_description
            }
            all_allowances.append(allowance_dict)

    return jsonify(all_allowances), 200

@api.route('/allowance/<int:id>', methods=['DELETE'])
def delete_allowance(id):
    allowance = Allowance.query.get_or_404(id)
    db.session.delete(allowance)
    db.session.commit()
    return make_response(jsonify({"message": "Allowance deleted"}), 204)


@api.route('/payroll', methods=['GET'])
def get_payroles():
    payroles = Payroll.query.all()
    return jsonify([payroll.to_dict() for payroll in payroles]), 200

@api.route('/absence_type', methods=['GET'])
def get_absence_types():
    absence_types = AbsenceType.query.all()
    return jsonify([absence_type.to_dict() for absence_type in absence_types]), 200

@api.route('/generate-report', methods=['GET'])
def generate_report():
    department_id = request.args.get('department_id')
    superior_id = request.args.get('superior_id')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    employment_date_from = request.args.get('employment_date_from', None)
    employment_date_to = request.args.get('employment_date_to', None)

    # Przekształcenie dat z formatu string na datetime
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    if employment_date_from:
        employment_date_from = datetime.strptime(employment_date_from, '%Y-%m-%d')
    if employment_date_to:
        employment_date_to = datetime.strptime(employment_date_to, '%Y-%m-%d')

    # Pobieranie danych pracowników
    employees_query = Employee.query.filter(
        Employee.department_id == department_id,
        Employee.superior_id == superior_id
    )

    # Filtracja po dacie zatrudnienia, jeśli podane
    if employment_date_from:
        employees_query = employees_query.filter(Employee.date_of_employment >= employment_date_from)
    if employment_date_to:
        employees_query = employees_query.filter(Employee.date_of_employment <= employment_date_to)

    employees = employees_query.all()

    # Tworzenie DataFrame
    data = []
    for employee in employees:
        payrolls = Payroll.query.filter(
            Payroll.employee_id == employee.id,
            Payroll.year_month >= start_date,
            Payroll.year_month <= end_date
        ).all()
        for payroll in payrolls:
            data.append({
                'Employee ID': employee.id,
                'Name': f"{employee.first_name} {employee.last_name}",
                'Date of Employment':employee.date_of_employment,
                'Month': payroll.year_month.strftime('%Y-%m'),
                'Base': float(payroll.base),
                'Overtime': float(payroll.overtime),
                'Additional': float(payroll.additional),
                'Deductions': float(payroll.deductions),
                'Sum': float(payroll.sum)
            })

    df = pd.DataFrame(data)
    
    # Zapis do pliku Excel
    excel_path = 'payroll_report.xlsx'
    df.to_excel(excel_path, index=False)

    return send_file(excel_path, as_attachment=True, download_name='payroll_report.xlsx')


@api.route('/calculate-monthly-payroll', methods=['POST'])
def calculate_monthly_payroll():
    data = request.get_json()
    year_month = data.get('year_month')

    if not year_month:
        return jsonify({'error': 'Year_month is required.'}), 400

    try:
        year_month_date = datetime.strptime(year_month, "%Y-%m")
    except ValueError:
        return jsonify({'error': 'Invalid year_month format, expected YYYY-MM'}), 400

    employees = Employee.query.filter(Employee.activity == '1').all()  # Assuming '1' means active

    for employee in employees:
        worked_hours = calculate_worked_hours(employee.id, year_month_date)
        paid_absence_hours = calculate_paid_absences(employee.id, year_month_date)

        total_hours = Decimal(worked_hours) + Decimal(paid_absence_hours)
        hours_difference = total_hours - (168 * employee.part_time)

        if hours_difference > 0:
            overtime = hours_difference
            deductions = 0
        else:
            overtime = 0
            deductions = abs(hours_difference)

        if overtime > 0:
            overtime_record = Overtime(
                employee_id=employee.id,
                year_month=year_month_date,
                number_of_hours=overtime,
                hour_multiplier=Decimal(1.5),
                confirmation='1'
            )
            db.session.add(overtime_record)

        payroll = Payroll(
            employee_id=employee.id,
            year_month=year_month_date,
            base=employee.hourly_rate * 168 * employee.part_time,
            overtime=overtime * employee.hourly_rate * Decimal(1.5),
            additional=Decimal(0),
            deductions=deductions * employee.hourly_rate,
            sum=employee.hourly_rate * 168 * employee.part_time + overtime * employee.hourly_rate * Decimal(1.5) - deductions
        )
        db.session.add(payroll)

    db.session.commit()
    return jsonify({'message': 'Monthly payroll calculated for all active employees successfully'}), 200

def calculate_worked_hours(employee_id, date):
    hours = db.session.query(func.sum(
        extract('hour', Presence.time_of_exit) - extract('hour', Presence.time_of_entry)
    )).filter(
        Presence.employee_id == employee_id,
        func.date_trunc('month', Presence.date) == date
    ).scalar() or 0
    return hours

def calculate_paid_absences(employee_id, date):
    hours = db.session.query(func.sum(
        (func.cast(Absence.end_date, Date) - func.cast(Absence.start_date, Date) + 1).cast(Numeric) *
        8 *
        (func.cast(AbsenceType.payment_percentage, Float) / 100)
    )).select_from(Absence).join(AbsenceType).filter(
        Absence.employee_id == employee_id,
        func.date_trunc('month', Absence.start_date) == date
    ).scalar() or 0
    return hours

@api.route('/managers', methods=['GET'])
def get_managers():
    managers = Employee.query.filter(Employee.superior_id.is_(None)).all()
    if managers:
        return jsonify([manager.to_dict() for manager in managers]), 200
    else:
        return jsonify({"message": "No managers found"}), 404
    
@api.route('/presences/bulk', methods=['POST'])
def add_presences_bulk():
    data = request.get_json()
    if 'presences' not in data or not isinstance(data['presences'], list):
        return jsonify({"error": "Invalid data format, expected a list of presences."}), 400

    new_presences = []
    for presence_data in data['presences']:
        try:
            new_presence = Presence(
                date=datetime.strptime(presence_data['date'], '%Y-%m-%d').isoformat(),
                time_of_entry=datetime.strptime(presence_data['time_of_entry'], '%H:%M:%S').time(),
                time_of_exit=datetime.strptime(presence_data['time_of_exit'], '%H:%M:%S').time(),
                comment=presence_data.get('comment', ''),
                employee_id=presence_data['employee_id']
            )
            new_presences.append(new_presence)
        except KeyError as e:
            return jsonify({"error": f"Missing required data: {str(e)}"}), 400
        except ValueError as e:
            return jsonify({"error": f"Invalid date or time format: {str(e)}"}), 400

    db.session.add_all(new_presences)
    db.session.commit()
    return jsonify({"message": "Presences added successfully", "count": len(new_presences)}), 201

@api.route('/overtime', methods=['GET'])
def get_overtime():
    overtime_list = Overtime.query.all()
    return jsonify([overtime.to_dict() for overtime in overtime_list]), 200

@api.route('/allowancetype' , methods = ['GET'])
def get_allowance_list():
    allowance_list = AllowanceType.query.all()
    return jsonify([allowance.to_dict() for allowance in allowance_list]), 200



@api.route('/allowanceassignment',methods= ['POST'])
def assing_allowance():
    data = request.get_json()
    new_allowance = AllowanceAssignment(
    allowance_id = data['allowance_id'],
    payroll_id = data['payroll_id']

    )
    db.session.add(new_allowance)
    db.session.commit()
    return make_response(jsonify(new_allowance.to_dict()), 201)

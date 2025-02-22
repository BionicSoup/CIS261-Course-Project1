from datetime import datetime

def get_dates():
    while True:
        try:
            from_date = input("Enter the from date (mm/dd/yyyy): ")
            to_date = input("Enter the to date (mm/dd/yyyy): ")
            datetime.strptime(from_date, "%m/%d/%Y")
            datetime.strptime(to_date, "%m/%d/%Y")
            return from_date, to_date
        except ValueError:
            print("Invalid date format. Please use mm/dd/yyyy.")

def collect_employee_data():
    employees = []
    while True:
        from_date, to_date = get_dates()
        name = input("Enter employee name: ")
        hours_worked = float(input("Enter total hours worked: "))
        hourly_rate = float(input("Enter hourly rate: "))
        tax_rate = float(input("Enter income tax rate (%): "))

        employees.append({
            "from_date": from_date,
            "to_date": to_date,
            "name": name,
            "hours_worked": hours_worked,
            "hourly_rate": hourly_rate,
            "tax_rate": tax_rate
        })

        another = input("Enter another employee? (yes/no): ").strip().lower()
        if another != "yes":
            break
    return employees

def calculate_payroll(employees):
    totals = {
        "num_employees": 0,
        "total_hours": 0,
        "total_tax": 0,
        "total_net_pay": 0
    }

    for emp in employees:
        gross_pay = emp["hours_worked"] * emp["hourly_rate"]
        income_tax = gross_pay * (emp["tax_rate"] / 100)
        net_pay = gross_pay - income_tax

        emp["gross_pay"] = gross_pay
        emp["income_tax"] = income_tax
        emp["net_pay"] = net_pay

        totals["num_employees"] += 1
        totals["total_hours"] += emp["hours_worked"]
        totals["total_tax"] += income_tax
        totals["total_net_pay"] += net_pay

    return employees, totals

def display_results(employees, totals):
    print("\nEmployee Payroll Details:")
    for emp in employees:
        print(f"\n{emp['name']} ({emp['from_date']} - {emp['to_date']})")
        print(f"Hours Worked: {emp['hours_worked']}")
        print(f"Hourly Rate: ${emp['hourly_rate']:.2f}")
        print(f"Gross Pay: ${emp['gross_pay']:.2f}")
        print(f"Tax Rate: {emp['tax_rate']}%")
        print(f"Income Tax: ${emp['income_tax']:.2f}")
        print(f"Net Pay: ${emp['net_pay']:.2f}")

    print("\nPayroll Summary:")
    print(f"Total Employees: {totals['num_employees']}")
    print(f"Total Hours: {totals['total_hours']}")
    print(f"Total Tax: ${totals['total_tax']:.2f}")
    print(f"Total Net Pay: ${totals['total_net_pay']:.2f}")

# Run the program
employees = collect_employee_data()
processed_employees, totals = calculate_payroll(employees)
display_results(processed_employees, totals)

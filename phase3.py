from datetime import datetime

# File name for storing employee data
EMPLOYEE_FILE = "employees.txt"

def save_employee_data(from_date, to_date, employee_name, hours_worked, pay_rate, tax_rate):
    """Save employee data to file in pipe-delimited format."""
    record = f"{from_date}|{to_date}|{employee_name}|{hours_worked}|{pay_rate}|{tax_rate}\n"
    with open(EMPLOYEE_FILE, "a") as file:  # Append mode to add data
        file.write(record)

def get_valid_date(prompt):
    """Get and validate date input in mm/dd/yyyy format."""
    while True:
        date_str = input(prompt).strip()
        if date_str.lower() == "all":
            return date_str
        try:
            datetime.strptime(date_str, "%m/%d/%Y")
            return date_str
        except ValueError:
            print("Invalid date format. Use mm/dd/yyyy or 'All'.")

def calculate_payroll(from_date, records):
    """Calculate and display payroll for records matching from_date or 'All'."""
    total_employees = 0
    total_hours = 0
    total_tax = 0
    total_net_pay = 0
    payroll_data = {}

    for record in records:
        parts = record.strip().split("|")
        if len(parts) != 6:
            continue
        rec_from_date, rec_to_date, name, hours, rate, tax = parts

        # Match records based on from_date or 'All'
        if from_date.lower() == "all" or rec_from_date == from_date:
            hours = float(hours)
            rate = float(rate)
            tax_rate = float(tax)
            gross_pay = hours * rate
            income_tax = gross_pay * tax_rate
            net_pay = gross_pay - income_tax

            # Display payroll for this employee
            print(f"From Date: {rec_from_date}, To Date: {rec_to_date}")
            print(f"Employee: {name}, Hours Worked: {hours}, Hourly Rate: {rate:.2f}")
            print(f"Gross Pay: {gross_pay:.2f}, Income Tax Rate: {tax_rate:.2%}, Income Taxes: {income_tax:.2f}")
            print(f"Net Pay: {net_pay:.2f}\n")

            # Update totals
            total_employees += 1
            total_hours += hours
            total_tax += income_tax
            total_net_pay += net_pay
            payroll_data[name] = (hours, rate, gross_pay, tax_rate, income_tax, net_pay)

    return total_employees, total_hours, total_tax, total_net_pay

def main():
    # Initial data entry loop
    while True:
        employee_name = input("Enter employee name (or 'quit' to exit): ").strip()
        if employee_name.lower() == 'quit':
            break

        from_date = input("Enter from date (mm/dd/yyyy): ").strip()
        to_date = input("Enter to date (mm/dd/yyyy): ").strip()
        hours_worked = float(input("Enter hours worked: "))
        pay_rate = float(input("Enter pay rate: "))
        tax_rate = float(input("Enter income tax rate (as decimal, e.g., 0.25 for 25%): "))

        save_employee_data(from_date, to_date, employee_name, hours_worked, pay_rate, tax_rate)
        print("Employee data saved.\n")

    # Get report date and process payroll
    from_date = get_valid_date("Enter From Date for report (mm/dd/yyyy) or 'All' for all records: ")
    with open(EMPLOYEE_FILE, "r") as file:
        records = file.readlines()
    
    totals = calculate_payroll(from_date, records)
    total_employees, total_hours, total_tax, total_net_pay = totals

    # Display totals
    print("\nPayroll Totals:")
    print(f"Total Employees: {total_employees}")
    print(f"Total Hours: {total_hours:.2f}")
    print(f"Total Tax: {total_tax:.2f}")
    print(f"Total Net Pay: {total_net_pay:.2f}")

if __name__ == "__main__":
    main()

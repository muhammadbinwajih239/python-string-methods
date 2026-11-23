employee_id = input("Enter your Employee ID: ")

employee_id = employee_id.strip()

if (
    employee_id.startswith("EMP-")
    and len(employee_id) == 8
    and employee_id[4:].isdigit()
):
    print(f"Valid Employee ID: {employee_id}")
else:
    print("Invalid Employee ID.")

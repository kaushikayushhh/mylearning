# Employee Data
employees = {
    101: {"name": "Satya", "age": 27, "department": "HR", "salary": 50000},
    102: {"name": "Ayush", "age": 25, "department": "AI", "salary": 60000}
}

# Add Employee
def add_employee():
    try:
        emp_id = int(input("Enter Employee ID: "))

        if emp_id in employees:
            print("Employee ID already exists!\n")
            return

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        department = input("Enter Department: ")
        salary = int(input("Enter Salary: "))

        employees[emp_id] = {
            "name": name,
            "age": age,
            "department": department,
            "salary": salary
        }

        print("Employee Added Successfully!\n")

    except ValueError:
        print("Invalid Input! Please enter correct data types.\n")


# View Employees
def view_employees():
    if len(employees) == 0:
        print("No employees available.\n")
        return

    print("\nID\tName\tAge\tDepartment\tSalary")
    print("-" * 50)

    for emp_id, details in employees.items():
        print(emp_id, "\t", details["name"], "\t", details["age"],
              "\t", details["department"], "\t", details["salary"])
    print()


# Search Employee
def search_employee():
    try:
        emp_id = int(input("Enter Employee ID to search: "))

        if emp_id in employees:
            details = employees[emp_id]
            print("\nEmployee Found:")
            print("Name:", details["name"])
            print("Age:", details["age"])
            print("Department:", details["department"])
            print("Salary:", details["salary"], "\n")
        else:
            print("Employee Not Found.\n")

    except ValueError:
        print("Please enter a valid ID.\n")


# Main Menu
def main():
    while True:
        print("====== Employee Management System ======")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            print("Thank you! Program Ended.")
            break
        else:
            print("Invalid Choice! Try again.\n")


# Run Program
main()
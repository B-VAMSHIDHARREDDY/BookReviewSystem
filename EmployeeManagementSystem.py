import json

class Employee:
    def __init__(self, name, employee_id, title, department):
        self.name = name
        self.employee_id = employee_id
        self.title = title
        self.department = department

    def display_details(self):
        print(f"Name: {self.name}, ID: {self.employee_id}, Title: {self.title}, Department: {self.department}")

    def __str__(self):
        return f"{self.name} - {self.employee_id}"

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee_id):
        self.employees = [emp for emp in self.employees if emp.employee_id != employee_id]

    def list_employees(self):
        for employee in self.employees:
            print(employee)

class Company:
    def __init__(self):
        self.departments = {}

    def add_department(self, department):
        self.departments[department.name] = department

    def remove_department(self, department_name):
        if department_name in self.departments:
            del self.departments[department_name]
        else:
            print("Department not found.")

    def display_departments(self):
        for department_name, department in self.departments.items():
            print(f"Department: {department_name}")
            department.list_employees()
            print("\n")

def save_to_file(company, filename="company_data.json"):
    data = {"departments": {}}
    for department_name, department in company.departments.items():
        data["departments"][department_name] = [{"name": emp.name, "id": emp.employee_id, "title": emp.title}
                                               for emp in department.employees]
    with open(filename, "w") as file:
        json.dump(data, file)

def load_from_file(filename="company_data.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            company = Company()
            for department_name, employees in data["departments"].items():
                department = Department(department_name)
                for emp_data in employees:
                    employee = Employee(emp_data["name"], emp_data["id"], emp_data["title"], department_name)
                    department.add_employee(employee)
                company.add_department(department)
            return company
    except FileNotFoundError:
        return Company()

def main():
    company = load_from_file()

    while True:
        print("\nEmployee Management System Menu:")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Display Departments")
        print("4. Add Department")
        print("5. Remove Department")
        print("6. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter employee name: ")
            employee_id = input("Enter employee ID: ")
            title = input("Enter employee title: ")
            department = input("Enter department name: ")

            if department in company.departments:
                employee = Employee(name, employee_id, title, department)
                company.departments[department].add_employee(employee)
                print("Employee added successfully.")
            else:
                print("Department not found. Please add the department first.")

        elif choice == "2":
            employee_id = input("Enter employee ID to remove: ")

            for department in company.departments.values():
                department.remove_employee(employee_id)

            print("Employee removed successfully.")

        elif choice == "3":
            company.display_departments()

        elif choice == "4":
            department_name = input("Enter department name: ")
            department = Department(department_name)
            company.add_department(department)
            print("Department added successfully.")

        elif choice == "5":
            department_name = input("Enter department name to remove: ")
            company.remove_department(department_name)

        elif choice == "6":
            save_to_file(company)
            print("Data saved. Exiting.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

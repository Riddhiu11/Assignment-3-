"""
Report Generation Module

This module provides a function for generating reports based on employee data.
"""

def generate_reports():
    """
    Generate Reports Function

    This function generates various reports based on employee data, such as:
    - List of departments
    - List of all employees with ID, full name, and department
    - List of all departments with the average age and salary of employees
    - List of employees in each department with ID, full name, date of birth, salary,
      and total salary for department's employees
    """
def generate_reports(employees_data):
    departments = set()
    department_employees = {}

    # Collecting data for reports
    for employee in employees_data:
        department = employee[3]
        departments.add(department)
        if department not in department_employees:
            department_employees[department] = []
        department_employees[department].append(employee)


    print("List of departments:")
    for department in departments:
        print("- ", department)


    print("\nList of all employees with ID, full name, and department:")
    for employee in employees_data:
        print("- ID:", employee[0], "Full Name:", employee[1], "Department:", employee[3])


    print("\nList of all departments with the average age and salary of employees:")
    for department, employees in department_employees.items():
        total_age = sum(int(employee[2]) for employee in employees)
        average_age = total_age / len(employees)
        total_salary = sum(float(employee[4]) for employee in employees)
        average_salary = total_salary / len(employees)
        print("- Department:", department, "Average Age:", average_age, "Average Salary:", average_salary)


    print("\nList of employees in each department with ID, full name, date of birth, salary, and total salary for department's employees:")
    for department, employees in department_employees.items():
        print("\nDepartment:", department)
        for employee in employees:
            print("- ID:", employee[0], "Full Name:", employee[1], "Date of Birth:", employee[2], "Salary:", employee[4])
        total_salary_department = sum(float(employee[4]) for employee in employees)
        print("Total Salary for Department's Employees:", total_salary_department)


employees_data = [
    ["1", "Ansh Patel", "30", "Male", "Manager", 50000.0, "01/01/1990"],
    ["2", "Riddhi Patel", "25", "Female", "Developer", 60000.0, "05/05/1995"],
    ["3", "Rudra Patel", "35", "Male", "Accountant", 55000.0, "10/10/1985"],
    ["4", "Shefali Macwan", "28", "Female", "Developer", 65000.0, "03/03/1996"]
]

generate_reports(employees_data)
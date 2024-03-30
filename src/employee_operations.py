"""
Employee Operations Module

This module provides functions for adding, deleting, and updating employee information.
"""

def add_employee():
    """
    Add Employee Function

    This function prompts the user to input details for a new employee and adds the employee
    to the system.
    """

def add_employee(employee_list):
    employee_id = input("Enter the ID of the new employee: ")
    employee_name = input("Enter the name of the new employee: ")


    new_employee = {'id': employee_id, 'name': employee_name}


    employee_list.append(new_employee)
    print("Employee added successfully.")

    return employee_list

employees = [
    {'id': '001', 'name': 'Riddhi'},
    {'id': '002', 'name': 'Ansh'},
    {'id': '003', 'name': 'Mike'}
]

print("Before adding new employee:")
print(employees)

def delete_employee():
    """
    Delete Employee Function

    This function prompts the user to input the ID of the employee to be deleted and
    removes the employee from the system.

    """
def delete_employee(employee_list):
    employee_id = input("Enter the ID of the employee to be deleted: ")

    for employee in employee_list:
        if employee['id'] == employee_id:
            employee_list.remove(employee)
            print(f"Employee with ID {employee_id} has been deleted.")
            return

    print(f"Employee with ID {employee_id} not found.")



employees = [
    {'id': '001', 'name': 'Riddhi'},
    {'id': '002', 'name': 'Ansh'},
    {'id': '003', 'name': 'Mike'}
]

delete_employee(employees)
print("Updated employee list:")
print(employees)
def update_employee():
    """
    Update Employee Function

    This function prompts the user to input the ID of the employee to be updated and
    allows the user to modify the employee's information such as name, department, or salary.

    """
def update_employee(employee_list):

    employee_id = input("Enter the ID of the employee to be updated: ")

    for employee in employee_list:
        if employee['id'] == employee_id:
            print("Employee found. Please update the employee's information:")
            choice = input("What do you want to update? (name/department/salary): ").lower()


            if choice == 'name':
                new_name = input("Enter the new name: ")
                employee['name'] = new_name
                print("Name updated successfully.")
            elif choice == 'department':
                new_department = input("Enter the new department: ")
                employee['department'] = new_department
                print("Department updated successfully.")
            elif choice == 'salary':
                new_salary = input("Enter the new salary: ")
                employee['salary'] = new_salary
                print("Salary updated successfully.")
            else:
                print("Invalid choice.")

            return


    print(f"Employee with ID {employee_id} not found.")


employees = [
    {'id': '001', 'name': 'Riddhi', 'department': 'HR', 'salary': '50000'},
    {'id': '002', 'name': 'Ansh', 'department': 'IT', 'salary': '60000'},
    {'id': '003', 'name': 'Mike', 'department': 'Finance', 'salary': '55000'}
]

print("Before updating employee:")
print(employees)

update_employee(employees)

print("After updating employee:")
print(employees)
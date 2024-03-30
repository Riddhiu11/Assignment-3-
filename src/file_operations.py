"""
File Operations Module

This module provides functions for reading from and writing to the text file
that stores employee data.
"""
def read_employees():
    """
    Read Employees Function

    This function reads employee data from the text file and returns it.

    Returns:
        list: A list containing employee data read from the text file.
    """
def read_employees(file_path):

    employees = []
    try:
        with open(file_path, 'r') as file:
            for line in file:

                employee_data = line.strip().split(',')

                employee = {
                    'id': employee_data[0],
                    'name': employee_data[1],
                    'department': employee_data[2],
                    'salary': employee_data[3]
                }
                employees.append(employee)
    except FileNotFoundError:
        print("Error: File not found.")
    return employees


file_path = "employees.txt"
employees_data = read_employees(file_path)
print("Employees data read from file:")
print(employees_data)

def write_employees():
    """
    Write Employees Function

    This function writes employee data to the text file.

    Parameters:
        employees_data (list): A list containing employee data to be written to the text file.
    """
def write_employees_data(employees_data):
    try:
        with open("employees.txt", "w") as file:
            for employee in employees_data:
                file.write(",".join(employee) + "\n")
        print("Employee data has been successfully written to employees.txt")
    except Exception as e:
        print("An error occurred while writing employee data:", e)

# Example usage:
employees_data = [
    ["Riddhi", "30", "Female", "Manager"],
    ["Ansh", "25", "Male", "Developer"],
    ["Mike", "35", "Male", "Accountant"]
]

write_employees_data(employees_data)
class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"{self.emp_id} {self.name} {self.age} {self.salary}"

def sort_employee_data(employees, sort_param):
    if sort_param == 1:
        employees.sort(key=lambda x: x.age, reverse=True)
    elif sort_param == 2:
        employees.sort(key=lambda x: x.name)
    elif sort_param == 3:
        employees.sort(key=lambda x: x.salary, reverse=True)
    else:
        print("Invalid sorting parameter")
        return

    print("Sorted Employee Data:")
    for emp in employees:
        print(emp)

if __name__ == '__main__':
    employees = [
        Employee('161E90', 'Raman', 41, 56000),
        Employee('161F91', 'Himadri', 38, 67500),
        Employee('161F99', 'Jaya', 51, 82100),
        Employee('171E20', 'Tejas', 30, 55000),
        Employee('171G30', 'Ajay', 45, 44000)
    ]

    sort_param = int(input("Enter sorting parameter (1. Age, 2. Name, 3. Salary): "))
    sort_employee_data(employees, sort_param)
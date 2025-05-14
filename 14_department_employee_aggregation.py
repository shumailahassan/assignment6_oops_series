#14. Aggregation:mCreate a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.# Employee class
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def show_details(self):
        print(f"Employee Name: {self.name}, ID: {self.emp_id}")


# Department class
class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee  # Aggregation: reference only

    def show_department_info(self):
        print(f"Department: {self.department_name}")
        self.employee.show_details()  # Aggregated object ka method call


# Employee object create kiya (independent object)
emp1 = Employee("Shumaila", 1010)

# Department object create kiya, lekin employee ka reference diya
dept1 = Department("Human Resources", emp1)

# Show department info (with employee details)
dept1.show_department_info()





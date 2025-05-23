#Employee Management 
#Store employee details using classes and show details of employees in a specific department. 
class Employee:
    def __init__(self, name, emp_id, department):
        self.name = name
        self.emp_id = emp_id
        self.department = department
 
    def show_details(self):
        print("Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Department:", self.department)
        print("------------------------")
        
employees = []
 
# Adding some employees manually
employees.append(Employee("Seema", 101, "HR"))
employees.append(Employee("Ravi", 102, "IT"))
employees.append(Employee("Anita", 103, "Finance"))
employees.append(Employee("Raj", 104, "IT"))
 
# Ask user for department to search
search_dept = input("Enter department to display employees: ")
 
print("\nEmployees in", search_dept, "department:\n")
for emp in employees:
    if emp.department.lower() == search_dept.lower():
        emp.show_details()
class Employee:
    def __init__(self, empid, name, address, contact, spouse, children, salary):
        self.empid = empid
        self.name = name
        self.address = address
        self.contact = contact
        self.spouse = spouse
        self.children = children
        self.salary = salary
    
    def display(self):
        print(f"ID: {self.empid}, Name: {self.name}, Salary: {self.salary}")

employees = []
while True:
    try:
        print("\nEnter employee details:")
        empid = int(input("ID: "))
        name = input("Name: ")
        address = input("Address: ")
        contact = input("Contact: ")
        spouse = input("Spouse Name: ")
        children = int(input("Number of children: "))
        salary = float(input("Salary: "))
        emp = Employee(empid, name, address, contact, spouse, children, salary)
        employees.append(emp)
        more = input("Add another? (y/n): ")
        if more.lower() != 'y':
            break
    except ValueError:
        print("Invalid input. Try again.")

with open("employees.csv", "w") as f:
    f.write("ID,Name,Address,Contact,Spouse,Children,Salary\n")
    for emp in employees:
        f.write(f"{emp.empid},{emp.name},{emp.address},{emp.contact},{emp.spouse},{emp.children},{emp.salary}\n")

print("\nAll employees:")
for emp in employees:
    emp.display()
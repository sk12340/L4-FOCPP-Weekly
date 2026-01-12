class Student:
    def __init__(self, id, name, address, year, level, section):
        self.id = id
        self.name = name
        self.address = address
        self.year = year
        self.level = level
        self.section = section
    
    def display(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Admission Year: {self.year}")
        print(f"Level: {self.level}")
        print(f"Section: {self.section}")

id = input("Enter ID: ")
name = input("Enter Name: ")
address = input("Enter Address: ")
year = input("Enter Admission Year: ")
level = input("Enter Level: ")
section = input("Enter Section: ")

s = Student(id, name, address, year, level, section)
s.display()
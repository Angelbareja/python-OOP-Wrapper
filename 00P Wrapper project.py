class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print("Name : {self.name}")
        print("Age : {self.age}")
        
class Employee:
    def __init__(self,name,age,eid,salary):
        self.name = name
        self.age = age
        self.eid = eid
        self.salary = salary
        
    def diplay(self):
        print("Name : {self.name}")
        print("Age : {self.age}")
        print("eid : {self.eid}")
        print("salary : {self.salary}")
        
class Manager:
    def __init__(self,name,age,eid,salary,department):
        self.name = name
        self.age = age
        self.eid = eid
        self.salary = salary
        self.department = department
        
    def diplay(self):
        print("Name : {self.name}")
        print("Age : {self.age}")
        print("eid : {self.eid}")
        print("salary : {self.salary}")
        print("Department : {self.department}")

print("---Python OOP project : Employee Management system---")
while True:
    print("choose an operation:")
    print("1.Create a Person")
    print("2.Create an Employee")
    print("3.Create a Manager")
    print("4.Show Details")
    print("5.Exit\n")

    choice = int(input("Enter your choice : "))
    print("\n-----choice another operation-----\n")

    if choice == 1:
        name = input("Enter Name : ")
        age = int(input("Enter Age : "))
        print("\n")
        Person = Person(name , age)       
        print(f"person created with Name : {Person.name} and Age : {Person.age}")         
        print("\n")

    elif choice == 2:
        name = input("Enter Name : ")
        age = int(input("Enter Age : "))
        eid = input("Enter Employee ID :")
        salary = int(input("Enter salary : "))
        print("\n")
        Employee = Employee(name,age,eid,salary)
        print(f"Employee created with Name : {Employee.name} , Age : {Employee.age} , ID : {Employee.eid} , and Salary : {Employee.salary}")
        
    elif choice == 3:
        name = input("Enter Name : ")
        age = int(input("Enter Age : "))
        eid = input("Enter Employee ID :")
        salary = int(input("Enter salary : "))
        department = input("Enter Department : ")
        print("\n")
        Manager = Manager(name,age,eid,salary,department)
        print(f"Employee created with Name : {Manager.name} , Age : {Manager.age} , ID : {Manager.eid} , Salary : {Manager.salary} , and Department : {Manager.department}")
        print("\n")

    elif choice == 4:
        print("Choose detail to show : ")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")

        cho = int(input("Enter your choice "))
        print("\n")

        if cho == 1:
            print("Person Details : ")
            print(f"Enter Name : {Person.name}")
            print(f"Enter Age : {Person.age}")
            print("\n")
        
        elif cho == 2:
            print("Employee Details : ")
            print(f"Enter Name : {Employee.name}")
            print(f"Enter Age : {Employee.age}")
            print(f"Enter Employee ID : {Employee.eid}")
            print(f"Enter Salary : {Employee.salary}")
            print("\n")

        elif cho == 3:
            print("Employee Details : ")
            print(f"Enter Name : {Employee.name}")
            print(f"Enter Age : {Employee.age}")
            print(f"Enter Employee ID : {Employee.eid}")
            print(f"Enter Salary : {Employee.salary}")
            print(f"Enter Department : {Employee.department}")
            print("\n")

        else:
            print("Enter vaild Number..")
            print("\n")


    elif choice == 5:
        print("Exiting the system. All resources have been freed.")
        print("\n")
        break
        
    else:
        print("Goodbye!")


            

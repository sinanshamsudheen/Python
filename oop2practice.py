class Circle:
    def __init__(self,radius):
        self.r = radius

    def Area(self):
        area=3.14*(self.r**2)
        print("The area is :",area)
    def Perimeter(self):
        per=2*3.14*self.r
        print("the perimeter is :",per)

c1=Circle(5)
c1.Area()
c1.Perimeter()

class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary
    def showDetails(self):
        print("the role :",self.role)
        print("department :",self.department)
        print("salary :",self.salary) 

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT","75000")
    

e1 = Employee("salesman","store","40000")
e1.showDetails()

eng= Engineer("sinan","20")
print(eng.name)
print(eng.salary)
eng.showDetails()

class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,odr2):       
        return self.price>odr2.price

odr1= Order("bread",35)
odr2= Order("tea",15)
print(odr1>odr2)

"""o/p
The area is : 78.5
the perimeter is : 31.400000000000002
the role : salesman
department : store
salary : 40000
sinan
75000
the role : Engineer
department : IT
salary : 75000"""

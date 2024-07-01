class student:
    __student_id = 69 #Adding "__" behind an object will make it private
    def __init__(self,name,age):
        self.name=name
        self.age=age


s1=student("sinan",20)
print(s1.name)
del(s1.name) #to delete an element
# print(s1.name)
# print(s1.student_id) #inaccessible

#INHERITANCE
# 1, single inheritance 
class Car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car):
    def __init__(self, name,type):
        super().__init__(type) #super method
        self.name=name
    
car1=ToyotaCar("fortuner","electric")
print(car1.name)
print(car1.type)

car1.start()

# 2, multilevel inheritance
class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand=brand

class fortuner(ToyotaCar):
    def __init__(self,type):
        self.type=type

car1=fortuner("diesel")
print(car1.type)
car1.start()

# 3,Multiple inheritance
class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"
class C(A,B):
    varC = "welcome to class C"

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)

#Class method

class Person:
    name = "anonymous"

    """def changeName(self,name):
        self.name=name
        Person.name=name -> first way
        self.__class__.name= "liza" -> 2nd way"""
    #classmethod can be used instead of the above fn
    @classmethod
    def changeName(cls,name):
        cls.name=name
    
p1 = Person()
p1.changeName("sinan")
print(p1.name)
print(Person.name)

#Property method
class stud:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
    # def calcPercentage(self):
    #     self.percentage=str((self.phy + self.chem+self.math)/3) + "%"
    @property
    def percentage(self):
        return str((self.phy + self.chem+self.math)/3) + "%"

stu1=stud(98,97,99)
print(stu1.percentage)
stu1.phy=86
print(stu1.percentage)

o/p 
"""sinan
fortuner
electric
car started..
diesel
car started..
welcome to class A
welcome to class B
welcome to class C
sinan
sinan
98.0%
94.0%"""
#the remaining part of oops2 is covered in the "polymorphism.py"
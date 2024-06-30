class car:
    color = "blue"
    brand = "mercedes"
    def __init__(self):
        print("Adding new car..") #constructor

car1 = car() #An object is an instance of class
car1.color="red"
print(car1.color)
print(car.color)

class student:
    def __init__(self, fullname, marks):
        self.name=fullname
        self.marks=marks
        print("adding new student..")
    
    def welcome(self):
        print("Welcome student,",self.name)


s1=student("sinan",95)
print(s1.name,s1.marks)
s1.welcome()

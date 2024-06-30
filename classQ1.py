#create student class that takes name & marks of 3 subjects sa arguments in constructor.
# then create a metod to print the average.

class student:
    def __init__(self, name, mark1, mark2, mark3):
        self.name=name
        self.sub1=mark1
        self.sub2=mark2
        self.sub3=mark3
        print("adding student..")
    def average(self):
        avg=(self.sub1+self.sub2+self.sub3)/3
        print("The average is:",avg)

    @staticmethod
    def college():
        print("sctce")

    
s1=student("sinan",56,57,34)
print(s1.name)

s2=student("Liza",79,89,99)
s1.average()
s2.average()
s2.college()

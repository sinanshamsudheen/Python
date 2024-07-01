# polymorphism -> operator overloading
# when the same operator is allowed to have different meaning according to the context.

print(1+3) #4 - sum
print("sinan" + "liza") #sinanliza - concatenate
print([1,2,3] + [4,5,6]) #[1, 2, 3, 4, 5, 6] - merge

class Complex:
    def __init__(self, real, img):
        self.real=real
        self.img=img
    def showNumber(self):
        print(self.real,"i +",self.img,"j")
    
    def __add__(self,num2): #dunder function
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return Complex(newReal,newImg)

    def __sub__(self,num2): #dunder function
        newReal=self.real-num2.real
        newImg=self.img+num2.img
        return Complex(newReal,newImg)

num1=Complex(1,3)
num1.showNumber()

num2=Complex(4,9)
num2.showNumber()

num3=num1+num2
num3.showNumber()

num4=num1-num2
num4.showNumber()
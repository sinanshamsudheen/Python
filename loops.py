#reverse a number
# n=(int)

sum = 0
i=0
n = int(input("enter the n value "))
while i<n :
    val = int(input("enter the number to add : "))
    sum=sum+val
    i+=1
print(sum)

nums = [1,2,3,4,5]
str = "sinan"
for valueee in nums:
    print(valueee)

for love in str:
    print(love)
else:
    print("loves liza\n")
print("\n")

#Range(start?,stop,step?)
for el in range(5):
    print(el)
print("\n")
for el in range(1,5):
    print(el)
print("\n")
for el in range(1,5,2):
    print(el)

#pass statment - to just pass through a loop without doing anything
for i in range(3):
    pass
print("hello")
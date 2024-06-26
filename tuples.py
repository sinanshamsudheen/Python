#A built-in data type that lets us create immutable sequences of values.

tup=(89,69,45,45)
#tup[0]=47 - Not allowed
print(tup[0])

tup1=("hello",) 
print(type(tup1))
tup1=("hello")
print(type(tup1)) 

#tuple methods
print(tup.index(69))
print(tup.count(45))


#conditional statements
a = int(input("enter the age :"))

if(a>=18):
    print("You can vote.")
elif(a<18 and a>11):
    print("You are a teenager.")
else:
    print("You are a child.")

#Single line if/ternary operator
# <var>=<val1> if<condition> else<val2>
food=input("food : ")
eat="yes" if food=="cake" else "no"
print(eat)

# <stt1> if<condition>else<stt2>
print("sweet") if food=="cake" or food=="jalebi" else print("not sweet")

#Clever if
# <var>=(false_val,true_val)[<condition>]

sal=float(input("salary : "))
tax=sal*(0.1,0.2)[sal<=50000]
print(tax)
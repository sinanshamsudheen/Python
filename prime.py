n = int(input("Enter the number : "))
flag=False
size=(int)(n/2)

for i in range(3,size+1):
    if(int(i%2)==0):
        flag=True
        break
    
if(flag==False):
    print("Is prime")
else:
    print("not prime")


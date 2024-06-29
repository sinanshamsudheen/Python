
def fact(n):
    facto=1
    for i in range(1,n+1):
        facto=facto*i
    return facto

# with recursion
def factrec(n):
    if(n==0):
        return 1;
    else:
        return n*factrec(n-1)
    
n=int(input("Enter the num :"))
print(fact(n))
print(factrec(n))

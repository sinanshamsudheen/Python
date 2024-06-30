# built-in-functions

print("sinan",end="@")
print("liza") #end= "\n"
print("sahal")

books = ["english","korean","japanese","english","korean","japanese"]
for i in books:
    print(i,end=" ")
print(len(books))

def sum(a=4,b=5): #default parameters
    print(a+b)
sum(10,10)
sum()

"""O/P 
sinan@liza
sahal
english korean japanese english korean japanese 6    
20
9"""

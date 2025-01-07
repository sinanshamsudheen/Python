countries={
    'China':143,
    'India':136,
    'US':32,
    'Pakistan':21}

def printdict():
    for i in countries:
        s=f"{i}==>{countries[i]}"
        print(s)

n=input("enter input: ")
if n=="print":
    printdict()
elif n=="add":
    m=input("enter a country name to add: ")
    if m in countries:
        print("country already exists!")
    else:
        x=input("enter population: ")
        countries[m]=x
    printdict()
elif n=="remove":
    j=input("enter a country name to remove: ")
    if j in countries:
        del countries[j]
    else:
        print("no country found to delete.")
    printdict()
elif n=="query":
    k=input("enter the country for query: ")
    if k in countries:
        print(f"population of {k} is {countries[k]}")
    else:
        print("not country matches!")



import json
book={}
book['sinan']={
    'name':'ikigai',
    'date':'2016',
    'price':200
}
s=json.dumps(book)
with open("D:\IDM\jsonTest.txt","w+") as f:
    f.write(s)

r=open("D:\IDM\jsonTest.txt","r+")
t=r.read()
print(t)

book2=json.loads(t)
print(book2['sinan']['date'])

for person in book:
    print(book[person])

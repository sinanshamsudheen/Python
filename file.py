# text files and binary files, both are stored in bits

f = open("demo.txt","w+")
f.write("this is a new line\n")
data=f.read()
print(data)
f.close()

f=open("demo.txt","a+")
f.write("this is the next line")
data=f.read()
print(data)

f.seek(0)
data2 = f.readline()
print(data2)
f.close()

with open("demo.txt","r") as f:
    data=f.read()
    print(data)
#No need to close the file while using "with"

import os
os.remove("demo.txt")

O/P 
"""

this is a new line

this is a new line
this is the next line"""
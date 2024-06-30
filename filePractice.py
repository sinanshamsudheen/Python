f=open("practice.txt","w+")
f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.\n")
f.seek(0)
data=f.read()
print(data)

new_data=data.replace("Java","Python")
print(new_data)

f.close()
f=open("practice.txt","w")
f.write(new_data)

f.close()

def check_for_word(word):
    with open("practice.txt","r") as f:
        data=f.read()
        
        if(data.find(word) != -1):
            print("found")
        else:
            print("not found")

def pos_of_word(word):
    with open("practice.txt","r") as f:
        data = True
        line_no = 1
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1

    return -1
        
check_for_word("learning")
pos_of_word("learning")

"""O/P
Hi everyone
we are learning File I/O
using Java.
I like programming in Java.

Hi everyone
we are learning File I/O
using Python.
I like programming in Python.

found
2
"""
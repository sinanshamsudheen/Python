#Dictionaries are unordered, mutable & don't allow duplicate keys
student = {
    "id" : "007",
    "grade" : "A",
    "name" : "sinan",
    "topics" : ("dict","set"),
    "subjects" : ["python","C","java"],
    "age" : 20,
    "is_adult" : True,
    12.99 : 94.6
}

print(student)
print(student["subjects"])
student["name"]="Liza"
print(student)

null_dict = {}

null_dict["food"] = "cake"

print(null_dict)

#Nested dictionary

employee = {
    "name" : "Aadil Sandeep",
    "languages" : {
        "python" : 68,
        "java" : 89,
        "Cpp" : 99
    }
}

#dictionary functions
print(employee["languages"]["python"])
print(employee.keys()) #return all keys
print(list(employee.keys()))
print(employee.values()) #return all values

pairs = list(employee.items()) #return all (key,val) pairs as tuples
print(pairs[0])

print(employee.get("name")) #to return the value of a key

employee.update({"salary" : "69"}) #to update or add an item
print(employee)

employee.update({"name" : "lechmi"}) #overwriting is possible
print(employee)
list=[2,1,3]
print(list)

list.append(6)
print(list)

list.sort()
print(list)

list.sort(reverse=True)
print(list)

list.reverse()
print(list)

#list.insert(idx,el)
list.insert(0,"sinan")
print(list)

list.remove("sinan")
print(list)

list.pop(3)
print(list)

# O/P
"""[2, 1, 3]
[2, 1, 3, 6]
[1, 2, 3, 6]
[6, 3, 2, 1]
[1, 2, 3, 6]
['sinan', 1, 2, 3, 6]
[1, 2, 3, 6]
[1, 2, 3]"""

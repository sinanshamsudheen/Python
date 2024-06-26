list=[1,"abc","abc",1]

list2 = list.copy()
print(type(list2))

list2.reverse()
print(list2)

if(list2 == list):
    print("palindrome")
else:
    print("not a palindrome")
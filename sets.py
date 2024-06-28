#duplicate elements are avoided while printing
#SETS ARE MUTABLE
#SET ELEMENTS ARE IMMUTABLE

collection = {1,2,2,2,"hello","hello",4}

empty_set = set()
print(collection)
print(type(empty_set))

#set methods
empty_set.add("sinan") #adds an element
empty_set.add("liza")
print(empty_set)
empty_set.remove("sinan") #removes an element
print(empty_set)
empty_set.clear() #empties the set
print(empty_set)

empty_set.add(5)
empty_set.add(6)
empty_set.pop() #removes a random value
print(empty_set)

# tuple is hashable, ie value does not change 
# dict,set,lists are unhashable

set1={1,2,3}
set2={3,4,5}
print(set1.union(set2))
print(set1.intersection(set2))
myset={3,2,2,1}
print(myset)
print(1 in myset) # it search is the 1 in myset.it print Boolean value True/False
myset.add("test") #adding an element to the set
print(myset)

myset2={4,5,6}
myset.update(myset2) #update like extend in list. it join two sets
print(myset) 

myset2={4,5,6}
myset2.remove(4) #command remove is remove the element into a set
print(myset2)

myset2.discard(5) #or we can use this command
print(myset2)

myset2={5,6}
myset2.pop() #it remove element from the start 
print(myset2)

myset2.clear() # it gives us the empty element into a set
print(myset2)

myset3={1,2,3}
del myset3
#print(myset3) #error in the code because with command del we deleted myset3

myset1={1,2,3}
myset2={3,4,5}
myset3=myset1.union(myset2) #command union give us all elements in both sets
print(myset3)

"""
    
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others
    
"""
#adding tuple
tuple=(5,5,5,2,8,10)
print(tuple)
print(len(tuple)) #we can know about tuple's length 

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple) #ADDING element to the tuple

#                                 UNPACKING
#we can Unpack the  tuple like this
tuple=(1,2,3)
first,second,third=tuple
print(first,second,third)

tuple=(1,2,3)
first,second,*third=tuple
print(third)


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red) # it means that we take all elements without last because, the last element is cherry=red


#we can print all elements of tuple with loop for
tuple=(1,2,3)
for i in tuple:
    print(i)

""" 

count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found

"""
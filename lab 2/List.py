list2=[0,1,2]
print(list2)
print(len(list2)) #size of list or length of list2
print(type(list2))#we can know the type of the list with this command
newlist=list(("0","1","2"))


#                                 CHANGE THE ELEMENTS
list2[1]="3" # the second el. of the list equals to "3"
list2[0:2]="4,3 "#we can change the range of the list


#                                         ADD
list2.append("4")  #adding element to the end with command append
list2.insert(2,"5") # we change third element to the "5"

#                                         JOIN
list2=[1,2,3]
list3=[3,4,5]
list2.extend(list3) # we join to lists, now it equals to [1,2,3,3,4,5]
print(list2) 
#                                           LOOP
list=[1,2,3]
for i in range(len(list)): #from start to end of this list
    print(list[i]) # we print all elements
    

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits: # in list fruits
  if "a" in x:    #if we have letter "a" 
    newlist.append(x)   #append it to newlist

print(newlist) #print it

#                                  SORT
Ilist=[5,2,85,1]
Ilist.sort() # sorting Slist
print(Ilist)    

Wlist=['b','d','a']
Wlist.sort() # sorting Wlist
print(Wlist)    

thislist = [1,2,3,4,5]
thislist.sort(reverse = True)  #To sort decrease
print(thislist)  



#                                             COPY
firtslist=[1,2,3]
copiedlist=firtslist.copy()
print(copiedlist)


#                                             JOIN
list1=["a","b","c"]
list2=[1,2,3]
print(list1+list2)

list1=["a","b","c"]
list2=[1,2,3]
for i in list2:
    list1.append(i)
print(list1)


list1=["a","b","c"]
list2=[1,2,3]
list1.extend(list2)


"""

append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list

"""
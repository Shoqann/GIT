mydict={
    "Car":"Audi",
    "Model":"R8"
    
}
print(mydict)
print(mydict["Car"]) # it print us the second element of pair

x=mydict.get("Model") # x equals to the second element of pair
print(x)

x = mydict.keys() #x=keys of the dictionaries
print(x)

mydict["Model"]="RS8" # we can change or
mydict["Color"]="Darked-Blue" # we can add the elements like this
print(mydict)

print(mydict.values()) #Shows us values

print(mydict.items()) #Shows us all pairs 

if "Model" in mydict:#Check the elements with the key
    print("SURE")
    
mydict.update({"Color":"White"}) #Change the value of element and update dictionary
print(mydict)

mydict.pop("Color") #Remove key Color from dict.
print(mydict)
mydict.popitem() #remove last key 
print(mydict)

del mydict["Car"] #Delete key Car from dict.
print(mydict)

mydict.clear() #remove all elements
print(mydict)

mydict={
    "Car":"Audi",
    "Model":"R8"
}
for i in mydict.values():#print Values of dictionary
    print(i)
    
for i in mydict.keys():#print keys of dictionary
    print(i)
    
for x,y in mydict.items():#print all in the dict.
    print(x,y)
    
mydict2=mydict.copy() #copied the dictionary
print(mydict2)

MyFamily={
    "Me":{
        "age":"17",
    },
    "Brother":{
        "Age":"29"
    }
    
}
print(MyFamily)

"""
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary

"""
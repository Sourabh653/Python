# Duplicates are not allowed.

mydict = {
    "name":"sourabh",
    "age":20,
    "roll_no":11202598
}

mydict["height"]="5'6"    #To add new item in dictionaries.

mydict.update({"b_year":2002})

thisdict = mydict.copy()

# mydict.popitem()        #Remove last item

# del mydict["name"]

# del mydict      #Delete all dictionary.

# mydict.clear()    #It gives a blank dictionary.

# print(mydict)
# print(type(mydict))
# print(mydict["age"])
# print(len(mydict))

# print(mydict.keys())      #Return all the keys
# print(mydict.get("name"))    
# print(mydict.values())    #Return all the keys

# for x in mydict.keys():
#     print(x)


# for y in mydict.values():
#     print(y)


# for a, b in mydict.items():
#     print(a, b)


print(mydict)
print(thisdict)
# print(mydict.items())   #return all items as a tuple in a list.


list1 = [["Sourabh",2],["Ram",5],["Harry",12],["Sherry",25]]
dict1 = dict(list1)

# print(dict1)
# for item, lollypop in dict1.items():
#     print(item, lollypop)

# for item in dict1:
#     print(item)

# ----------------QUIZ------------------

num = [int, float, "string",3,5,2,7,6,11,22,1,90]
for item in num:
    if str(item).isnumeric() and item>=6:
        
        print(item)
    
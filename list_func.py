# var1 = 6
# var2 = 2
# var3 = int(input())

# if var3 >var2:
#     print("greater")
# elif var3 == var2:
#     print("equal")
# else:
#     print("lesser")

# list1 = [5,3,2,6]

# print(5 in list1)

# if 5 in list1:
#     print("yes")

# print(15 not in list1)

# if 15 not in list1:
#     print("no it's not")

from tkinter.messagebox import QUESTION


#----------------QUIZ-------------

print("Enter your age: ")
age = int(input())
if age>18:
    print("You can drive!") 
elif age==18:
    print("Cant decide about you!")
else:
    print("You can't drive!")

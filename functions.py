# a = 3
# b = 5
# c = sum((a,b))    #built in function
# print(c)


def function1(a,b):
    print("Hello you are in function1", a+b)

def function2(a,b):
    """This is a function which will calculate average of two numebers"""
    average = (a+b)/2
    # print(average)
    return average

v = function2(5,12)
print(v)
print(function2.__doc__)
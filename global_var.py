# l = 10 #Global Variable

# def function1(n):
#     # l = 5 #local variable
#     m = 8 #local variable
#     global l
#     l = l+12
#     print(l,m)
#     print(n, "I have printed")

# function1("This is me")
# print(l)





# x = 47
def harry():
    x = 12
    def sam():
        global x
        x = 88
    print("before calling sam()", x)
    sam()
    print("after calling sam()",x)

harry()
# print(x)
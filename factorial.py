# def print3(str1):
#     print("This is " + str1)

# print3("Sam")

# ---------------------------------------------------------

# def fact_iterative(n):

#     fac = 1
#     for i in range(n):
#         fac = fac * (i+1)
#     return fac

# def fact_recursive(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact_recursive(n-1)

# number = int(input("Enter the number: "))

# print("Factorial using iterative method",fact_iterative(number))
# print("Factorial using recursive method",fact_recursive(number))


#------------------Fibonacci--------------------
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

number = int(input("Enter the number: "))
print(fibonacci(number))

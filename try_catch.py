num1 = input("Enter 1st number: ")
num2 = input("Enter 2nd number: ")

try:
    print("Sum of two numbers is: ",
    int(num1)+int(num2))

except Exception as error:
    print(error)
    
print("This line is very important")
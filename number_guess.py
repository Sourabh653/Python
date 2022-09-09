import random

random_num = random.randint(0,100)

number_of_gusses = 1

print("You can guess only 9 time:")

while(number_of_gusses<=9):
    guess_number = int(input("Guess the number:\n"))

    if guess_number<random_num:
        print("You entered lesses number,  please enter greater number.\n")

    elif guess_number>random_num:
        print("You entered greater number, please enter lesses number.\n")

    else:
        print("You Won!\n")
        print(f"{number_of_gusses} Number of guesses you took to finish.")
        break

    print(f"{9-number_of_gusses} Number of guesses left.")
    
    number_of_gusses = number_of_gusses + 1

if(number_of_gusses>9):
    print(f"The number is {random_num}")
    print("Game Over!!!")
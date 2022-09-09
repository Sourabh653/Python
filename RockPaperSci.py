import random

avail_choice = ["rock","paper","scissors"]
user_choice = input("Enter a choice ('rock','paper','scissors'):- ")
comp_choice = random.choice(avail_choice)
print(f"You chose {user_choice} and computer chose {comp_choice}")

if user_choice == comp_choice:
    print(f"Both select {user_choice}. Game tie!")

elif user_choice == "rock":
    if comp_choice == "paper":
        print("Paper cover the rock. You lose!")
    else:
        print("Rock break the scissor. You win!")

elif user_choice == "paper":
    if comp_choice == "scissors":
        print("Scissor cut the paper. You lose!")
    else:
        print("Paper cover the rock. You win!")

elif user_choice == "scissors":
    if comp_choice == "rock":
        print("Rock break the scissors. You lose!")
    else:
        print("Scissor cut the paper. You win!")
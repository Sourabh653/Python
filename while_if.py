
# i = 0
# while True:
#     if i+1<5:
#         i=i+1
#         continue
#     print(i+1, end=" ")
#     if i==44:
#         break  #Stop the loop
#     i=i+1

# -----------QUIZ--------------

while True:
    inp = int(input("Enter a number: "))
    if inp > 100:
        print("Congratulations!")
        break
    else:
        print("Try again!")
        continue
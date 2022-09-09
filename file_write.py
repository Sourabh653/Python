# f = open("new.txt", "w")
# a = f.write("you are very good in english\n")
# print(a)
# f.close()

# f = open("new2.txt", "a")
# a = f.write("you are very good in english\n")
# print(a)
# f.close()

# Handle read and write both
f = open("new.txt", "r+")
print(f.read())
f.write("Thanq")
f.close()
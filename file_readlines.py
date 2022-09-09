with open("new.txt") as f:
    a = f.readlines()
    print(a)


f = open("new.txt")
print(f.readline())
f.close()
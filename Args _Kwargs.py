# Args   and  Kwargs
# First normal argument, 2nd *args and 3rd **kwargs


# def name(a,b,c,d,e):
#     print(a,b,c,d,e)

# name("Sourabh","Sam","Rohit","Shiv", "Gourav")

def funargs(norme,*args1, **kwargs):
    print(norme,"\n")
    for item in args1:
        print(item,"\n")
    for key, value in kwargs.items():
        print(f"{key} is a {value}\n")

    # print(type(args1))
    # print(args1[1])
    print(args1)

har = ["Sourabh","Sam","Rohit","Shiv", "Gourav","Programmer"]
norme = 34
kw = {"Rohan":"Monitor", "Harry":"programmer"}
funargs(norme, *har, **kw)
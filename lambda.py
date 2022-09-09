# #-------------Lambda Function---------------

# def add(a,b):
#     return a+b
# print(add(12,5))


# minus = lambda x,y: x-y   #LAMBDA FUNCTION

# # def minus(x,y):
# #     return x-y

# print(minus(12,5))

# ----------------------------------------------------
# def a_first(a):
#     return a[1]

a = [[1,3],[5,1],[12,30]]
a.sort(key=lambda x:x[1])
print(a)
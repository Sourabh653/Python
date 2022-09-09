# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list.

counting = [1, 2, 3, 4]
a, b, *c = counting
print(counting)
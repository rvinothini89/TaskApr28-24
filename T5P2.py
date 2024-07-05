data = [10,"vino",22,37,100,999,"vishu",351]
#using type method to find whether the element is string or integer
result = lambda x:type(x)
print(list(map(result,data)))
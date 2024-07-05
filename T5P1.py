#this code filters number based on lambda condition if x > 4 and print the list with 
#numbers greater than 4
data = [10,501,22,37,100,999,87,351]
result = filter(lambda x:x>4,data)
print(list(result))
# This returns the complete list as each element is greater than 4 
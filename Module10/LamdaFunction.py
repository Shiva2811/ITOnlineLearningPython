# lambda arguments: expression
number = lambda x, y:x+y
print(number(3,10))


numbers = [1,2,3,4,5]
squares = list(map(lambda x :x**2, numbers))
print(squares)


#defined function to calculate power of number 
def power(n):
    return lambda a : a**n

check = power(3)
print(check(3))
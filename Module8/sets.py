#Creating set wiht {}
numbers = {1,2,3,4,5,9}

#Creating set wiht set() constructor
set_constructor =set({3,4,5,12})

#adding item in set
numbers.add(7)

#removing item from set
numbers.remove(1)

#discarding item form set 
numbers.discard(2)


print(set_constructor)
print(numbers)


#Checking if item is present in a set 
if 7 in numbers:
    print("7 is available in number set.")
else:
    print("7 is not available in number set.")

#using "union" operation in sets
set3 = numbers.union(set_constructor)
print("set3 :: ", set3)

#using intersection in sets
set3 = numbers.intersection(set_constructor)
print(set3)

#using difference in sets
set3 = numbers.difference(set_constructor)
print(set3)

#using semitrical difference 
set3 = numbers.symmetric_difference(set_constructor)
print(set3)

#using pop finction wiht set3
print(numbers.pop())
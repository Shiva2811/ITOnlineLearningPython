children_age = 1,2,3,8,4,5,2,4,5,2,6,4,2

# tuple slicing
print(children_age[1:2]) 

#count function with tuple is to count the same items in single tuple
print(children_age.count(2)) 

#".index" is to check the index of an item in tuple
print(children_age.index(3))

#a function with tuple
def coordinates():
    return(3,4)
x,y=coordinates()
print(x, " ==== ", y)
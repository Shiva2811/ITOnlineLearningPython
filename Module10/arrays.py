 #list 
list = [1,2,3,4,5,6]

#arrays 
from array import array
import numpy as np

myarray = array('i',[1,2,3,4,5,6])

myarray2 = np.array([1,2,3,4,5])
myarray3 = np.array([3,2,6,7,8])

result = myarray2+myarray3
print(result)

myarray4= np.array([[1,2,3,4],[5,4,3,2]])
print(myarray4)

sortArray = np.sort(myarray3)
print(sortArray)

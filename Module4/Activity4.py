import random
#assigning random number to veriable 
random_number = random.randint(1,100)
#printing random number and its type
print(random_number)
print(type(random_number))

#multi-word variable naming convention with single and double qoutes for string litrals
firstName='Shiva'
LastName="Mahajan"
Full_Name= '''Shiva Mahajan'''

#random number conversion
float_random = float(random_number)
complex_random= complex(random_number)

print("Float conversion of random number :: ",float_random)
print("Type of float_random  :: ",type(float_random))

print("Complex conversion of random number :: ",complex_random)
print("Type of complex_random  :: ",type(complex_random))
firstName = input("Enter your first name :: ")
lastName = input("Enter your last name :: ")
age = input("Enter your age :: ")
city = input("Enter your city :: ")
occupation = input("Enter your occupation :: ")
# Concatenate first and last name
fullName =  firstName.capitalize()+" "+lastName.capitalize()
# Choose "a" or "an" based on the first letter of occupation
article = "an" if occupation[0].lower() in "aeiou" else "a"
#Create profile discription using string formatting
profile_desc = f"{fullName} is {age} years old, lives in {city.capitalize()}, and works as {article} {occupation.capitalize()}."

#add esacpe characters to include quatation marks and a new line
profile_info = "\"Profile Information:\"\n" +profile_desc

#use string method to modify full name and discription
modified_name = fullName.upper()
modified_desc = profile_info

#Display user profile
print("===== User Profile =====")
print(modified_name)
print(modified_desc)
print("========================")
#Creating a string
string = input("Enter a string of your choice :: ")
option = int(input('''Choose one option in between 1 to 5
      1. Converting string to upper case.
      2. Converting string to lower case.
      3. Slicing string from a start index to end index.
      4. Calculate the length of the string.
      5. Loop through each character in the string and display it on a new line.'''))
if option == 1:
    #Converting string to upper case
    print(string.upper())
elif option==2:
    #converting string to lower case
    print(string.lower())
elif option==3:
    #Slicing string from a start index to an end index
    print(string[:])
elif option==4:
    #Calculate the length of the string
    print(len(string))
elif option==5:
    #Loop through each character in the string and display it on a new line
    for x in string:
        print(x)
else:
    print("Choose option in between 1 to 5.")
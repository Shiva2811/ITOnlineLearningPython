#function is defined by "def 'function_name'(arg)"

def greet(name, age, email):
    print(f'''Hello {name}
Your email is {email} and age is {age}''')

name = input("enter your name :: ")
email = input("enter email :: ")
age = input("Enter age :: ")
greet(name, age, email)
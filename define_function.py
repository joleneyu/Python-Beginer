# define addition function
def addition(a, b):
    return a+b

def greeting(name):
    print("Hello", name)

# Main programme
user_name = input("Enter your name:\n")
greeting(user_name)

num1 = float(input("Enter the first number:\n"))
num2 = float(input("Enter another number:\n"))
sum = addition(num1, num2)
print("Result is", sum)


# Day 6 - Functions Practice

def greet():
    print("Hello!")
    print("Welcome to Day 6 of the 100 Days of Python challenge.")
    print("Let's learn about functions!")

greet()


# Function with parameters
def greet_user(name):
    print(f"Hello {name}")
    print("Nice to meet you!")

greet_user("Aryan")


# Function with return value
def add_numbers(a, b):
    return a + b

result = add_numbers(10, 5)
print("The sum is:", result)
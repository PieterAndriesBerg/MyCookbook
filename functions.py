def greet_user():
    """Generic greeting for users"""
    print("Hello ")
    print("Welcome")


def greet_user_by_name(name="user", greeting="Hello"):
    """Customized greeting"""
    print(greeting + ", " + name)


def cube(base_number):
    cubed_value = base_number * base_number * base_number
    return cubed_value


greet_user()
greet_user_by_name(input("What is your name? "))
greet_user_by_name()
greet_user_by_name("Pieter-Andries", "Welcome")
greet_user_by_name(greeting="Welcome", name="Pieter-Andries")
eleven_cubed = cube(11)
print(eleven_cubed)

"""An object has two characteristics:
    -attributes
    -behavior

 example:
 Parrot is an object
   - name, age, color are attributes
   - singing, dancing are behavior

 In Python the concept of OOP follows the following basic principles:
   - Inheritance: A process of using details from a new class without modifiying existing class.
   - Encapsulation: Hiding the private details of a class from other objects.
   - Polymorphism: A concept of using common operation in different ways for different data input."""


class Parrot:
    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def sing(self, song):
        return f"{self.name} sings {song}"

    def dance(self):
        return f"{self.name} is now dancing"


# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print(f"Blu is a {blu.species}")
print(f"Woo is also a {woo.species}")

# access the instance attributes
print(f"{blu.name} is {blu.age} years old.")
print(f"{woo.name} is {woo.age} years old.")

# call our instance methods
print(blu.sing("'Happy'"))
print(blu.dance())

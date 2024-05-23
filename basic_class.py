class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

# Usage
my_dog = Dog("Rex", 2)
print(my_dog.bark())  # Output: Rex says woof!
print(f"My dog is {my_dog.age} years old.")  # Output: My dog is 2 years old

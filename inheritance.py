class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"

# Usage
dog = Dog("Rex")
cat = Cat("Whiskers")
print(dog.speak())  # Output: Rex says woof!
print(cat.speak())  # Output: Whiskers says meow!

class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # Protected attribute

    def display(self):
        return f"Name: {self.name}, Age: {self._age}"

# Usage
person = Person("Alice", 30)
print(person.display())  # Output: Name: Alice, Age: 30

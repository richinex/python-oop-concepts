class Bird:
    def fly(self):
        return "Birds can fly"

class Penguin(Bird):
    def fly(self):
        return "Penguins cannot fly"

# Usage
bird = Bird()
penguin = Penguin()
print(bird.fly())  # Output: Birds can fly
print(penguin.fly())  # Output: Penguins cannot fly

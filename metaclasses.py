class Meta(type):
    def __new__(cls, name, bases, attrs):
        attrs['class_name'] = name
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=Meta):
    pass

# Usage
print(MyClass.class_name)  # Output: MyClass

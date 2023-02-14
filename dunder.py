class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False
    
    def __bool__(self):
        return self.age >= 18

if __name__ == '__main__':
    # Using the custom data structure
    p1 = Person("Alice", 25)
    p2 = Person("Bob", 30)
    p3 = Person("Alice", 25)

    print(p1 == p2)  # False
    print(p1 == p3)  # True

    if p1:
        print("p1 is an adult")
    else:
        print("p1 is not an adult")

# Lab 42: Pythonisms

This repository demonstrates examples of the more advanced Python functionality of iterators, generators, decorators, and dunder methods.

## Example Demonstrating Iterators/Generators on a Custom Collection

* Suppose we have a custom collection of words called WordCollection and we want to use it in a for loop and a list comprehension. We can make it iterable by implementing the `__iter__()` and `__next__()` methods and using the yield keyword in the latter.

```py
class WordCollection:
    def __init__(self):
        self.words = ['apple', 'banana', 'cherry', 'date']
    
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index < len(self.words):
            word = self.words[self.index]
            self.index += 1
            return word
        else:
            raise StopIteration

# Using the WordCollection in a for loop
wc = WordCollection()
for word in wc:
    print(word)

# Using the WordCollection in a list comprehension
wc = WordCollection()
words_starting_with_c = [word for word in wc if word.startswith('c')]
print(words_starting_with_c)
```

## Example Demonstrating a Decorator that Adds Behavior to a Function

* We can create a decorator to calculate the time spent in a function by wrapping it in a function that uses the time module to measure the execution time.

```py
import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken: {end_time - start_time:.5f} seconds")
        return result
    return wrapper

# Using the decorator to time a function
@time_it
def slow_function():
    time.sleep(2)

slow_function()
```

## Example Demonstrating the Use of Dunder Methods to Make Custom Data Structures More Elegant

* We can use the `__eq__()` method to define how two instances of a custom data structure should be considered equal. We can also use the `__bool__()` method to define whether an instance should be considered truthy or falsy.

```py
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
```

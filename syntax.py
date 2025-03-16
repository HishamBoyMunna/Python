print("Hello, World!")  # Output: Hello, World!

# This is a single-line comment
"""
This is a multi-line comment
"""

name = "Alice"  # String
age = 25        # Integer
height = 5.7    # Float
is_student = True  # Boolean

print(type(name))  # Output: <class 'str'>  #typechecking
num = "10"
num = int(num)  # Convert string to integer  #typecasting

#Arithmetic
x = 10
y = 3
print(x + y)  # Addition (13)
print(x - y)  # Subtraction (7)
print(x * y)  # Multiplication (30)
print(x / y)  # Division (3.33)
print(x // y)  # Floor Division (3)
print(x % y)  # Modulus (1)
print(x ** y)  # Exponentiation (1000)
#Comparison
a, b = 5, 10
print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
# Logical operators
print(a > 2 and b > 5)  # True
print(a > 2 or b < 5)   # True
print(not(a > 2))       # False

#control flow
num = 10
if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

#loops
#for
for i in range(5):  # range(0, 5) -> 0 to 4
    print(i)
#while
x = 0
while x < 5:
    print(x)
    x += 1
#loop control
for i in range(10):
    if i == 5:
        break  # Exit loop when i is 5
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)

#data structures
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # apple
fruits.append("orange")
fruits.remove("banana")
print(fruits)  # ['apple', 'cherry', 'orange']
#list comprehension
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

#tuples-immutable,ordered
coordinates = (3, 4)
print(coordinates[0])  # 3
#set-unordered,unique values
unique_numbers = {1, 2, 3, 3, 4}
unique_numbers.add(5)
print(unique_numbers)  # {1, 2, 3, 4, 5}
#dictionaries-key value pairs
person = {"name": "Alice", "age": 25}
print(person["name"])  # Alice
person["age"] = 26
print(person)  # {'name': 'Alice', 'age': 26}

#functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
#lambda
square = lambda x: x * x
print(square(4))  # 16

#import module
import math
print(math.sqrt(16))  # 4.0
#create module
def add(x, y):  #mymodule.py
    return x + y
#import and use
import mymodule
print(mymodule.add(3, 5))  # 8

#class & objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name}"

p = Person("Alice", 25)
print(p.greet())  # Hi, I'm Alice
#inheritance
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

d = Dog()
print(d.speak())  # Woof!

#exception handling
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution completed")

#file handling
# Writing to a file
with open("file.txt", "w") as f:
    f.write("Hello, world!")

# Reading from a file
with open("file.txt", "r") as f:
    content = f.read()
    print(content)

#generator
def count_up(n):
    for i in range(n):
        yield i

gen = count_up(5)
print(next(gen))  # 0
print(next(gen))  # 1

#decorator
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()

#multithreading
import threading

def print_numbers():
    for i in range(5):
        print(i)

t = threading.Thread(target=print_numbers)
t.start()
t.join()

#web scraping
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.title.text)











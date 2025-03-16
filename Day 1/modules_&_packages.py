#Creating a module
# mymodule.py
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

PI = 3.14159
#example.py
import mymodule
print(mymodule.greet("Bob"))
from mymodule import greet, add  #specific
print(greet("Charlie"))
print(add(2, 3))
from mymodule import *  #all
print(greet("David"))
import mymodule as mm  #alias
print(mm.greet("Eve"))

# mymodule.py
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("Main User"))  # This will run only if executed directly

#packages
'''
mypackage/
│── __init__.py  (Makes this a package)
│── module1.py   (First module)
│── module2.py   (Second module)
'''
# module1.py
def hello():
    return "Hello from module1!"
# module2.py
def square(n):
    return n * n
#example.py
import mypackage.module1
import mypackage.module2

print(mypackage.module1.hello())  # Output: Hello from module1!
print(mypackage.module2.square(4)) # Output: 16

#to make importing easier
# __init__.py
from .module1 import hello
from .module2 import square
#example.py
import mypackage

print(mypackage.hello())      # Output: Hello from module1!
print(mypackage.square(5))    # Output: 25

#Installing and Using Your Package
#setup.py
from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.1",
    packages=find_packages(),  # Automatically finds package directories
)
'''
pip install .
'''

#absolute import
import mypackage.module1
print(mypackage.module1.hello())
#relative import
# Inside another module in the package
from .module1 import hello

#dynamic import
import importlib

module_name = "mypackage.module1"
module = importlib.import_module(module_name)

print(module.hello())  # Output: Hello from module1!
#check availability 
import pkgutil

package = mypackage
modules = [name for _, name, _ in pkgutil.iter_modules(package.__path__)]
print(modules)  # Output: ['module1', 'module2']

#making executable
# mymodule.py
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("Direct Execution"))  # Runs only when executed as a script
'''
python mymodule.py
'''









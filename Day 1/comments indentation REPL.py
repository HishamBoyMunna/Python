# 1.comments in python
  
#single line
# This is a single-line comment
print("Hello, World!")  # This is an inline comment

#multi_line(doc string)
"""
This is a multi-line comment.
It can span multiple lines.
"""
print("Python is fun!")

OR

'''
Another way to write
multi-line comments.
'''
print("Let's learn Python!")

#docstring
def add(a, b):
    """This function adds two numbers and returns the result."""
    return a + b
help(add)
print(add.__doc__)

# 2.indentation in python
if True:
    print("This is correctly indented")  # 4 spaces or 1 tab indentation
    print("Python enforces indentation")

'''
Indentation Best Practices
	•	Use 4 spaces per indentation level (PEP 8 standard).
	•	Don’t mix tabs and spaces (it will cause errors).
	•	Every block inside an if, for, while, def, and class must be indented.
'''
def greet(name):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, Stranger!")

#3.REPL
'''
REPL stands for:
	•	R → Read (takes user input)
	•	E → Evaluate (processes the input)
	•	P → Print (displays the result)
	•	L → Loop (waits for the next command)

It allows you to run Python commands interactively without writing a full script.

open terminal
python3

exit()
'''

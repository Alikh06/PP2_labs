#Python HOME
print("Hello World!")

#Python Introduction
print("Hello World!")

#Python Get started
print("Hello, World!")

#Python Syntax
if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 

#Python Comments
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

#Python Variables
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = 5
y = "Nikita"
print(x, y)

x = "awesome"
def myfunc():
  x = "fantastic"
  print("Professor is " + x)

myfunc()
print("Professor is " + x)

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

x = "awesome"
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#Python Data Types
x = memoryview(bytes(5))

print(x)

print(type(x)) 

#Python Numbers
import random

print(random.randrange(1, 10))

#Python Casting
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

#Python Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

txt = "The best things in life are free!"
print("free" in txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)


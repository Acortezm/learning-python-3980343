# LinkedIn Learning Python course by Joe Marini
# Working with modules of code
import math

print("the square root of 16 is", math.sqrt(16))

# import the math module, which contains features for working with mathematics
from math import pi
print("pi is", pi)

# import a specific part of the module so you can refer to it more easily
import random as r 
print(r.randint(100, 200))

# import a module and give it a different name


# the math module contains lots of pre-built functions


# in addition to functions, some modules contain useful constants 


# Generate a random number between 100 and 200


# try some of the math functions for yourself here:

# Use the 3rd party tabulate module to print tabulated data:
from tabulate import tabulate
# Sample data
data = [
  ["Product", "Price", "Stock"],
  ["Laptop", 999.99, 45],
  ["Mouse", 24.99, 128],
  ["Keyboard", 59.99, 89]
]
print(tabulate(data, headers="firstrow", tablefmt="double_outline"))

# Create a formatted table

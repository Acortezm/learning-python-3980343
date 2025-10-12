#
# Example file for working with os.path module
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path 
import time
from datetime import datetime

# Print the name of the OS
print(os.name)

# Check for item existence and type
print("Item exist:", path.exists("textfile.txt"))
print("Item is a file:", path.isfile("textfile.txt"))
print("Item is a dir:", path.isdir("textfile.txt"))

# Work with file paths
print("Item's path:", path.realpath("textfile.txt"))
print("Item's path and name:", path.split(path.realpath("textfile.txt")))

# Get the modification time

t = time.ctime(path.getatime("textfile.txt"))
print(t)
print(datetime.fromtimestamp(path.getatime("textfile.txt")))

# Calculate how long ago the item was modified

td =  datetime.now() - datetime.fromtimestamp(path.getatime("textfile.txt"))
print(td)
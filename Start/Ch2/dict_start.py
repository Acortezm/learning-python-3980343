# LinkedIn Learning Python course by Joe Marini
# Example file for complex types


# Dictionary: a key-value data structure
mydic = {
  "One" : 1, 
  1.2 : [1, 2], 
  3: "three"
}

print(mydic)

# dictionaries are accessed via keys
print(mydic["One"]) #!= mydic["one"]

# you can also set dictionary data by creating a new key
mydic["seven"] = 7
print(mydic)

# Trying to access a nonexistent key will produce an error
# To avoid this, you can use the "in" operator to see if a key exists
print("two" in mydic)

# You can retrieve all of the keys and values from a dictionary
print(mydic.keys())
print(mydic.values())

# You can also iterate over all the items in a dictionary
for key, val in mydic.items(): 
  print(key, val) #it will pring a tuble

  
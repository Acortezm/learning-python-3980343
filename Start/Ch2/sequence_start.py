# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
mylist = [1, "two", 3.2, False]
print(len(mylist))

# to access a member of a sequence type, use []
print(mylist[3])
print(mylist[-1])
mylist[0] = 10
print(mylist)

# add a list to another list
another_list = [1,2,3]
mylist = mylist + another_list
print(mylist)

# use slices to get parts of a sequence
print(mylist[1:4:2]) #start, end, steps

# you can use slices to reverse a sequence
print(mylist[::-1])

# Tuples are like lists, but they are immutable
mytuple = (0, 1, 2, "three")

# Sets are also sequences, but they contain unique values
myset = {1, 2, 3,2, 4, "hey"}
print(myset) #any repeated item will be filter out.

# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error

# Test for membership
print(1 in mylist) #in checks in the valu exist in the list, tuple, sets.
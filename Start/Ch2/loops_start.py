# LinkedIn Learning Python course by Joe Marini
# Example file for working with loops


x = 0

# define a while loop
# while x < 5:
#   print(x)
#   x = x + 1

# # define a for loop
days = ["Mon", "Tue","Wed", "Thu", "Fri", "Sat", "Sun" ]
# for d in days: 
#   print(d)

# use a for loop over a collection


# use the break and continue statements
for d in days: 
  if (d == "Wed"):
    break #stops the loop
  print(d)

for d in days: 
  if (d == "Thu"):
    continue #skip
  print (d)
# using the enumerate() function to get an index and an item
for i, d in enumerate(days):
  print(i, d)
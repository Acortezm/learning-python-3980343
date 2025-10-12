# LinkedIn Learning Python course by Joe Marini
# Example file for working with conditional statements


x, y = 1000, 100

# conditional flow uses if, elif, else
if x < y: 
  print("x is less than y")
elif x == y:
  print("x is the same a y")
else: 
  print("y is greater than x")

# conditional statements let you use "a if C else b"

result = "x is less than y" if (x > y) else "y is less than x"
print(result)
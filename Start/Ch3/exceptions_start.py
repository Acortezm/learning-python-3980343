# # LinkedIn Learning Python course by Joe Marini
# # Example file for working with Exceptions
# #

# # Errors can happen in programs, and we need a clean way to handle them
# # This code will cause an error because you can't divide by zero:
# # x = 10 / 0
# # Exceptions provide a way of catching errors and then handling them in 
# # a separate section of the code to group them together
# try: 
#   x = 10 / 0 
# except: 
#   print("well that didn't work")

# # You can also catch specific exceptions
# try:
#   answer = input("What should I divide 10 by?")
#   num = int(answer)
#   print(10/num)
# except ZeroDivisionError as e: 
#   print("You can't divide by zero")
# except ValueError as e: 
#   print("You didn't give me a valid number")
#   print(e)
# finally: 
#   print("Finally always run")


# Python code​​​​​​‌‌‌​​‌‌​​​​‌​​‌‌​​‌‌‌‌‌​​ below
# Use print("messages...") to debug your solution.

#code challenge below
import string

show_expected_result = False
show_hints = False

def is_palindrome(teststr):
    # Your code goes here.
    cleanStr =  teststr.translate(str.maketrans('', '', string.punctuation))
    cleanStr = cleanStr.replace(" ", "")
    cleanStr = cleanStr.lower()
    
    newstr = ""
    for i in range(len(cleanStr) ,0,-1):
        newstr += cleanStr[i - 1]   

    if newstr == cleanStr:
        return True
    else:
        return False


print(is_palindrome("Madam, I'm Adam."))
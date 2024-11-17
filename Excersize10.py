Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# ask the user to enter a number
>>> number = int(input("Enter a number: "))
Enter a number: 7
# check if the entered number is even or odd
>>> if(number % 2) == 0:
...     print("{0} is even number".format(number))
... else:
...     print("{0} is odd number".format(number))
... 
...     
7 is odd number

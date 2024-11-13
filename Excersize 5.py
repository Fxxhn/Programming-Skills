Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> days_in_month = {
...     1: 31,  # January
...     2: 28,  # February
...     3: 31,  # March
...     4: 30,  # April
...     5: 31,  # May
...     6: 30,  # June
...     7: 31,  # July
...     8: 31,  # August
...     9: 30,  # September
...     10: 31, # October
...     11: 30, # November
...     12: 31  # December
... }
>>> month_number = int(input("Enter the month number (1-12): "))
Enter the month number (1-12): 12
>>> if month_number in days_in_month:
...     print(f"The number of days in month {month_number} is {days_in_month[month_number]}.")
... else:
...     print("Invalid month number. Please enter a number between 1 and 12.")
... 
...     
The number of days in month 12 is 31.
>>> month_number = int(input("Enter the month number (1-12): "))
Enter the month number (1-12): 4
>>> if month_number in days_in_month:
...     print(f"The number of days in month {month_number} is {days_in_month[month_number]}.")
... else:
...     print("Invalid month number. Please enter a number between 1 and 12.")
... 
...     
The number of days in month 4 is 30.

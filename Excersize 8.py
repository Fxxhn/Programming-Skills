Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
... 
>>> search_term = input("Enter the name you want to search for: ")
... 
Enter the name you want to search for: Sam
>>> 
>>> if search_term in names:
...     print(f"{search_term} was found in the list.")
... else:
...     print(f"{search_term} was not found in the list.")
... 
...     
Sam was found in the list.
>>> 
>>> search_term = input("Enter the name you want to search for: ")
Enter the name you want to search for: Zac

>>> if search_term in names:
...     print(f"{search_term} was found in the list.")
... else:
...     print(f"{search_term} was not found in the list.")
... 
...     
Zac was found in the list.

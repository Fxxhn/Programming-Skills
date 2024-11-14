Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> correct_password = "12345"
... 
>>> max_attempts = 5
>>> attempts = 0
>>> while attempts < max_attempts:
...     password = input("Enter the password: ")
... 
...     
Enter the password:  if password == correct_password:
...         print("Access granted.")
...         break
...     else:
...         attempts += 1
...         remaining_attempts = max_attempts - attempts
...         print(f"Incorrect password. You have {remaining_attempts} attempts left.")
Enter the password: Enter the password: Enter the password: Enter the password: Enter the password: Enter the password: Enter the password: if attempts == max_attempts:
...             print("Maximum attempts reached. Authorities have been alerted.")
Enter the password: Enter the password: 12345
Enter the password: 12345
Enter the password: 12345
Enter the password: 12345
Enter the password: 123456
Enter the password: 222
Enter the password: 
Enter the password: 
Enter the password: 
Enter the password: 2
Enter the password: 
Enter the password: 
Enter the password: 
Enter the password: 
Enter the password: 
Enter the password: 2133

Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
questions = {
    "France": "Paris",
    "Germany": "Berlin",
...     "Italy": "Rome",
...     "Spain": "Madrid",
...     "Portugal": "Lisbon",
...     "Netherlands": "Amsterdam",
...     "Belgium": "Brussels",
...     "Switzerland": "Bern",
...     "Austria": "Vienna",
...     "Norway": "Oslo"
... }
... 
>>> 
>>> score = 0
>>> for country, capital in questions.items():
...     answer = input(f"What is the capital of {country}? ").strip().lower()
... 
...     
What is the capital of France? 
What is the capital of Germany? 
What is the capital of Italy? 
What is the capital of Spain? 
What is the capital of Portugal? 
What is the capital of Netherlands? 
What is the capital of Belgium? 
What is the capital of Switzerland? 
What is the capital of Austria? 
What is the capital of Norway? 
>>> if answer == capital.lower():
...         print("Correct!")
...         score += 1
... 
...         
>>> if answer == capital.lower():
...         print("Correct!")
...         score += 1
... 
...         
>>> print(f"\nQuiz completed! Your score: {score}/{len(questions)}")

Quiz completed! Your score: 0/10

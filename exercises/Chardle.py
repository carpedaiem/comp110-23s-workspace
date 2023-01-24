"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730374002"

word: str = input("Enter a 5-character word:")
total: int = 0

if len(word) == 5:
    """filler material because it somehow wont work"""
else: 
    print("Error: Word must contain 5 characters")
    exit()

character: str = input("Enter a single character:")

if len(character) == 1:
    print("Searching for " + character + " in " + word)
else: 
    print("Error: Character must be a single character.")
    exit()

if word[0] == character:
    print(character + " found at index 0")
    total = total + 1
else: 
    total = total
if word[1] == character:
    print(character + " found at index 1")
    total = total + 1
else: 
    total = total
if word[2] == character:
    print(character + " found at index 2")
    total = total + 1
else: 
    total = total   
if word[3] == character:
    print(character + " found at index 3")
    total = total + 1
else: 
    total = total
if word[4] == character:
    print(character + " found at index 4")
    total = total + 1
else: 
    total = total

if total >= 2:
    print(str(total) + " instances of " + character + " found in " + word)
else: 
    if total == 1:
        print(str(total) + " instance of " + character + " found in " + word)
    else:
        print("No instances of " + character + " found in " + word)
"""EX 02 - One shot Wordle!"""
__author__ = "730374002"

secret = "python"

""" Length of secret word"""
length = len(secret)

guess: str = input("What is your " + str(length) + "-letter guess? ")

while len(guess) != length:
    new_guess: str = input("That was not " + str(length) + " letters! Try again: ")
    guess = new_guess

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

letter = 0
boxes = ""

while letter < length:
    guess_check = guess[letter]
    secret_check = secret[letter]
    if ord(guess_check) == ord(secret_check):
        boxes = boxes + GREEN_BOX
    else: 
        yellow_find = False
        yellow_length = 0
        while yellow_length < length:
            if ord(guess_check) == ord(secret[yellow_length]):
                yellow_find = True
            yellow_length = yellow_length + 1
        if yellow_find is True:
            boxes = boxes + YELLOW_BOX
        else: 
            boxes = boxes + WHITE_BOX
    letter = letter + 1

print(boxes)
"""Correction statement"""
if len(guess) == length:
    if str(guess) == str(secret):
        print("Woo! You got it!")
    else:
        print("Not quite. Play again soon!")
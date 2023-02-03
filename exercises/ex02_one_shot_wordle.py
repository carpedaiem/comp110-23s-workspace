"""EX 02 - One shot Wordle!"""
__author__ = "730374002"

secret = "python"
length = len(secret)

guess: str = input("What is your " + str(length) + "-letter guess? ")

"""Checking whether the length of the guess is the same as the secret word"""
while len(guess) != length:
    new_guess: str = input("That was not " + str(length) + " letters! Try again: ")
    guess = new_guess

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

position = 0
boxes = ""

"""Loop for checking letters and their positions"""
while position < length:
    guess_check = guess[position]
    secret_check = secret[position]
    if ord(guess_check) == ord(secret_check):
        boxes = boxes + GREEN_BOX
    else: 
        yellow_find = False
        yellow_position = 0
        while yellow_position < length:
            if ord(guess_check) == ord(secret[yellow_position]):
                yellow_find = True
            yellow_position = yellow_position + 1
        if yellow_find is True:
            boxes = boxes + YELLOW_BOX
        else: 
            boxes = boxes + WHITE_BOX
    position = position + 1
print(boxes)

"""Correction statement"""
if len(guess) == length:
    if str(guess) == str(secret):
        print("Woo! You got it!")
    else:
        print("Not quite. Play again soon!")
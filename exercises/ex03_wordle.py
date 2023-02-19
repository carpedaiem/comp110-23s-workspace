"""Wow, A Structured Wordle!"""
__author__ = "730374002"

"""defining contains_char function"""
def contains_char(word: str, needle: str) -> bool:
    assert len(needle) == 1
    position = 0
    """while loop to search indices for same character"""
    while position < len(word):
        result = False
        if word[position] == needle:
            result = True
            return result
        else:
            if position == (len(word) - 1):
                return result
            else:
                position = position + 1

"""emojified variables"""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

"""Defining emojified function"""
def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret)
    position = 0
    boxes = ""
    while position < len(secret):
        """Checks for green box criteria"""
        if ord(guess[position]) == ord(secret[position]):
            boxes = boxes + GREEN_BOX
        else:
            """Checks for yellow box criteria"""
            yellow_check = contains_char(secret, guess[position])
            if yellow_check is True:
                boxes = boxes + YELLOW_BOX
            else:
                boxes = boxes + WHITE_BOX
        position = position + 1
    return boxes

"""defining input_guess function"""
def input_guess(guess_length: int) -> str:
    guess: str = input(f"Enter a {guess_length} character word: ")
    """For wrong input lengths"""
    while len(guess) != guess_length:
        new_guess: str = input(f"That wasn't {guess_length} chars! Try again: ")
        guess = new_guess
    return guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn = 1
    secret = "codes"
    win = False
    """while loop for a max 6-turn game"""
    while turn <= 6 and win == False:
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(len(secret))
        game = emojified(guess, secret)
        print(game)
        if guess != secret:
            win = False
            if turn == 6:
                print("X/6 - Sorry, try again tomorrow!")
        else:
            win = True
            print(f"You won in {turn}/6 turns!")
        turn = turn + 1

"""Calling the main function"""
if __name__ == "__main__":
    main()

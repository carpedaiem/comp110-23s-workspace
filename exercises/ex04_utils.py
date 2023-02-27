"""Utility Functions."""
___author___ = "730374002"


def all(list: list[int], number: int) -> bool:
    """Function tests if number is equal to all items on list."""
    match = False
    position = 0
    while match is False:
        if len(list) == 0:
            return match
        if list[position] == number:
            position += 1
            if position == len(list):
                match = True
                return match
        else:
            return match
    return match


def max(input: list[int]) -> int:
    """Function that prints out the largest integer in a list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    counter = len(input)
    while counter != 1:
        if input[0] > input[1]:
            input.pop(1)
        else:
            input.pop(0)
        counter = len(input)
    return input[0]


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Function tests whether two lists are deep equal."""
    position = 0
    deep_equal = False
    if len(list_1) != len(list_2):
        return deep_equal
    elif len(list_1) == 0 and len(list_2) == 0:
        deep_equal = True
        return deep_equal
    while deep_equal is False:
        if list_1[position] == list_2[position]:
            if position == len(list_1) - 1:
                deep_equal = True
                return deep_equal
            position += 1
        else:
            return deep_equal
    return deep_equal
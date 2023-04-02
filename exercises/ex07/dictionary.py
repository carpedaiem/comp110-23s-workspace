"""EX07 - Dictionary Functions."""

__author__ = "730374002"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverts the dictionary."""
    invert: dict[str, str] = {}
    for key in input:
        invert[input[key]] = key
    return invert


def favorite_color(input: dict[str, str]) -> str:
    """Determines which color appears more frequently."""
    favorite: str = ""
    i: int = 0
    element: str = ""
    for elem in input:
        position: int = 0
        element = input[elem]
        for idx in input:
            if input[idx] == element:
                position += 1
            if position > i:
                i = position
                favorite = element
    return favorite


def count(input: list[str]) -> dict[str, int]:
    """Counting the frequencies of each unique index in a list."""
    dictionary: dict[str, int] = {}
    for idx in input:
        if idx in dictionary:
            dictionary[idx] += 1
        else:
            dictionary[idx] = 1
    return dictionary
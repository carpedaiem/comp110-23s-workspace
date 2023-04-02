"""Dictionary Tests."""

__author__ = "730374002"


from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count

"""with pytest.raises(KeyError):
    my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
    invert(my_dictionary)"""


def test_invert_small() -> None:
    """Test small input."""
    assert invert({"Emily": "730374002"}) == {"730374002": "Emily"}


def test_invert_big() -> None:
    """Tests multiple inputs."""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_uppercase() -> None:
    """Tests if the function can differentiate upper and lowercase."""
    assert invert({"EMILY": "emily"}) == {"emily": "EMILY"}


def test_favorite_color_small() -> None:
    """Tests small inputs."""
    assert favorite_color({"Emily": "purple"}) == "purple"


def test_favorite_color_big() -> None:
    """Tests multiple inputs."""
    assert favorite_color({"Emily": "purple", "One": "blue", "Your": "purple"}) == "purple"


def test_favorite_color_tie() -> None:
    """Tests ties between colors."""
    assert favorite_color({"Emily": "purple", "One": "blue", "Your": "green"}) == "purple"


def test_count_small() -> None:
    """Tests small inputs."""
    assert count(["Emily"]) == {"Emily": 1}


def test_count_big() -> None:
    """Tests multiple inputs."""
    assert count(["Emily", "Emily", "Sophia"]) == {"Emily": 2, "Sophia": 1}


def test_count_case() -> None:
    """Upper and lower case should be differentiated."""
    assert count(["Emily", "emily", "Sophia"]) == {"Emily": 1, "emily": 1, "Sophia": 1}
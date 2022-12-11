from calculator import count_people


def test():
    assert count_people(50, 20, 3, True) == 440


def test_1():
    assert count_people(50, 20, 3, False) == 200

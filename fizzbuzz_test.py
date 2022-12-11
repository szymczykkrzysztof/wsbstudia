from fizzbuzz import fizzbuzz


def test_0():
    assert fizzbuzz(1) == 1


def test_1():
    assert fizzbuzz(3) == "Fizz"


def test_2():
    assert fizzbuzz(5) == "Buzz"


def test_3():
    assert fizzbuzz(15) == "FizzBuzz"


def test_4():
    assert fizzbuzz(10) == "Buzz"


def test_5():
    assert fizzbuzz(0) == 0


def test_6():
    assert fizzbuzz(-2) is None

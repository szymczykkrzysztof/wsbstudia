def fizzbuzz(data):
    number = int(data)
    if number < 0:
        return None
    elif number == 0:
        return 0
    elif number % 5 == 0 and number % 3 == 0:
        return "FizzBuzz"
    elif number % 5 == 0:
        return "Buzz"
    elif number % 3 == 0:
        return "Fizz"
    else:
        return number

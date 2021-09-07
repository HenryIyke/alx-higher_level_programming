#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = random % 10
if last_digit == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, last_digit))
elif number < 0:
    num = number * -1
    n = num % 10
    print("Last digit of -{:d} is -{:d} and "
            "is less than 6 and not 0".format(num, n))
elif number > 0:
    if n < 6:
        print("Last digit of {:d} is {:d} and "
                "is less than 6 and not 0".format(number, n))
else:
    print("Last digit of {:d} is {:d} and "
            "is greater than 5".format(number, n))

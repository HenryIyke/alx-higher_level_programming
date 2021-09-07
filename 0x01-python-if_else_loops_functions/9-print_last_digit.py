#!/usr/bin/python3
def print_last_digit(number):
    """Prints the last digit of a number"""
    ld = number % 10 if number >= 0 else (number * -1) % 10
    print("{:d}".format(ld), end="")
    return ld

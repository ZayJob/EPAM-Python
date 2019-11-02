#!/usr/bin/python3

#Task 4.6
#Implement a decorator call_once which runs a function or method once.

def call_once(func):
    def wrapper(a, b):
        if not wrapper.has_run:
            wrapper.has_run = True
            print(func(a, b))
    wrapper.has_run = False
    return wrapper

@call_once
def sum_of_numbers(a, b):
    return a + b

if __name__ == "__main__":
    sum_of_numbers(13, 42)
    sum_of_numbers(13, 42)
    sum_of_numbers(13, 42)
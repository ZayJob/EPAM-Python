#!/usr/bin/python3

from functools import reduce

#Task 4.5
#Implement a decorator remember_result which remembers last result of function it decorates
#and prints it before next call.

def remember_result(func):
    temp = None
    def wrapper(*args):
        nonlocal temp
        print(f"Current result = '{temp}'")
        temp = func(args)
    return wrapper

@remember_result
def sum_list(args):
    s = reduce(lambda x,y: x + y, list(args))
    print(f"Current result = '{s}'\n")
    return s

if __name__ == "__main__":
    sum_list(1,2,3)
    sum_list(1,2,3,4)
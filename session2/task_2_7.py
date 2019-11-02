#!/usr/bin/python

from functools import reduce

#Task 2.7
#Implement a function foo(List[int]) -> List[int] which, given a list of integers, return a new
#list such that each element at index i of the new list is the product of all the numbers in the
#original array except the one at i .

def foo(array):
    return [(reduce(lambda x, y: x*y,array) // array[i]) for i in range(len(array))]

if __name__ == "__main__":
    print(foo([1, 2, 3, 4, 5]))
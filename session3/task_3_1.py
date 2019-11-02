#!/usr/bin/python

import string
from functools import reduce

#Task 3.1
#Implement a bunch of functions which receive a changeable number of strings and return next
#parameters:
#1. characters that appear in all strings
#2. characters that appear in at least one string
#3. characters that appear at least in two strings
#4. characters of alphabet, that were not used in any string
#Note: use string.ascii_lowercase for list of alphabet letters

def test_1_1(*args):
    return reduce(lambda x,y: x & y, map(set,args))

def test_1_2(*args):
    return set("".join(list(args)))

def test_1_3(*args):
    args = list(args)
    return reduce(lambda x,y: x | y,[set(i).intersection(set("".join(args[:args.index(i)] + args[args.index(i) + 1:]))) for i in args])

def test_1_4(*args):
    return set(string.ascii_lowercase) - set("".join(list(args)))


if __name__ == '__main__':
    print(test_1_1("hello", "world", "python", ))
    print(test_1_2("hello", "world", "python", ))
    print(test_1_3("hello", "world", "python", ))
    print(test_1_4("hello", "world", "python", ))
#!/usr/bin/python

#Task 3.3
#Implement a function, that takes string as an argument and returns a dictionary, that contains
#letters of given string as keys and a number of their occurrence as values.

def count_letters(string):
    return { i:string.count(i) for i in list(string)}

if __name__ == '__main__':
    print(count_letters("stringsample"))
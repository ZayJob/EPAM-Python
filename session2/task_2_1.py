#!/usr/bin/python3

import string

#Task 2.1
#Implement a function which receives a string and replaces all " symbols with ' and vise versa.

def my_replace(s):
    return s.translate(s.maketrans({"\"":"\'","\'":"\""}))

if __name__ == '__main__':
    print(my_replace("sdcsdc\"sdcsdcsdcsdcs\"sdcsd\'csdc"))
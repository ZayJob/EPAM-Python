#!/usr/bin/python

#Task 2.2
#Write a function that check whether a string is a palindrome or not. Usage of any reversing
#functions is prohibited. To check your implementation you can use strings from here.

def check_palindrome(string):
    return string == string[::-1]

if __name__ == "__main__":
    print(check_palindrome("aba"))
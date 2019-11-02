#!/usr/bin/python

#Task 2.6
#Implement a function get_shortest_word(s: str) -> str which returns the longest word in the
#given string. The word can contain any symbols except whitespaces ( , \n , \t and so on). If
#there are multiple longest words in the string with a same length return the word that occures
#first.

def get_shortest_word(string):
    return max(string.split(),key=len)

if __name__ == "__main__":
    print(get_shortest_word("ajveifbv bekjfbvjefvjke cejfv ehf vebfvebfvhebfvjhefbvjefbvjhbefvhjfe"))
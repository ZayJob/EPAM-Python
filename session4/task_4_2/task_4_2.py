#!/usr/bin/python3

from collections import Counter
from functools import reduce

#Task 4.2
#Implement a function which search for most common words in the file. Use
#data/lorem_ipsum.txt file as a example.

def most_common_words(filepath, number_of_words=3):
    with open(filepath, "r") as rf:
        data = rf.read()
        return [i[0] for i in Counter(list(filter(str.isalpha, str.lower(data).split()))).most_common(number_of_words)]

if __name__ == '__main__':
    print(most_common_words("lorem_ipsum.txt"))
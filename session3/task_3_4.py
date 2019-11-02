#!/usr/bin/python

from functools import reduce

#Task 3.4
#Implement a function, that receives changeable number of dictionaries (keys - letters, values -
#numbers) and combines them into one dictionary. Dict values should be summarized in case of
#identical keys

def combine_dicts(*args):
    d = reduce(lambda x,y: {**x,**y}, args)

    for key in d.keys():
        d[key] = 0
        for i in args:
            if key in i.keys():
                d[key] += i[key]
    return d

if __name__ == '__main__':
    print(combine_dicts({'a': 100, 'b': 200},{'a': 200, 'c': 300},{'a': 300, 'd': 100}))
#!/usr/bin/python

import re

#Task 2.3
#Implement a function which works the same as str.split method (without using str.split
#itself, ofcourse).

#Оставлю 2 функции, потому что не знаю,можно ли использовать импорты стандартных библиотек

def my_split(string):
    return re.findall(r'\S+',string)

if __name__ == "__main__":
    print(my_split("1  243234efvnefnvienfvinfiv123123     2342342    234234234"))
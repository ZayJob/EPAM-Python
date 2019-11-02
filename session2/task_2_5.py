#!/usr/bin/python

#Task 2.5
#Implement a function get_digits(num: int) -> Tuple[int] which returns a tuple of a given
#integer's digits.

def get_digits(integer):
    return tuple(map(int,list(str(integer))))

if __name__ == "__main__":
    print(get_digits(834659304650238465))
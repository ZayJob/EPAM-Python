#!/usr/bin/python

#Task 2.8
#Implement a function get_pairs(lst: List) -> List[Tuple] which returns a list of tuples
#containing pairs of elements. Pairs should be formed as in the example. If there is only one
#element in the list return None instead.

def get_pairs(array):
    return [(i,j) for i,j in zip(array,array[1:])] if len(array) > 1 else None

if __name__ == "__main__":
    print(get_pairs([1,2,3,8,9]))
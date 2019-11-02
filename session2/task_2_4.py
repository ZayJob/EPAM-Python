#!/usr/bin/python

#Task 2.4
#Implement a function split_by_index(s: str, indexes: List[int]) -> List[str] which splits
#the s string by indexes specified in indexes . Wrong indexes must be ignored.

def clear_array(array, lenght):    
    temp = 0
    answer = [0,lenght]
    i = 0
    while (i < len(array)):
        if array[i] <= lenght and array[i] >= temp:
            temp = array[i]
            answer.insert(1,array[i])
        i += 1
    return list(sorted(set(answer)))

def my_split_index(string, array):
    array = clear_array(array, len(string) + 1)
    return [string[array[i]:array[i + 1]:] for i in range(len(array) - 1)]

if __name__ == "__main__":
    print(my_split_index("pythoniscool,isn'tit?", [5,8]))
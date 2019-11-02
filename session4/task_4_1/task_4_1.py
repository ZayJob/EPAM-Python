#!/usr/bin/python3

#Task 4.1
#Open file data/unsorted_names.txt in data folder. Sort the names and write them to a new file
#called sorted_names.txt . Each name should start with a new line as in the following example:

def sort_file(rpath, wpath):
    with open(rpath, "r") as rf, open(wpath, "w") as wf:
        read_data = rf.readlines()
        read_data.sort()
        wf.writelines(read_data)

if __name__ == '__main__':
    sort_file("unsorted_names.txt","sorted_names.txt")
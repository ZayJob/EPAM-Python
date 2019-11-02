#!usr/bin/python3

import csv

#Task 4.3
#File data/students.csv stores information about students in CSV format. This file contains the
#student’s names, age and average mark.
#1. Implement a function which receives file path and returns names of top performer students
#2. Implement a function which receives the file path with srudents info and writes CSV student
#information to the new file in descending order of age. Result:

def get_top_performers(file_path, number_of_top_students=5):
    with open(file_path, "r") as rf:
        data = csv.DictReader(rf, delimiter=',')
        select_top_students = sorted(data, key=lambda row: float(row["average mark"]), reverse=True)[:number_of_top_students]
        return [line["student name"] for line in select_top_students]

def move_data(r_path,w_path):
    with open(r_path, "r") as rf,open(w_path, "w", newline='') as wf:
        data = csv.DictReader(rf, delimiter=',')
        sort_data = sorted(data, key=lambda row: int(row["age"]), reverse=True)

        field_names = ['student name', 'age','average mark']
        writer = csv.DictWriter(wf,field_names,delimiter=',')
        
        writer.writeheader()
        writer.writerows(sort_data)

if __name__ == "__main__":
    print(get_top_performers("students.csv"))
    move_data("students.csv","sort_age_students.csv")
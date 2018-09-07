from  __future__ import print_function
import os
import sys

def gradingStudents(grades):
    op = []
    for grade in grades:
        temp = divmod(grade, 5)
        next_multiple = grade + 5- temp[1]
        if (next_multiple - grade < 3) and grade >= 38:
            op.append(next_multiple)
        else:
            op.append(grade)
    return op

if __name__ == '__main__':
    f = open('./input.txt')
    t = int(f.readline().strip())
    grades = []
    for _ in range(t):
        grades_item = int(f.readline().strip())
        grades.append(grades_item)
    result = gradingStudents(grades)
    print('\n'.join(map(str, result)))

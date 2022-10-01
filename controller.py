from tkinter import *

name = []
surname = []
first_number = []
second_number = []
other = []

def col_lines(name_file):
    lines= 0
    with open (name_file, 'r', encoding="utf-8") as file:
        for line in file:
            lines+=1
    return lines

def save_contact(name, surname, first_number, second_number, other):
    lines = col_lines("Numbers.txt")
    if lines == 0:
        id = str(col_lines("Numbers.txt")+1)
        with open ("Numbers.txt", "a", encoding="utf-8") as write:
                write.write(id + '\t')
                write.write(name[0] + '\t')
                write.write(surname[0] + '\t')
                write.write(first_number[0] + '\t')
                write.write(second_number[0] + '\t')
                write.write(other[0] + '\t')
    else:
        id = str(col_lines("Numbers.txt")+1)
        with open ("Numbers.txt", "a", encoding="utf-8") as write:
                write.write('\n' + id + '\t')
                write.write(name[0] + '\t')
                write.write(surname[0] + '\t')
                write.write(first_number[0] + '\t')
                write.write(second_number[0] + '\t')
                write.write(other[0] + '\t')   


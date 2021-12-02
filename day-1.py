from reader.file_reader import *


def value_increased(val):
    increased = 0
    for i in range(len(val) - 1):
        if int(val[i]) < int(val[i + 1]):
            increased += 1
    return increased


def in_place_solution():
    val = read_file("inputs/day-1.txt")
    increased = 0
    count = int(val[0]) + int(val[1]) + int(val[2])
    for i in range(1, len(val) - 2):
        if count < (int(val[i]) + int(val[i + 1]) + int(val[i + 2])):
            increased += 1
            count = int(val[i]) + int(val[i + 1]) + int(val[i + 2])

    print("increased", increased)


def puzzle1():
    val = read_file("inputs/day-1.txt")
    print("increased", value_increased(val))


def puzzle2():
    val = read_file("inputs/day-1.txt")
    count_list = [
        (int(val[i]) + int(val[i + 1]) + int(val[i + 2])) for i in range(len(val) - 2)
    ]
    print("increased", value_increased(count_list))


puzzle1()
puzzle2()

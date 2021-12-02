from reader.file_reader import *


def compute():
    val = read_file("inputs/day-2.txt")
    horizontal = 0
    depth = 0
    down = 0
    up = 0
    aim = 0
    for i in range(len(val)):
        line = val[i].split(" ")
        if line[0] == "forward":
            depth += int(line[1]) * aim
            horizontal += int(line[1])
        if line[0] == "down":
            down += int(line[1])
            aim += int(line[1])
        if line[0] == "up":
            up += int(line[1])
            aim -= int(line[1])
    print("puzzle 1", horizontal * (down - up))
    print("puzzle 2", horizontal * depth)


compute()

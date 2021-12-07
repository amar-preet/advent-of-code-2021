def read():
    with open("inputs/day-6.txt") as f:
        content = f.read().split(",")
        return content


def puzzle(num):
    content = read()
    new_list = []
    n = 0
    while n < num:
        n += 1
        new_list = []
        for i in content:
            if int(i) == 0:
                new_list.append(6)
                new_list.append(8)
            else:
                new_list.append(int(i) - 1)
        content = new_list
    print("new_list", len(content))


puzzle(80)
puzzle(256)

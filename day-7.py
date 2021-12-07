def read():
    with open("inputs/day-7.txt") as f:
        content = f.read().split(",")
        return content


def puzzle1():
    content = read()
    return_list = []

    for i in range(len(content)):
        add_list = [abs(int(content[j]) - int(content[i])) for j in range(len(content))]
        return_list.append(sum(add_list))
    print(min(return_list))


def puzzle2():
    content = read()
    return_list = []
    largest_num = max([int(x) for x in content])
    sum_n = 0
    for k in range(largest_num):
        add_list = []
        for i in content:
            x = abs(int(k) - int(i))
            sum_n = 0
            for n in range(x):
                sum_n += n
            add_list.append(sum_n + x)

        return_list.append(sum(add_list))
    print(min(return_list))


puzzle1()
puzzle2()

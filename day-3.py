def read():
    with open("inputs/day-3.txt") as f:
        content = f.read().split("\n")
        return content


def puzzle1():
    content = read()
    epsilon_rate = ""
    gamma_rate = ""
    for i in range(len(content[0])):
        ones = 0
        zeroes = 0
        column = [content[i] for content in content]
        for val in column:
            if val == "1":
                ones += 1
            else:
                zeroes += 1
        if ones > zeroes:
            gamma_rate = gamma_rate + "1"
        else:
            gamma_rate = gamma_rate + "0"
    for gamma in gamma_rate:
        if gamma == "0":
            epsilon_rate = epsilon_rate + "1"
        else:
            epsilon_rate = epsilon_rate + "0"
    print("puzzle1", str(int(gamma_rate, 2) * int(epsilon_rate, 2)))


def oxygen_co2_generator(one: str, zero: str):
    content = read()
    needed_list = []

    for i in range(len(content[0])):
        if len(content) != 1:
            needed_list = []
            ones = 0
            zeroes = 0
            column = [content[i] for content in content]
            for val in column:
                if val == "1":
                    ones += 1
                else:
                    zeroes += 1
            if ones >= zeroes:
                for item in content:
                    if item[i].startswith(one):
                        if item not in needed_list:
                            needed_list.append(item)
            else:
                for item in content:
                    if item[i].startswith(zero):
                        if item not in needed_list:
                            needed_list.append(item)
            content = needed_list
            continue

    return content


puzzle1()
print(
    "puzzle2",
    str(
        int(oxygen_co2_generator("1", "0")[0], 2)
        * int(oxygen_co2_generator("0", "1")[0], 2)
    ),
)

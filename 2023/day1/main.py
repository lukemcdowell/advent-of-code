def part_one():
    total = 0

    with open("input.txt", "r") as file:

        for line in file:
            num_1 = None
            num_2 = None

            for i in line:
                if num_1:
                    break

                if i.isnumeric():
                    num_1 = i

            for j in reversed(line):
                if num_2:
                    break

                if j.isnumeric():
                    num_2 = j

            value = str(num_1) + str(num_2)

            total += int(value)

    print(total)


def part_two():
    numbers = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]


if __name__ == "__main__":
    part_one()

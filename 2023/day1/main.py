import re


class Day1:
    def __init__(self, input_file):
        self.input_file = input_file

    def part_one(self):
        total = 0

        with open(self.input_file, "r") as file:
            for line in file:
                digits = re.findall(r"\d", line)

                line_num = digits[0] + digits[-1]

                total += int(line_num)

        return total

    def part_two(self):
        number_strings = [
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

        get_num_from_string = lambda s: number_strings.index(s) + 1

        def convert_to_int(string):
            try:
                return int(string)
            except ValueError:
                return get_num_from_string(string)

        total = 0

        with open(self.input_file, "r") as file:
            for line in file:
                line = line.strip()

                nums = []

                for i in range(len(line)):
                    char = line[i]

                    if char.isnumeric():
                        nums.append(char)
                    else:
                        for string in number_strings:
                            if line[i:].startswith(string):
                                nums.append(string)

                line_num = convert_to_int(nums[0]) * 10 + convert_to_int(nums[-1])

                total += line_num

        return total


if __name__ == "__main__":
    day1 = Day1("input.txt")
    print("Part One Total:", day1.part_one())
    print("Part Two Total:", day1.part_two())

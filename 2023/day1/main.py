class Day1:
    def __init__(self, input_file):
        self.input_file = input_file

    # could have used regex to get the digits
    def part_one(self):
        """
        Finds the first and last numeric characters in each line, concatenates them, and sums them up.
        """

        total = 0

        with open(self.input_file, "r") as file:

            for line in file:
                num_1 = None
                num_2 = None

                for char in line:
                    if num_1:
                        break

                    if char.isnumeric():
                        num_1 = char

                for char in reversed(line):
                    if num_2:
                        break

                    if char.isnumeric():
                        num_2 = char

                value = str(num_1) + str(num_2)

                total += int(value)

        return total

    def part_two(self):
        """
        Tries to find numeric words (e.g., "one", "two") near numeric digits in each line, concatenates them, and sums.
        """
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

        # try and find the numbers using is numberic
        # if found, slice the string from the start or end until the index
        # search that slice for the number string
        # if found, use that as the number

        total = 0

        with open(self.input_file, "r") as file:

            for line in file:
                num_1 = None
                num_2 = None

                for index, i in enumerate(line):
                    if num_1:
                        up_to_num = line.slice(index)

                        nums_in_string = []

                        for num in numbers:
                            if num in up_to_num:
                                nums_in_string.append(num)

                        # check for position of num substring in string
                        # .find() returns the index of the start of the substring
                        # use the first substring as the value

                    if i.isnumeric():
                        num_1 = i

                for index, j in enumerate(reversed(line)):
                    if num_2:
                        break

                    if j.isnumeric():
                        num_2 = j

                value = str(num_1) + str(num_2)

                total += int(value)

        return total


if __name__ == "__main__":
    day1 = Day1("input.txt")
    print("Part One Total:", day1.part_one())
    print("Part Two Total:", day1.part_two())

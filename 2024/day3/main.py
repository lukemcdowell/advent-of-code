import re


class Main:
    def __init__(self, input_file):
        self.data = self.get_data(input_file)

    def get_data(self, filename):
        with open(filename, "r") as file:
            return file.read()

    def part_one(self):
        total = 0

        # match mul(X,Y) where X and Y are 1 to 3 digit numbers
        matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", self.data)

        for m in matches:
            nums = [int(n) for n in re.findall(r"\d{1,3}", m)]
            total += nums[0] * nums[1]

        return total

    def part_two(self):
        total = 0
        # match mul() and also do() and don't()
        matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", self.data)

        # loop through all matches, ignore mul() between don't() and do()
        ignore = False
        for m in matches:
            if m == "do()":
                ignore = False
            elif m == "don't()":
                ignore = True
            elif not ignore:
                nums = [int(n) for n in re.findall(r"\d{1,3}", m)]
                total += nums[0] * nums[1]

        return total


if __name__ == "__main__":
    day1 = Main("input.txt")
    print("Part One Total:", day1.part_one())
    print("Part Two Total:", day1.part_two())

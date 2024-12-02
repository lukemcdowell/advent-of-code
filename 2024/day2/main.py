import re


class Main:
    def __init__(self, input_file):
        self.data = self.get_data(input_file)

    def get_data(self, filename):
        with open(filename, "r") as file:
            return [x.strip() for x in file.readlines()]

    # check number is increasing or decreasing in a "safe" range
    def check_gradual_change(self, num1, num2, is_asc):
        if is_asc:
            return num1 < num2 <= num1 + 3
        else:
            return num1 > num2 >= num1 - 3

    # nums in line have to be either gradually increasing or decreasing in safe range
    def part_one(self):
        safe_reports = 0

        for line in self.data:
            digits = [int(s) for s in re.findall(r"\d+", line)]

            safe = True

            is_asc = True
            if digits[0] > digits[1]:
                is_asc = False

            for i in range(len(digits) - 1):
                if not self.check_gradual_change(digits[i], digits[i + 1], is_asc):
                    safe = False
                    break

            if safe:
                safe_reports += 1

        return safe_reports

    # line is safe if one num can be removed to make it "safe"
    def part_two(self):
        safe_reports = 0

        def check_asc(digits):
            asc, desc = 0, 0

            for i in range(len(digits) - 1):
                if digits[i] < digits[i + 1]:
                    asc += 1
                else:
                    desc += 1

            return asc > desc

        def check_valid_sequence(levels, is_asc):
            invalid_index = None

            for i in range(len(levels) - 1):
                if not self.check_gradual_change(levels[i], levels[i + 1], is_asc):
                    invalid_index = i + 1
                    break

            return invalid_index

        for line in self.data:
            digits = [int(s) for s in re.findall(r"\d+", line)]

            safe = True
            is_asc = check_asc(digits)

            invalid_index = check_valid_sequence(digits, is_asc)
            if invalid_index:
                remaining = digits[invalid_index:]

                if invalid_index - 1 != 0:
                    if self.check_gradual_change(
                        invalid_index - 1, invalid_index + 1, is_asc
                    ):
                        remaining[0] = digits[invalid_index - 1]
                    # covers 7, 10, 8, 10, 11
                    else:
                        remaining[0] = digits[invalid_index]

                remainder_is_valid = check_valid_sequence(remaining, is_asc)
                if remainder_is_valid:
                    safe = False

            if safe:
                safe_reports += 1

        return safe_reports


if __name__ == "__main__":
    day1 = Main("input.txt")
    print("Part One Total:", day1.part_one())
    print("Part Two Total:", day1.part_two())

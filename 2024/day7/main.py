from itertools import product


class Main:
    def __init__(self, input_file):
        self.data = self.get_data(input_file)

    def get_data(self, filename):
        with open(filename, "r") as file:
            return [x.strip() for x in file.readlines()]

    def part_one(self):
        total = 0

        # represent all combinations of * and + as binary
        def count_up_in_binary(bits):
            max_number = 2**bits
            combinations = []
            for i in range(max_number):
                binary_representation = f"{i:0{bits}b}"
                combinations.append(binary_representation)
            return combinations

        for line in self.data:
            v = int(line.split(":")[0])  # value
            nums = [int(n) for n in line.split(":")[1].strip().split(" ")]

            combos = count_up_in_binary(len(nums) - 1)

            # go through each num and append to total based on operator
            for c in combos:
                val = nums[0]
                for i in range(1, len(nums)):
                    if c[i - 1] == "1":  # 1 = *
                        val *= nums[i]
                    else:  # 0 = +
                        val += nums[i]

                if val == v:
                    total += v
                    break
        return total

    def part_two(self):
        total = 0

        operators = ["*", "+", "||"]

        for line in self.data:
            v = int(line.split(":")[0])  # value
            nums = [int(n) for n in line.split(":")[1].strip().split(" ")]

            # generate a list of all possible orders
            combos = list(product(operators, repeat=len(nums) - 1))

            # go through each num and append to total based on operator
            for c in combos:
                val = nums[0]
                for i in range(1, len(nums)):
                    if c[i - 1] == "*":
                        val *= nums[i]
                    elif c[i - 1] == "||":
                        val = int(str(val) + str(nums[i]))
                    else:  # +
                        val += nums[i]

                if val == v:
                    total += v
                    break
        return total


if __name__ == "__main__":
    day1 = Main("input.txt")
    print("Part One Total:", day1.part_one())
    print("Part Two Total:", day1.part_two())

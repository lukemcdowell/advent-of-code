class DayX:
    def __init__(self, input_file):
        self.input_file = input_file

        self.data = self.get_data(input_file)

    def get_data(filename):
        return [x.strip() for x in open(filename).readlines()]

    def part_one(self):
        """
        Does something
        """

        with open(self.input_file, "r") as file:
            pass

        pass

    def part_two(self):
        """
        Does something else
        """

        with open(self.input_file, "r") as file:
            pass

        pass


if __name__ == "__main__":
    day1 = DayX("input.txt")
    print("Part One Total:", day1.part_one())
    print("Part Two Total:", day1.part_two())

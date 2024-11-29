class Main:
    def __init__(self, input_file):
        self.data = self.get_data(input_file)

    def get_data(self, filename):
        return [x.strip() for x in open(filename).readlines()]

    def part_one(self):
        for line in self.data:
            pass

    def part_two(self):
        for line in self.data:
            pass


if __name__ == "__main__":
    day1 = Main("input.txt")
    print("Part One Total:", day1.part_one())
    print("Part Two Total:", day1.part_two())

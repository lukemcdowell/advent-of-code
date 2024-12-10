class Main:
    def __init__(self, input_file):
        self.data = self.get_data(input_file)

    def get_data(self, filename):
        with open(filename, "r") as file:
            return [x.strip() for x in file.readlines()]

    def part_one(self):
        for line in self.data:
            pass

    def part_two(self):
        for line in self.data:
            pass


if __name__ == "__main__":
    main = Main("input.txt")
    print("Part One Total:", main.part_one())
    print("Part Two Total:", main.part_two())

class Main:
    def __init__(self, input_file):
        self.data = self.get_data(input_file)

    def get_data(self, filename):
        with open(filename, "r") as file:
            return [x.strip() for x in file.readlines()]

    def part_one(self):
        max_cubes = {"red": 12, "green": 13, "blue": 14}
        total = 0

        for line in self.data:
            # parse the game number and turn data
            colon = line.index(":")
            game_id = int(line[:colon].split()[1])
            game = line[colon + 1 :].split(";")

            valid_game = True
            for turn in game:
                num_cubes = turn.split(",")
                for cube_color in num_cubes:
                    cubes = cube_color.split()
                    color = cubes[1].strip()
                    num = int(cubes[0])

                    # check the num of cubes is less than max
                    if num > max_cubes[color]:
                        valid_game = False
                        break
            if valid_game:
                total += game_id

        return total

    def part_two(self):
        total = 0

        for line in self.data:
            min_cubes = {"red": 0, "green": 0, "blue": 0}

            # parse the game number and turn data
            colon = line.index(":")
            game = line[colon + 1 :].split(";")

            for turn in game:
                num_cubes = turn.split(",")
                for cube_color in num_cubes:
                    cubes = cube_color.split()
                    color = cubes[1].strip()
                    num = int(cubes[0])

                    # add the num of cubes if it is greater than the current value
                    if num > min_cubes[color]:
                        min_cubes[color] = num

            power = min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]
            total += power

        return total


if __name__ == "__main__":
    day1 = Main("input.txt")
    print("Part One Total:", day1.part_one())
    print("Part Two Total:", day1.part_two())

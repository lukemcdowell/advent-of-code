class Main:
    def __init__(self, input_file):
        self.data = self.get_data(input_file)

    def get_data(self, filename):
        with open(filename, "r") as file:
            return [x.strip() for x in file.readlines()]

    def part_one(self):
        g = [list(line) for line in self.data]  # grid
        rows = len(g)
        cols = len(g[0])

        possible_antinodes = set()
        chars = {}

        # find all alphanumeric chars in the map and store positions in dict
        for x in range(rows):
            for y in range(cols):
                if g[x][y].isalnum():
                    if g[x][y] in chars:
                        chars[g[x][y]].append((x, y))
                    else:
                        chars[g[x][y]] = [(x, y)]

        # loop over each set of chars
        for c in chars:
            positions = chars[c]
            # for each antenna a, find it's position relative to each other antenna o
            for a in positions:
                for o in positions:
                    if a == o:
                        continue
                    # change in position = (x2 - x1, y2 - y1)
                    x1, y1 = a
                    x2, y2 = o
                    diff = (x2 - x1, y2 - y1)

                    # the antinode will then be the same diff away from o
                    antinode = (x2 + diff[0], y2 + diff[1])
                    if 0 <= antinode[0] < rows and 0 <= antinode[1] < cols:
                        possible_antinodes.add(antinode)

        return len(possible_antinodes)

    def part_two(self):
        g = [list(line) for line in self.data]  # grid
        rows = len(g)
        cols = len(g[0])

        possible_antinodes = set()
        chars = {}

        # find all alphanumeric chars in the map
        for x in range(rows):
            for y in range(cols):
                if g[x][y].isalnum():
                    if g[x][y] in chars:
                        chars[g[x][y]].append((x, y))
                    else:
                        chars[g[x][y]] = [(x, y)]

        # loop over each set of chars
        for c in chars:
            positions = chars[c]

            # for each antenna a, find it's position relative to each other antenna o
            for a in positions:
                if len(positions) > 1:
                    possible_antinodes.add(a)
                for o in positions:
                    if a == o:
                        continue

                    # change in position = (x2 - x1, y2 - y1)
                    x1, y1 = a
                    x2, y2 = o

                    diff = (x2 - x1, y2 - y1)

                    # the antinodes will then be the same distance and dir away from o (repeating)
                    antinode = (x2 + diff[0], y2 + diff[1])

                    while True:
                        if 0 <= antinode[0] < rows and 0 <= antinode[1] < cols:
                            possible_antinodes.add(antinode)
                        else:
                            break

                        antinode = (antinode[0] + diff[0], antinode[1] + diff[1])

        return len(possible_antinodes)


if __name__ == "__main__":
    day1 = Main("input.txt")
    print("Part One Total:", day1.part_one())
    print("Part Two Total:", day1.part_two())

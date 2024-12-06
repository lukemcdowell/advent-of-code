class Main:
    def __init__(self, input_file):
        self.data = self.get_data(input_file)

        self.grid = [list(line) for line in self.data]
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])

        # directions and order
        self.dirs = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
        self.dir_order = ["^", ">", "v", "<"]

    def get_data(self, filename):
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]

    def part_one(self):
        visited_positions = set()
        guard_pos = None

        # find start position and direction
        for x in range(self.rows):
            if guard_pos:
                break
            for y in range(self.cols):
                if self.grid[x][y] in self.dirs:
                    guard_dir = self.grid[x][y]
                    guard_pos = (x, y)
                    break

        while True:
            x, y = guard_pos
            if guard_pos not in visited_positions:
                visited_positions.add(guard_pos)

            # calculate next position
            dx, dy = self.dirs[guard_dir]
            nx, ny = x + dx, y + dy

            # check if out of bounds
            if not (0 <= nx < self.rows and 0 <= ny < self.cols):
                break

            # turn right if obstacle,
            if self.grid[nx][ny] == "#":
                guard_dir = self.dir_order[(self.dir_order.index(guard_dir) + 1) % 4]
            # move forward
            else:
                guard_pos = (nx, ny)

        return len(visited_positions)

    def part_two(self):
        possible_obstacles = set()
        turns = []
        guard_pos = None

        # find start position and direction
        for x in range(self.rows):
            if guard_pos:
                break
            for y in range(self.cols):
                if self.grid[x][y] in self.dirs:
                    guard_dir = self.grid[x][y]
                    guard_pos = (x, y)
                    break

        while True:
            x, y = guard_pos

            # calculate next position
            dx, dy = self.dirs[guard_dir]
            nx, ny = x + dx, y + dy

            # check if out of bounds
            if not (0 <= nx < self.rows and 0 <= ny < self.cols):
                break

            # turn right if obstacle,
            if self.grid[nx][ny] == "#":
                guard_dir = self.dir_order[(self.dir_order.index(guard_dir) + 1) % 4]
                turns.append((x, y))
            # move forward
            else:

                # check for possible infinite loops by placing obstacles
                # currently only works for rectangles
                if len(turns) >= 4:
                    # check if placing an obsctacle infront would make a loop
                    # to make a loop, current position would have to intercept the line
                    # made between two turns ago and three turns ago
                    x1, y1 = (x, y)  # current point
                    x2, y2 = turns[-3]  # two turns ago
                    x3, y3 = turns[-4]  # three turns ago

                    # check that a, b and c are on the same line
                    # https://math.stackexchange.com/questions/405966/if-i-have-three-points-is-there-an-easy-way-to-tell-if-they-are-collinear
                    if (y1 - y2) * (x1 - x3) == (y1 - y3) * (x1 - x2):
                        if (nx, ny) not in possible_obstacles:
                            possible_obstacles.add((nx, ny))

                guard_pos = (nx, ny)

        return len(possible_obstacles)


if __name__ == "__main__":
    day6 = Main("sample.txt")
    print("Part One Total:", day6.part_one())

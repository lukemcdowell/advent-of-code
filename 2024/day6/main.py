import time


class Main:
    def __init__(self, input_file):
        self.data = self.get_data(input_file)

        self.grid = [list(line) for line in self.data]
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])

        # directions and order
        self.dirs = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
        self.dir_order = ["^", ">", "v", "<"]
        # could have just used one list and stored dir as an int

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
        total = 0
        guard_pos, guard_dir = None, None
        start_pos, start_dir = None, None

        # find start position and direction
        for x in range(self.rows):
            if guard_pos:
                break
            for y in range(self.cols):
                if self.grid[x][y] in self.dirs:
                    start_pos = (x, y)
                    start_dir = self.grid[x][y]
                    guard_pos = (x, y)
                    guard_dir = self.grid[x][y]
                    break

        # get a list of all visited positions
        visited_positions = set()
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

        def check_loop(pos, dir):
            num_moves = 0

            while True:
                max_moves = self.rows * self.cols * 4 + 1
                if num_moves > max_moves:
                    return True

                x, y = pos

                # calculate next position
                dx, dy = self.dirs[dir]
                nx, ny = x + dx, y + dy

                # check if out of bounds
                if not (0 <= nx < self.rows and 0 <= ny < self.cols):
                    return False

                # turn right if obstacle,
                if self.grid[nx][ny] == "#":
                    dir = self.dir_order[(self.dir_order.index(dir) + 1) % 4]
                # move forward
                else:
                    pos = (nx, ny)

                num_moves += 1

        for x in range(self.rows):
            for y in range(self.cols):
                # check all visited positions and see if placing a # there causes an infinite loop
                if (x, y) in visited_positions and self.grid[x][y] == ".":
                    print("check: ", (x, y))
                    self.grid[x][y] = "#"
                    if check_loop(start_pos, start_dir):
                        total += 1
                    self.grid[x][y] = "."

        return total


if __name__ == "__main__":
    day6 = Main("input.txt")
    print("Part One Total:", day6.part_one())
    print("Part Two Total:", day6.part_two())

class Main:
    def __init__(self, input_file):
        self.data = self.get_data(input_file)

        # convert file into 2d array
        self.grid = []
        for line in self.data:
            self.grid.append(list(line))

        self.cols = len(self.grid[0])
        self.rows = len(self.grid)

    def get_data(self, filename):
        with open(filename, "r") as file:
            return [x.strip() for x in file.readlines()]

    def part_one(self):
        total = 0

        # direction = 1 (up and left), 2 (up) ... 8 (left)
        def get_m_direction(x, y, i, j):
            m_dirs = []

            if i == x - 1 and j == y - 1:
                m_dirs.append(1)
            elif i == x - 1 and j == y:
                m_dirs.append(2)
            elif i == x - 1 and j == y + 1:
                m_dirs.append(3)
            elif i == x and j == y + 1:
                m_dirs.append(4)
            elif i == x + 1 and j == y + 1:
                m_dirs.append(5)
            elif i == x + 1 and j == y:
                m_dirs.append(6)
            elif i == x + 1 and j == y - 1:
                m_dirs.append(7)
            elif i == x and j == y - 1:
                m_dirs.append(8)

            return m_dirs

        # get coords of square to check based on dir
        def coords_to_check(x, y, dir):
            match dir:
                case 1:
                    return x - 1, y - 1
                case 2:
                    return x - 1, y
                case 3:
                    return x - 1, y + 1
                case 4:
                    return x, y + 1
                case 5:
                    return x + 1, y + 1
                case 6:
                    return x + 1, y
                case 7:
                    return x + 1, y - 1
                case 8:
                    return x, y - 1

        # check surrounding squares for "M", return directions
        def check_surrounding(x, y):
            dirs = []
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if not (0 <= i < self.rows) or not (0 <= j < self.cols):
                        continue
                    if i == x and j == y:
                        continue

                    # if match, record direction and check for A, then S in that direction
                    if self.grid[i][j] == "M":
                        dir = get_m_direction(x, y, i, j)[0]
                        check_dir(i, j, "A", dir)

            return dirs

        # call recursively with different char
        def check_dir(x, y, char, dir):
            nonlocal total

            i, j = coords_to_check(x, y, dir)
            if not (0 <= i < self.rows) or not (0 <= j < self.cols):
                return
            if self.grid[i][j] == char:
                # if S found, increment total
                if char == "S":
                    total += 1
                else:
                    check_dir(i, j, "S", dir)

        # loop over characters and check for "X"
        for x in range(self.rows):
            for y in range(self.cols):
                if self.grid[x][y] == "X":

                    # if X, search surrounding square in grid for M
                    check_surrounding(x, y)
        return total

    def part_two(self):
        total = 0

        for x in range(self.rows):
            for y in range(self.cols):
                if self.grid[x][y] == "A":

                    if not (1 <= x < self.rows - 1) or not (1 <= y < self.cols - 1):
                        continue

                    corners = (
                        self.grid[x - 1][y - 1],
                        self.grid[x - 1][y + 1],
                        self.grid[x + 1][y - 1],
                        self.grid[x + 1][y + 1],
                    )

                    valid_crosses = [
                        ("M", "M", "S", "S"),
                        ("M", "S", "M", "S"),
                        ("S", "S", "M", "M"),
                        ("S", "M", "S", "M"),
                    ]

                    for config in valid_crosses:
                        if corners == config:
                            total += 1

        return total


if __name__ == "__main__":
    day1 = Main("input.txt")
    print("Part One Total:", day1.part_one())
    print("Part Two Total:", day1.part_two())

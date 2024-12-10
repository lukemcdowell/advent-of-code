from collections import deque


class Main:
    def __init__(self, input_file):
        self.data = self.get_data(input_file)

    def get_data(self, filename):
        with open(filename, "r") as file:
            return [x.strip() for x in file.readlines()]

    def part_one(self):
        grid = [[int(n) for n in line] for line in self.data]
        rows, cols = len(grid), len(grid[0])
        total_score = 0

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # find all paths to a 9 from a zero using BFS
        def calculate_score(x, y):
            visited = set()
            queue = deque([(x, y, 0)])  # BFS queue: (current x, current y, height)
            nines = set()

            while queue:
                cx, cy, current_height = queue.popleft()

                if (cx, cy) in visited:
                    continue
                visited.add((cx, cy))

                if grid[cx][cy] == 9:
                    nines.add((cx, cy))
                    continue

                # explore all neighbors
                # if neighbour is a valid height progression, add to queue
                for dx, dy in dirs:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                        if grid[nx][ny] == current_height + 1:
                            queue.append((nx, ny, current_height + 1))

            return len(nines)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    total_score += calculate_score(r, c)

        return total_score

    # the same as part one minus tracking the squares that have been visited
    def part_two(self):
        grid = [[int(n) for n in line] for line in self.data]
        rows, cols = len(grid), len(grid[0])
        total_score = 0

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # find all paths to a 9 from a zero using BFS
        def calculate_score(x, y):
            queue = deque([(x, y, 0)])  # BFS queue: (current x, current y, height)
            nines = []

            while queue:
                cx, cy, current_height = queue.popleft()

                if grid[cx][cy] == 9:
                    nines.append((cx, cy))
                    continue

                # explore all neighbors
                # if neighbour is a valid height progression, add to queue
                for dx, dy in dirs:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < rows and 0 <= ny < cols and (nx, ny):
                        if grid[nx][ny] == current_height + 1:
                            queue.append((nx, ny, current_height + 1))

            return len(nines)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    total_score += calculate_score(r, c)

        return total_score


if __name__ == "__main__":
    main = Main("input.txt")
    print("Part One Total:", main.part_one())
    print("Part Two Total:", main.part_two())

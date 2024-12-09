class Main:
    def __init__(self, input_file):
        self.data = self.get_data(input_file)

    def get_data(self, filename):
        with open(filename, "r") as file:
            return file.read()

    def part_one(self):
        total = 0

        disk = []
        file_index = 0
        for i, size in enumerate(self.data):
            if i % 2 == 0:  # file
                disk += [file_index] * int(size)
                file_index += 1
            else:  # free space
                disk += ["."] * int(size)

        for i, b in enumerate(disk):
            if b == ".":
                last_file_index = None
                while True:
                    file = disk.pop()
                    if file == ".":
                        continue
                    else:
                        last_file_index = file
                        break

                total += i * last_file_index
            else:
                total += i * b
        return total

    def part_two(self):
        total = 0

        def find_empty(list, size):
            c = 1
            for i, x in enumerate(list):
                if x == ".":
                    c += 1
                else:
                    c = 0
                if c == size:
                    return i - size + 1

        disk = []
        files = []  # store sizes and index of disk
        file_index, disk_index = 0, 0
        for i, size in enumerate(self.data):
            if i % 2 == 0:  # file
                disk += [file_index] * int(size)
                files.append((int(size), file_index, disk_index))
                file_index += 1
                disk_index += int(size)
            else:  # free space
                if int(size) == 0:
                    continue
                disk += ["."] * int(size)
                disk_index += int(size)

        files.reverse()

        # for each file, try and move left
        for f in files:  # size, file index, disk index
            left = disk[: f[2]]

            e = find_empty(left, f[0])

            if e:
                for i in range(f[0]):
                    disk[e + i] = f[1]
                    disk[f[2] + i] = "."

        for i, b in enumerate(disk):
            if b == ".":
                continue
            else:
                total += i * b

        return total


if __name__ == "__main__":
    day1 = Main("input.txt")
    print("Part One Total:", day1.part_one())
    print("Part Two Total:", day1.part_two())

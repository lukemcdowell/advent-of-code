class Main:
    def __init__(self, input_file):
        self.data = self.get_data(input_file)

    def get_data(self, filename):
        with open(filename, "r") as file:
            return file.read()

    def part_one(self):
        total = 0

        files, free_space = [], []
        for i, f in enumerate(self.data):
            if i % 2 == 0:  # file
                files.append(int(f))
            else:  # free space
                free_space.append(int(f))

        disk = []
        for i, file_size in enumerate(files):
            disk += [i] * file_size

        total_space = sum(files)

        print(self.data)
        print(files)
        print("sum", sum(files))
        print(disk)
        print(total_space)

        index = 0
        file_index = 0
        for i, size in enumerate(self.data):
            if total_space == 0:
                return total

            # if file, fore size of block, add index * file index to total
            if i % 2 == 0:
                for j in range(int(size)):
                    print(
                        f"{index}. file. size: {size}, file index: {file_index}. total: {index * file_index}"
                    )
                    total += index * file_index
                    index += 1
                file_index += 1
            # if empty, for the size of the block, add index * last file index to total
            else:
                for j in range(int(size)):
                    if total_space == 0:
                        return total

                    last_file_index = disk.pop()
                    print("pop:", last_file_index)
                    print(disk)
                    print(
                        f"{index}. empty. size: {size}, last file index: {last_file_index}. total: {index * last_file_index}"
                    )
                    print("total space: ", total_space)
                    total += index * last_file_index
                    index += 1
                    total_space -= 1

    def part_two(self):
        for line in self.data:
            pass


if __name__ == "__main__":
    day1 = Main("sample.txt")
    print("Part One Total:", day1.part_one())
    print("Part Two Total:", day1.part_two())

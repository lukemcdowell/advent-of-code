from collections import Counter


class Main:
    def __init__(self, input_file):
        self.data = self.get_data(input_file)

    def get_data(self, filename):
        with open(filename, "r") as file:
            return [int(s) for s in file.read().strip().split()]

    # brute forced
    def part_one(self):
        stones = self.data

        def blink():
            nonlocal stones
            new_stones = []
            for s in stones:
                if s == 0:
                    new_stones.append(1)
                elif len(str(s)) % 2 == 0:
                    l, r = str(s)[: len(str(s)) // 2], str(s)[len(str(s)) // 2 :]
                    new_stones.append(int(l))
                    new_stones.append(int(r))
                else:
                    new_stones.append(s * 2024)

            stones = new_stones

        for _ in range(25):
            blink()

        return len(stones)

    # memoising with Counter
    def part_two(self):
        stones = Counter(self.data)

        def blink(stones):
            new_stones = Counter()
            for s, count in stones.items():
                if s == 0:
                    new_stones[1] += count
                elif len(str(s)) % 2 == 0:
                    l, r = str(s)[: len(str(s)) // 2], str(s)[len(str(s)) // 2 :]
                    new_stones[int(l)] += count
                    new_stones[int(r)] += count
                else:
                    new_stones[s * 2024] += count

            return new_stones

        for _ in range(75):
            stones = blink(stones)

        return sum(stones.values())


if __name__ == "__main__":
    main = Main("input.txt")
    print("Part One Total:", main.part_one())
    print("Part Two Total:", main.part_two())

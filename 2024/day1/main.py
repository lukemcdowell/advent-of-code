from collections import Counter


class Main:
    def __init__(self, input_file):
        self.data = self.get_data(input_file)

    def get_data(self, filename):
        with open(filename, "r") as file:
            return [x.strip() for x in file.readlines()]

    def part_one(self):
        list1 = []
        list2 = []
        diff = []

        for line in self.data:
            nums = line.split("   ")

            list1.append(int(nums[0]))
            list2.append(int(nums[1]))

        list1.sort()
        list2.sort()

        for i in range(len(list1)):
            diff.append(abs(list1[i] - list2[i]))

        return sum(diff)

    def part_two(self):
        list1 = []
        list2 = []
        score = []

        for line in self.data:
            nums = line.split("   ")

            list1.append(int(nums[0]))
            list2.append(int(nums[1]))

        # find num of occurrences in list2 and calculate "similarity score" (occurrences * num)
        c = Counter(list2)
        for num in list1:
            score.append(num * c[num])

        return sum(score)


if __name__ == "__main__":
    day1 = Main("input.txt")
    print("Part One Total:", day1.part_one())
    print("Part Two Total:", day1.part_two())

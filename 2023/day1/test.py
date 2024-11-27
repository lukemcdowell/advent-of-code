import unittest
from main import Day1


class TestDay1(unittest.TestCase):

    def test_part_one(self):
        day1 = Day1("sample1.txt")

        expected_result = 142
        result = day1.part_one()

        self.assertEqual(result, expected_result)

    def test_part_two(self):
        day1 = Day1("sample2.txt")

        expected_result = 281
        result = day1.part_two()

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()

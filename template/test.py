import unittest
from main import DayX


class TestDay1(unittest.TestCase):

    def test_part_one(self):
        dayX = DayX("sample1.txt")

        expected_result = 123
        result = dayX.part_one()

        self.assertEqual(result, expected_result)

    def test_part_two(self):
        dayX = DayX("sample2.txt")

        expected_result = 123
        result = dayX.part_two()

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()

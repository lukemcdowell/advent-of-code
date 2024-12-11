import unittest
from main import Main


class TestMain(unittest.TestCase):

    def test_part_one(self):
        main = Main("sample.txt")

        expected_result = 55312
        result = main.part_one()

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()

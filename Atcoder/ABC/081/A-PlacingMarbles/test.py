import unittest
from main import solution


class TestMain(unittest.TestCase):
    def test_solve(self):
        actual1: str = solution("101")
        actual2: str = solution("000")

        self.assertEqual(actual1, 2)
        self.assertEqual(actual2, 0)


if __name__ == '__main__':
    unittest.main()

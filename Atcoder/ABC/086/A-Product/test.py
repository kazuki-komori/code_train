import unittest
from main import solve


class TestMain(unittest.TestCase):
    def test_solve(self):
        actual1: str = solve(3, 4)
        actual2: str = solve(1, 21)

        self.assertEqual(actual1, "Even")
        self.assertEqual(actual2, "Odd")


if __name__ == '__main__':
    unittest.main()

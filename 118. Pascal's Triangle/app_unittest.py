from app import Solution
import unittest

class TestPascalTriangle(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_generate(self):
        self.assertEqual(
            self.solution.generate(0),
            []
        )
        self.assertEqual(
            self.solution.generate(1),
            [[1]]
        )
        self.assertEqual(
            self.solution.generate(2),
            [[1], [1,1]]
        )
        self.assertEqual(
            self.solution.generate(5),
            [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
        )


if __name__ == '__main__':
    unittest.main()
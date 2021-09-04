from app import Solution
import unittest

class TestPascalTriangle2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_get_row(self):
        self.assertEqual(self.solution.getRow(0), [1])
        self.assertEqual(self.solution.getRow(1), [1,1])
        self.assertEqual(self.solution.getRow(2), [1,2,1])
        self.assertEqual(self.solution.getRow(3), [1,3,3,1])
        self.assertEqual(self.solution.getRow(4), [1,4,6,4,1])


if __name__ == '__main__':
    unittest.main()
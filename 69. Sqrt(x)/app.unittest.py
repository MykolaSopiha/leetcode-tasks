import unittest

from app import Solution


class TestSqrt(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
    
    def test_my_sqrt(self):
        self.assertEqual(self.solution.mySqrt(1), 1)
        self.assertEqual(self.solution.mySqrt(2), 1)
        self.assertEqual(self.solution.mySqrt(3), 1)
        self.assertEqual(self.solution.mySqrt(4), 2)
        self.assertEqual(self.solution.mySqrt(6), 2)
        self.assertEqual(self.solution.mySqrt(8), 2)
        self.assertEqual(self.solution.mySqrt(36), 6)

if __name__ == '__main__':
    unittest.main()

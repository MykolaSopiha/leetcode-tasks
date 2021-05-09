import unittest

from app import Solution

class TestPlusOne(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_plus_one(self):
        self.assertEqual(self.solution.plusOne([1,2,3]),   [1,2,4])
        self.assertEqual(self.solution.plusOne([4,3,2,1]), [4,3,2,2])
        self.assertEqual(self.solution.plusOne([0]),       [1])
        self.assertEqual(self.solution.plusOne([9]),       [1,0])

if __name__ == '__main__':
    unittest.main()
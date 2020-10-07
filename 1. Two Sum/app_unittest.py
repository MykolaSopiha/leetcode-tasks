import unittest
from app import Solution

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_two_sum(self):
        self.assertCountEqual(self.solution.twoSum([2,7,11,15], 9), [0, 1])
        self.assertCountEqual(self.solution.twoSum([3,2,4],     6), [1, 2])
        self.assertCountEqual(self.solution.twoSum([3,3],       6), [1, 0])


if __name__ == '__main__':
    unittest.main()
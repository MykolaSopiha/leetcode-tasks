from app import Solution
import unittest

class TestMaxSubarray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_two_sum(self):
        self.assertEqual(self.solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), 6)
        self.assertEqual(self.solution.maxSubArray([1]), 1)
        self.assertEqual(self.solution.maxSubArray([5,4,-1,7,8]), 23)
        self.assertEqual(self.solution.maxSubArray([-1]), -1)
        self.assertEqual(self.solution.maxSubArray([-2,1]), 1)


if __name__ == '__main__':
    unittest.main()
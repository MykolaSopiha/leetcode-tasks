import unittest
from app import Solution

class TestСountAndSay(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_count_and_say(self):
        self.assertListEqual(
            self.solution.combinationSum(candidates = [2,3,6,7], target = 7),
            [[2,2,3],[7]]
        )
        self.assertListEqual(
            self.solution.combinationSum(candidates = [2,3,5], target = 8),
            [[2,2,2,2],[2,3,3],[3,5]]
        )

if __name__ == '__main__':
    unittest.main()
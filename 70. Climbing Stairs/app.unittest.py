import unittest

from app import Solution


class TestClimbingStairs(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
    
    def test_climb_stairs(self):
        self.assertEqual(self.solution.climbStairs(1), 1)
        self.assertEqual(self.solution.climbStairs(2), 2)
        self.assertEqual(self.solution.climbStairs(3), 3)

if __name__ == '__main__':
    unittest.main()

import unittest
from app import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def addToArrayForm(self):
        self.assertEqual(
            self.solution.addToArrayForm([1,2,0,0], 34),
            [1,2,3,4]
        )
        self.assertEqual(
            self.solution.addToArrayForm([2,7,4], 181),
            [4,5,5]
        )
        self.assertEqual(
            self.solution.addToArrayForm([2,1,5], 806),
            [1,0,2,1]
        )


if __name__ == '__main__':
    unittest.main()
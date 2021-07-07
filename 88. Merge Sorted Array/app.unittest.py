import unittest

from app import Solution

class TestСountAndSay(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_count_and_say(self):
        self.assertEqual(
            self.solution.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3),
            [1, 2, 2, 3, 5, 6]
        )
        self.assertEqual(
            self.solution.merge([1],1,[],0),
            [1]
        )
        self.assertEqual(
            self.solution.merge([2,0],1,[1],1),
            [1, 2]
        )

if __name__ == '__main__':
    unittest.main()
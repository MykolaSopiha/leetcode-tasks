import unittest

from app import Solution

class TestLongestSubstringWithoutRepeating(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_length_of_longest_substring(self):
        self.assertEqual(self.solution.findMedianSortedArrays([1,3], [2]), 2)
        self.assertEqual(self.solution.findMedianSortedArrays([1,2], [3,4]), 2.5)
        self.assertEqual(self.solution.findMedianSortedArrays([0,0], [0,0]), 0)
        self.assertEqual(self.solution.findMedianSortedArrays([], [1]), 1)
        self.assertEqual(self.solution.findMedianSortedArrays([2], []), 2)


if __name__ == '__main__':
    unittest.main()
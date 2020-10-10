import unittest

from app import Solution

class TestLongestSubstringWithoutRepeating(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test1_length_of_longest_substring(self):
        self.assertEqual(
            self.solution.lengthOfLongestSubstring('abcabcbb'),
            3
        )
        self.assertEqual(
            self.solution.lengthOfLongestSubstring('bbbbb'),
            1
        )
        self.assertEqual(
            self.solution.lengthOfLongestSubstring('pwwkew'),
            3
        )


if __name__ == '__main__':
    unittest.main()
import unittest

from app import Solution

class TestLongestPalindromicSubstring(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_longest_palindrome(self):
        self.assertEqual(self.solution.longestPalindrome('babad'), 'bab')
        self.assertEqual(self.solution.longestPalindrome('cbbd'),  'bb')
        self.assertEqual(self.solution.longestPalindrome('a'),     'a')
        self.assertEqual(self.solution.longestPalindrome('ac'),    'a')

if __name__ == '__main__':
    unittest.main()
import unittest

from app import Solution


class TestValidPalindrome(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_is_palindrome(self):
        self.assertTrue(self.solution.isPalindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(self.solution.isPalindrome("aa"))
        self.assertTrue(self.solution.isPalindrome("a"))
        self.assertTrue(self.solution.isPalindrome(""))
        self.assertFalse(self.solution.isPalindrome("race a car"))


if __name__ == '__main__':
    unittest.main()

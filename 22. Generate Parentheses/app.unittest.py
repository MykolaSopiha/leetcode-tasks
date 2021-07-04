import unittest

from app import Solution

class TestGenerateParentheses(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_generate_parenthesis(self):
        self.assertCountEqual(self.solution.generateParenthesis(0), [''])
        self.assertCountEqual(self.solution.generateParenthesis(3), ["((()))","(()())","(())()","()(())","()()()"])

if __name__ == '__main__':
    unittest.main()
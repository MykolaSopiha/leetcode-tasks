import unittest

from app import Solution
from app import ListNode

class TestIsPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def listTwoLinkedList(self, nodeValues: list) -> ListNode:
        head = prev = None
        nodeValues.reverse()

        for value in nodeValues:
            head = ListNode(value, prev)
            prev = head
        
        return head

    def test_is_palindrome(self):
        head = self.listTwoLinkedList([1,2,3,4,5,6,5,4,3,2,1])
        self.assertIs(self.solution.isPalindrome(head), True)

        head = self.listTwoLinkedList([1,2])
        self.assertIs(self.solution.isPalindrome(head), False)

        head = self.listTwoLinkedList([1,2,3,4,5,6])
        self.assertIs(self.solution.isPalindrome(head), False)

        head = self.listTwoLinkedList([1])
        self.assertIs(self.solution.isPalindrome(head), True)

        head = self.listTwoLinkedList([])
        self.assertIs(self.solution.isPalindrome(head), True)

if __name__ == '__main__':
    unittest.main()
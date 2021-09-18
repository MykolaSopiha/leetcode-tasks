import unittest
from typing import List

from app import Solution
from data_structures import ListNode

class TestAddTwoNumbers(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def get_linked_list(self, nums: List[int]):
        tail = None

        for value in reversed(nums):
            tmp = tail
            tail = ListNode(value)
            tail.next = tmp
        
        return tail

    def test1_add_two_numbers(self):
        nums1 = [2, 4, 3]
        nums2 = [5, 6, 4]
        expect = [7, 0, 8]

        list1 = self.get_linked_list(nums1)
        list2 = self.get_linked_list(nums2)

        tail = self.solution.addTwoNumbers(list1, list2)
        result = []

        while tail:
            result.append(tail.val)
            tail = tail.next
        
        self.assertEqual(result, expect)

    def test2_add_two_numbers(self):
        nums1 = [0]
        nums2 = [0]
        expect = [0]

        list1 = self.get_linked_list(nums1)
        list2 = self.get_linked_list(nums2)

        tail = self.solution.addTwoNumbers(list1, list2)
        result = []

        while tail:
            result.append(tail.val)
            tail = tail.next
        
        self.assertEqual(result, expect)

    def test3_add_two_numbers(self):
        nums1 = [9,9,9,9,9,9,9]
        nums2 = [9,9,9,9]
        expect = [8,9,9,9,0,0,0,1]

        list1 = self.get_linked_list(nums1)
        list2 = self.get_linked_list(nums2)

        tail = self.solution.addTwoNumbers(list1, list2)
        result = []

        while tail:
            result.append(tail.val)
            tail = tail.next
        
        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main()
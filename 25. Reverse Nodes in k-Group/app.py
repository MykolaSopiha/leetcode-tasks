# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from math import floor

class Solution:
    def hasNextNodes(self, head: ListNode, num: int) -> bool:
        i = 0
        cursor = head
        while i < num:
            if cursor.next:
                cursor = cursor.next
                i = i + 1
            else:
                return False
        return True

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        cursor = head
        i = 0

        while self.hasNextNodes(cursor, k):
            cur = cursor
            for m in range(k):
                c = cur
                for n in range(k-m):
                    tmp = c.val
                    c.val = c.next.val
                    c.next.val = tmp
                    c = c.next
                cur = cur.next
            
            
            i = i + k
            for _ in range(k):
                cursor = cursor.next
        
        return head
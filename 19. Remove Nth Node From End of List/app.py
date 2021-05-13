# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        i = 0
        target = cursor = head
        prev = None
        
        while cursor:
            i = i + 1
            
            if i > n:
                prev = target
                target = target.next
            
            cursor = cursor.next
        
        if target and prev:
            prev.next = target.next
            target.next = None
        elif not prev and target:
            head = head.next
        
        return head
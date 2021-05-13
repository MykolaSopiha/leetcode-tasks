# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        startNode = None
        i = 0
        cursor = endNode = head
        
        while cursor:
            i = i + 1
            
            if i == k:
                startNode = cursor
            
            if i > k:
                endNode = endNode.next
            
            cursor = cursor.next
        
        tmp = startNode.val
        startNode.val = endNode.val
        endNode.val = tmp
        return head
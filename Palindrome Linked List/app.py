# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def listTwoLinkedList(self, nodeValues: list) -> ListNode:
        head = prev = None
        nodeValues.reverse()

        for value in nodeValues:
            head = ListNode(value, prev)
            prev = head
        
        return head
    
    def reverseLinkedList(self, head: ListNode) -> ListNode:
        node = prev = None

        while head:
            node = ListNode(head.val, prev)
            prev = node
            head = head.next
        
        return node

    def isPalindrome(self, head: ListNode) -> bool:
        fastPtr = rightPtr = slowPtr = head
        
        while fastPtr and fastPtr.next:
            fastPtr = fastPtr.next.next
            slowPtr = slowPtr.next
        
        if fastPtr == None or fastPtr == slowPtr:
            rightPtr = slowPtr
            print('+')
        elif fastPtr.next == None:
            rightPtr = slowPtr.next
            print('-')
        
        revRightPtr = self.reverseLinkedList(rightPtr)

        while revRightPtr:
            if revRightPtr.val == head.val:
                revRightPtr = revRightPtr.next
                head = head.next
            else:
                return False
        
        return True

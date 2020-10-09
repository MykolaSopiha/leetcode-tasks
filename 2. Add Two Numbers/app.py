from ListNode import ListNode

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        tail = head = ListNode(0)
        prev = head
        overflow = False

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            sum = x + y

            if overflow:
                sum += 1

            if sum > 9:
                sum %= 10
                overflow = True
            else:
                overflow = False
            
            tail = ListNode(sum)
            prev.next = tail
            prev = tail

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        if overflow:
            tail.next = ListNode(1)
        
        return head.next

from .list_node import ListNode


def compare_lists(head1: ListNode, head2: ListNode, debug: bool = False) -> bool:
    while True:
        if debug:
            print("{} : {}".format(
                head1 and head1.val,
                head2 and head2.val
            ))
        if not head1 and not head2:
            return True
        elif bool(head1) != bool(head2) or head1.val != head2.val:
            return False
        else:
            head1 = head1.next
            head2 = head2.next

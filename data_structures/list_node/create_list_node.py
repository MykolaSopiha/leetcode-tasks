from typing import List

from .list_node import ListNode


def create_list_node(nodes: List):
    head = prev = None
    for val in nodes[::-1]:
        head = ListNode(val, prev)
        prev = head
    return head

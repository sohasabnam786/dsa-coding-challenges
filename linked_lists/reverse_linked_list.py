"""
🟢 Reverse Linked List
Reverse a singly linked list iteratively and recursively.

Time:  O(n)
Space: O(1) iterative, O(n) recursive
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from utils import ListNode


def reverse_list(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


def reverse_list_recursive(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


if __name__ == "__main__":
    lst = ListNode.from_list([1, 2, 3, 4, 5])
    print(f"Original: {lst}")
    reversed_lst = reverse_list(lst)
    print(f"Reversed: {reversed_lst}")

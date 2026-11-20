"""
🟢 Linked List Cycle
Detect if a linked list has a cycle using Floyd's algorithm.

Time:  O(n)
Space: O(1)
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from utils import ListNode


def has_cycle(head: ListNode) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def detect_cycle_start(head: ListNode) -> ListNode:
    """Find the node where the cycle begins, or None."""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # cycle
    print(has_cycle(node1))  # True

    no_cycle = ListNode.from_list([1, 2, 3])
    print(has_cycle(no_cycle))  # False

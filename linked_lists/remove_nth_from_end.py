"""
🟡 Remove Nth Node From End of List
Remove the nth node from the end of a linked list in one pass.

Time:  O(n)
Space: O(1)
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from utils import ListNode


def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n + 1):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next


if __name__ == "__main__":
    lst = ListNode.from_list([1, 2, 3, 4, 5])
    result = remove_nth_from_end(lst, 2)
    print(result)  # 1 -> 2 -> 3 -> 5

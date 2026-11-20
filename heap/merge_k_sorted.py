"""
🔴 Merge K Sorted Lists
Merge k sorted linked lists into one sorted linked list.

Time:  O(N log k) where N is total elements, k is number of lists
Space: O(k) for the heap
"""
import heapq
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from utils import ListNode


def merge_k_lists(lists: list) -> ListNode:
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i, lst))

    dummy = ListNode(0)
    curr = dummy

    while heap:
        val, idx, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, idx, node.next))

    return dummy.next


def merge_k_lists_divide_conquer(lists: list) -> ListNode:
    """Divide and conquer approach."""
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]

    mid = len(lists) // 2
    left = merge_k_lists_divide_conquer(lists[:mid])
    right = merge_k_lists_divide_conquer(lists[mid:])

    return merge_two(left, right)


def merge_two(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 if l1 else l2
    return dummy.next


if __name__ == "__main__":
    lists = [
        ListNode.from_list([1, 4, 5]),
        ListNode.from_list([1, 3, 4]),
        ListNode.from_list([2, 6]),
    ]
    result = merge_k_lists(lists)
    print(result)  # 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

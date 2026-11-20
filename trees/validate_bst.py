"""
🟡 Validate Binary Search Tree
Determine if a binary tree is a valid BST.

Time:  O(n)
Space: O(h)
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from utils import TreeNode


def is_valid_bst(root: TreeNode) -> bool:
    def validate(node, low=float("-inf"), high=float("inf")):
        if not node:
            return True
        if node.val <= low or node.val >= high:
            return False
        return (validate(node.left, low, node.val) and
                validate(node.right, node.val, high))
    return validate(root)


def is_valid_bst_inorder(root: TreeNode) -> bool:
    prev = float("-inf")
    def inorder(node):
        nonlocal prev
        if not node:
            return True
        if not inorder(node.left):
            return False
        if node.val <= prev:
            return False
        prev = node.val
        return inorder(node.right)
    return inorder(root)


if __name__ == "__main__":
    valid = TreeNode.from_list([2, 1, 3])
    print(is_valid_bst(valid))  # True

    invalid = TreeNode.from_list([5, 1, 4, None, None, 3, 6])
    print(is_valid_bst(invalid))  # False

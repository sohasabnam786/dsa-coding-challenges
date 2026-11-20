"""
🟢 Balanced Binary Tree
Determine if a binary tree is height-balanced.

Time:  O(n)
Space: O(h)
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from utils import TreeNode


def is_balanced(root: TreeNode) -> bool:
    def check(node):
        if not node:
            return 0
        left = check(node.left)
        if left == -1:
            return -1
        right = check(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return check(root) != -1


if __name__ == "__main__":
    balanced = TreeNode.from_list([3, 9, 20, None, None, 15, 7])
    print(is_balanced(balanced))  # True

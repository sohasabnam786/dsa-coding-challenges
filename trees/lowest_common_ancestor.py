"""
🟡 Lowest Common Ancestor of a Binary Tree
Find the LCA of two nodes in a binary tree.

Time:  O(n)
Space: O(h)
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from utils import TreeNode


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root or root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left if left else right


def lca_bst(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """LCA in a Binary Search Tree."""
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
    return None


if __name__ == "__main__":
    tree = TreeNode.from_list([3, 5, 1, 6, 2, 0, 8])
    print(f"LCA: {tree.val}")

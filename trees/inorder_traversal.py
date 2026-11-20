"""
🟢 Binary Tree Inorder Traversal
Return the inorder traversal of a binary tree.

Time:  O(n)
Space: O(n)
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from utils import TreeNode


def inorder_recursive(root: TreeNode) -> list[int]:
    result = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)
    dfs(root)
    return result


def inorder_iterative(root: TreeNode) -> list[int]:
    result = []
    stack = []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right
    return result


if __name__ == "__main__":
    tree = TreeNode.from_list([1, None, 2, None, None, 3])
    print(inorder_recursive(tree))
    print(inorder_iterative(tree))

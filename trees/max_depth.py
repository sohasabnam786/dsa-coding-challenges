"""
🟢 Maximum Depth of Binary Tree
Find the maximum depth (height) of a binary tree.

Time:  O(n)
Space: O(h) where h is the height
"""
from collections import deque
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from utils import TreeNode


def max_depth_recursive(root: TreeNode) -> int:
    if not root:
        return 0
    return 1 + max(max_depth_recursive(root.left), max_depth_recursive(root.right))


def max_depth_bfs(root: TreeNode) -> int:
    if not root:
        return 0
    depth = 0
    queue = deque([root])
    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return depth


if __name__ == "__main__":
    tree = TreeNode.from_list([3, 9, 20, None, None, 15, 7])
    print(max_depth_recursive(tree))  # 3
    print(max_depth_bfs(tree))        # 3

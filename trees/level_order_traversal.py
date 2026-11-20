"""
🟡 Binary Tree Level Order Traversal
Return the level order traversal of a binary tree.

Time:  O(n)
Space: O(n)
"""
from collections import deque
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from utils import TreeNode


def level_order(root: TreeNode) -> list[list[int]]:
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


def zigzag_level_order(root: TreeNode) -> list[list[int]]:
    if not root:
        return []
    result = []
    queue = deque([root])
    left_to_right = True
    while queue:
        level = deque()
        for _ in range(len(queue)):
            node = queue.popleft()
            if left_to_right:
                level.append(node.val)
            else:
                level.appendleft(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(list(level))
        left_to_right = not left_to_right
    return result


if __name__ == "__main__":
    tree = TreeNode.from_list([3, 9, 20, None, None, 15, 7])
    print(level_order(tree))          # [[3], [9, 20], [15, 7]]
    print(zigzag_level_order(tree))   # [[3], [20, 9], [15, 7]]

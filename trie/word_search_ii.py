"""
🔴 Word Search II
Given a 2D board and a list of words, find all words that exist in the grid.

Time:  O(m * n * 4^L) where L is max word length
Space: O(total characters in all words)
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word

    rows, cols = len(board), len(board[0])
    result = []

    def dfs(r, c, node):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        char = board[r][c]
        if char not in node.children:
            return

        next_node = node.children[char]
        if next_node.word:
            result.append(next_node.word)
            next_node.word = None  # Avoid duplicates

        board[r][c] = "#"
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dfs(r + dr, c + dc, next_node)
        board[r][c] = char

        # Prune empty branches
        if not next_node.children:
            del node.children[char]

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root)

    return result


if __name__ == "__main__":
    board = [
        ["o","a","a","n"],
        ["e","t","a","e"],
        ["i","h","k","r"],
        ["i","f","l","v"]
    ]
    words = ["oath","pea","eat","rain"]
    print(find_words(board, words))  # ["oath", "eat"]

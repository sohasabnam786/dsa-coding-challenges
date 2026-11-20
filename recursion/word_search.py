"""
🟡 Word Search
Find if a word exists in a 2D grid of characters.

Time:  O(m * n * 4^L) where L is word length
Space: O(L) for recursion stack
"""


def exist(board: list[list[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])
    def backtrack(r, c, idx):
        if idx == len(word):
            return True
        if (r < 0 or r >= rows or c < 0 or c >= cols or
                board[r][c] != word[idx]):
            return False
        temp = board[r][c]
        board[r][c] = "#"
        found = (backtrack(r + 1, c, idx + 1) or
                 backtrack(r - 1, c, idx + 1) or
                 backtrack(r, c + 1, idx + 1) or
                 backtrack(r, c - 1, idx + 1))
        board[r][c] = temp
        return found

    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0):
                return True
    return False


if __name__ == "__main__":
    board = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    print(exist([row[:] for row in board], "ABCCED"))  # True
    print(exist([row[:] for row in board], "SEE"))     # True
    print(exist([row[:] for row in board], "ABCB"))    # False

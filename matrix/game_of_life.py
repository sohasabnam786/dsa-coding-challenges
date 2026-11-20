"""
🟡 Conway's Game of Life
Apply one step of Game of Life rules to a 2D grid.

Rules:
1. Live cell with < 2 live neighbors dies (underpopulation)
2. Live cell with 2-3 live neighbors lives
3. Live cell with > 3 live neighbors dies (overpopulation)
4. Dead cell with exactly 3 live neighbors becomes alive

Time:  O(m * n)
Space: O(1) in-place
"""


def game_of_life(board: list[list[int]]) -> None:
    """In-place solution using state encoding."""
    m, n = len(board), len(board[0])
    # States: 0=dead->dead, 1=live->live, 2=live->dead, 3=dead->live

    for i in range(m):
        for j in range(n):
            live_neighbors = count_live(board, i, j, m, n)

            if board[i][j] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    board[i][j] = 2  # Live -> Dead
            else:
                if live_neighbors == 3:
                    board[i][j] = 3  # Dead -> Live

    # Finalize states
    for i in range(m):
        for j in range(n):
            board[i][j] %= 2


def count_live(board, row, col, m, n):
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            r, c = row + dr, col + dc
            if 0 <= r < m and 0 <= c < n and board[r][c] in (1, 2):
                count += 1
    return count


if __name__ == "__main__":
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    print("Before:")
    for row in board:
        print(row)
    game_of_life(board)
    print("After:")
    for row in board:
        print(row)

"""
🔴 Sudoku Solver
Solve a 9x9 Sudoku puzzle using backtracking.

Time:  O(9^(empty cells))
Space: O(81) for the board
"""


def solve_sudoku(board: list[list[str]]) -> bool:
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                for num in "123456789":
                    if is_valid_placement(board, i, j, num):
                        board[i][j] = num
                        if solve_sudoku(board):
                            return True
                        board[i][j] = "."
                return False
    return True


def is_valid_placement(board, row, col, num):
    # Check row
    if num in board[row]:
        return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3x3 box
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False

    return True


def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        row = ""
        for j in range(9):
            if j % 3 == 0 and j != 0:
                row += "| "
            row += board[i][j] + " "
        print(row)


if __name__ == "__main__":
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    print("Before:")
    print_board(board)
    solve_sudoku(board)
    print("\nAfter:")
    print_board(board)

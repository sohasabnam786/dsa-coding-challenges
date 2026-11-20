"""
🔴 N-Queens Problem
Place n queens on an n x n chessboard so no two queens threaten each other.

Time:  O(n!)
Space: O(n^2)
"""


def solve_n_queens(n: int) -> list[list[str]]:
    solutions = []
    board = [["." for _ in range(n)] for _ in range(n)]

    cols = set()
    pos_diag = set()  # (row + col)
    neg_diag = set()  # (row - col)

    def backtrack(row):
        if row == n:
            solution = ["".join(r) for r in board]
            solutions.append(solution)
            return

        for col in range(n):
            if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                continue

            cols.add(col)
            pos_diag.add(row + col)
            neg_diag.add(row - col)
            board[row][col] = "Q"

            backtrack(row + 1)

            cols.remove(col)
            pos_diag.remove(row + col)
            neg_diag.remove(row - col)
            board[row][col] = "."

    backtrack(0)
    return solutions


def total_n_queens(n: int) -> int:
    """Just count the number of solutions."""
    return len(solve_n_queens(n))


if __name__ == "__main__":
    solutions = solve_n_queens(4)
    print(f"4-Queens has {len(solutions)} solutions:")
    for i, sol in enumerate(solutions):
        print(f"\nSolution {i + 1}:")
        for row in sol:
            print(f"  {row}")

    for n in range(1, 9):
        print(f"{n}-Queens: {total_n_queens(n)} solutions")

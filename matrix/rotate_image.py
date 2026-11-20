"""
🟡 Rotate Image
Rotate an n x n matrix 90 degrees clockwise in-place.

Time:  O(n^2)
Space: O(1)
"""


def rotate(matrix: list[list[int]]) -> None:
    n = len(matrix)
    # Transpose
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for row in matrix:
        row.reverse()


def rotate_ccw(matrix: list[list[int]]) -> None:
    """Rotate 90 degrees counter-clockwise."""
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    matrix.reverse()


if __name__ == "__main__":
    m = [[1,2,3],[4,5,6],[7,8,9]]
    print("Before:", m)
    rotate(m)
    print("After 90 CW:", m)  # [[7,4,1],[8,5,2],[9,6,3]]

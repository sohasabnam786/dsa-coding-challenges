"""
🟡 Spiral Matrix
Return all elements of a matrix in spiral order.

Time:  O(m * n)
Space: O(1) extra
"""


def spiral_order(matrix: list[list[int]]) -> list[int]:
    if not matrix:
        return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse right
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # Traverse down
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        # Traverse left
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        # Traverse up
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result


def generate_spiral(n: int) -> list[list[int]]:
    """Generate an n x n matrix filled in spiral order."""
    matrix = [[0] * n for _ in range(n)]
    top, bottom, left, right = 0, n - 1, 0, n - 1
    num = 1

    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            matrix[top][col] = num
            num += 1
        top += 1
        for row in range(top, bottom + 1):
            matrix[row][right] = num
            num += 1
        right -= 1
        if top <= bottom:
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1
        if left <= right:
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num
                num += 1
            left += 1

    return matrix


if __name__ == "__main__":
    m = [[1,2,3],[4,5,6],[7,8,9]]
    print(spiral_order(m))  # [1,2,3,6,9,8,7,4,5]
    spiral = generate_spiral(4)
    for row in spiral:
        print([f"{x:2}" for x in row])

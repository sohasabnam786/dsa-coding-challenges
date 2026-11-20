"""
🟡 Search a 2D Matrix
Search for a value in a sorted matrix efficiently.

Time:  O(log(m * n)) for sorted matrix, O(m + n) for row-col sorted
Space: O(1)
"""


def search_matrix(matrix: list[list[int]], target: int) -> bool:
    """Matrix where each row is sorted and first element > last of previous row."""
    if not matrix:
        return False

    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = (left + right) // 2
        val = matrix[mid // n][mid % n]

        if val == target:
            return True
        elif val < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


def search_matrix_ii(matrix: list[list[int]], target: int) -> bool:
    """Matrix where rows and columns are individually sorted."""
    if not matrix:
        return False

    row, col = 0, len(matrix[0]) - 1

    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1

    return False


if __name__ == "__main__":
    m1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    print(search_matrix(m1, 3))   # True
    print(search_matrix(m1, 13))  # False

    m2 = [[1,4,7,11],[2,5,8,12],[3,6,9,16],[10,13,14,17]]
    print(search_matrix_ii(m2, 5))   # True
    print(search_matrix_ii(m2, 20))  # False

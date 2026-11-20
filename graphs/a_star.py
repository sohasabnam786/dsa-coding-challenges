"""
🔴 A* Search Algorithm
Finds shortest path using heuristic-guided search.

Time:  O(E log V) with good heuristic
Space: O(V)
"""
import heapq


def a_star(grid: list[list[int]], start: tuple, end: tuple) -> list[tuple]:
    rows, cols = len(grid), len(grid[0])

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    open_set = [(heuristic(start, end), 0, start)]
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, cost, current = heapq.heappop(open_set)

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = current[0] + dr, current[1] + dc
            neighbor = (nr, nc)

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                new_g = g_score[current] + 1

                if neighbor not in g_score or new_g < g_score[neighbor]:
                    g_score[neighbor] = new_g
                    f_score = new_g + heuristic(neighbor, end)
                    heapq.heappush(open_set, (f_score, new_g, neighbor))
                    came_from[neighbor] = current

    return []  # No path found


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    path = a_star(grid, (0, 0), (4, 4))
    print(f"Path: {path}")
    print(f"Length: {len(path)}")

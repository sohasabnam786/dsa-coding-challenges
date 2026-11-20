"""
🟡 Breadth-First Search (BFS)
BFS traversal and shortest path in an unweighted graph.

Time:  O(V + E)
Space: O(V)
"""
from collections import deque


def bfs(graph: dict, start: str) -> list[str]:
    visited = set()
    queue = deque([start])
    visited.add(start)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order


def shortest_path(graph: dict, start: str, end: str) -> list[str]:
    if start == end:
        return [start]
    visited = {start}
    queue = deque([(start, [start])])
    while queue:
        node, path = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor == end:
                return path + [neighbor]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return []


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"], "B": ["A", "D", "E"],
        "C": ["A", "F"], "D": ["B"],
        "E": ["B", "F"], "F": ["C", "E"],
    }
    print(bfs(graph, "A"))
    print(shortest_path(graph, "A", "F"))

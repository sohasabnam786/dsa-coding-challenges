"""
🟡 Depth-First Search (DFS)
DFS traversal - iterative and recursive implementations.

Time:  O(V + E)
Space: O(V)
"""


def dfs_recursive(graph: dict, start: str) -> list[str]:
    visited = set()
    order = []
    def _dfs(node):
        visited.add(node)
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                _dfs(neighbor)
    _dfs(start)
    return order


def dfs_iterative(graph: dict, start: str) -> list[str]:
    visited = set()
    stack = [start]
    order = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
    return order


def has_path(graph: dict, start: str, end: str) -> bool:
    visited = set()
    def _dfs(node):
        if node == end:
            return True
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if _dfs(neighbor):
                    return True
        return False
    return _dfs(start)


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"], "B": ["A", "D", "E"],
        "C": ["A", "F"], "D": ["B"],
        "E": ["B", "F"], "F": ["C", "E"],
    }
    print(dfs_recursive(graph, "A"))
    print(dfs_iterative(graph, "A"))
    print(has_path(graph, "A", "F"))  # True

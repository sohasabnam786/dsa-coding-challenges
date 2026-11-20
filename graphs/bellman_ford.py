"""
🟡 Bellman-Ford Algorithm
Shortest paths from source, handles negative edges, detects negative cycles.

Time:  O(V * E)
Space: O(V)
"""


def bellman_ford(vertices: int, edges: list[tuple], source: int) -> tuple:
    distances = [float("inf")] * vertices
    distances[source] = 0
    predecessors = [-1] * vertices

    # Relax edges V-1 times
    for _ in range(vertices - 1):
        updated = False
        for u, v, w in edges:
            if distances[u] != float("inf") and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                predecessors[v] = u
                updated = True
        if not updated:
            break

    # Check for negative cycles
    for u, v, w in edges:
        if distances[u] != float("inf") and distances[u] + w < distances[v]:
            return None, None  # Negative cycle detected

    return distances, predecessors


def get_path(predecessors: list[int], target: int) -> list[int]:
    path = []
    node = target
    while node != -1:
        path.append(node)
        node = predecessors[node]
    path.reverse()
    return path


if __name__ == "__main__":
    edges = [
        (0, 1, 4), (0, 2, 5), (1, 2, -3),
        (2, 3, 4), (3, 1, -1),
    ]
    distances, preds = bellman_ford(4, edges, 0)
    if distances:
        print(f"Distances from 0: {distances}")
        for i in range(4):
            print(f"  Path to {i}: {get_path(preds, i)}")
    else:
        print("Negative cycle detected!")

    # Test negative cycle
    edges_neg = [(0, 1, 1), (1, 2, -1), (2, 0, -1)]
    result, _ = bellman_ford(3, edges_neg, 0)
    print(f"Negative cycle test: {'Detected!' if result is None else 'None'}")

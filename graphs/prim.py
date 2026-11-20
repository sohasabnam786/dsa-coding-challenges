"""
🟡 Prim's Minimum Spanning Tree
Find the MST using a greedy approach with a priority queue.

Time:  O(E log V)
Space: O(V + E)
"""
import heapq
from collections import defaultdict


def prim(num_vertices: int, edges: list[tuple]) -> tuple:
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))

    visited = set()
    mst = []
    total_weight = 0
    pq = [(0, 0, -1)]  # (weight, vertex, from_vertex)

    while pq and len(visited) < num_vertices:
        weight, u, from_v = heapq.heappop(pq)
        if u in visited:
            continue

        visited.add(u)
        total_weight += weight
        if from_v != -1:
            mst.append((from_v, u, weight))

        for w, v in graph[u]:
            if v not in visited:
                heapq.heappush(pq, (w, v, u))

    return mst, total_weight


if __name__ == "__main__":
    edges = [
        (0, 1, 4), (0, 7, 8), (1, 2, 8), (1, 7, 11),
        (2, 3, 7), (2, 8, 2), (2, 5, 4), (3, 4, 9),
        (3, 5, 14), (4, 5, 10), (5, 6, 2), (6, 7, 1),
        (6, 8, 6), (7, 8, 7),
    ]
    mst, weight = prim(9, edges)
    print(f"MST edges: {mst}")
    print(f"Total weight: {weight}")  # 37

"""
🟡 Dijkstra's Shortest Path Algorithm
Find shortest paths from a source vertex to all other vertices in a weighted graph.

Time:  O((V + E) log V) with binary heap
Space: O(V)
"""
import heapq
from collections import defaultdict


def dijkstra(graph: dict, start: str) -> dict:
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    predecessors = {node: None for node in graph}
    pq = [(0, start)]

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)

        if curr_dist > distances[curr_node]:
            continue

        for neighbor, weight in graph[curr_node]:
            distance = curr_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = curr_node
                heapq.heappush(pq, (distance, neighbor))

    return distances, predecessors


def shortest_path(graph: dict, start: str, end: str) -> tuple:
    distances, predecessors = dijkstra(graph, start)
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = predecessors[node]
    path.reverse()

    if distances[end] == float("inf"):
        return float("inf"), []
    return distances[end], path


if __name__ == "__main__":
    graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("D", 3), ("C", 1)],
        "C": [("B", 1), ("D", 5)],
        "D": [("E", 2)],
        "E": [],
    }
    distances, _ = dijkstra(graph, "A")
    print(f"Distances from A: {distances}")

    dist, path = shortest_path(graph, "A", "E")
    print(f"Shortest path A->E: {path} (distance: {dist})")

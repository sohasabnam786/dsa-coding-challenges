"""
🟡 Floyd-Warshall Algorithm
All-pairs shortest paths. Works with negative edges (no negative cycles).

Time:  O(V^3)
Space: O(V^2)
"""


def floyd_warshall(graph: list[list[float]]) -> list[list[float]]:
    n = len(graph)
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


def has_negative_cycle(dist: list[list[float]]) -> bool:
    for i in range(len(dist)):
        if dist[i][i] < 0:
            return True
    return False


if __name__ == "__main__":
    INF = float("inf")
    graph = [
        [0,   3,   INF, 7],
        [8,   0,   2,   INF],
        [5,   INF, 0,   1],
        [2,   INF, INF, 0],
    ]

    result = floyd_warshall(graph)
    print("All-pairs shortest distances:")
    for row in result:
        print([f"{x:4}" if x != INF else " INF" for x in row])

    print(f"Has negative cycle: {has_negative_cycle(result)}")

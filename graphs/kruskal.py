"""
🟡 Kruskal's Minimum Spanning Tree
Find the MST using a greedy approach with Union-Find.

Time:  O(E log E)
Space: O(V)
"""


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True


def kruskal(num_vertices: int, edges: list[tuple]) -> tuple:
    edges_sorted = sorted(edges, key=lambda x: x[2])
    uf = UnionFind(num_vertices)
    mst = []
    total_weight = 0

    for u, v, w in edges_sorted:
        if uf.union(u, v):
            mst.append((u, v, w))
            total_weight += w
            if len(mst) == num_vertices - 1:
                break

    return mst, total_weight


if __name__ == "__main__":
    edges = [
        (0, 1, 4), (0, 7, 8), (1, 2, 8), (1, 7, 11),
        (2, 3, 7), (2, 8, 2), (2, 5, 4), (3, 4, 9),
        (3, 5, 14), (4, 5, 10), (5, 6, 2), (6, 7, 1),
        (6, 8, 6), (7, 8, 7),
    ]
    mst, weight = kruskal(9, edges)
    print(f"MST edges: {mst}")
    print(f"Total weight: {weight}")  # 37

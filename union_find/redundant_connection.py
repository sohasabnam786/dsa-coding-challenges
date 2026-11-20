"""
🟡 Redundant Connection
Find the edge that, when removed, makes the graph a tree.

Time:  O(n * alpha(n))
Space: O(n)
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


def find_redundant_connection(edges: list[list[int]]) -> list[int]:
    n = len(edges)
    uf = UnionFind(n + 1)

    for u, v in edges:
        if not uf.union(u, v):
            return [u, v]

    return []


if __name__ == "__main__":
    print(find_redundant_connection([[1,2],[1,3],[2,3]]))           # [2, 3]
    print(find_redundant_connection([[1,2],[2,3],[3,4],[1,4],[1,5]]))  # [1, 4]

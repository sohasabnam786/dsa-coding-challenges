"""
🟡 Union-Find (Disjoint Set Union)
Data structure for tracking disjoint sets with path compression and union by rank.

Time:  O(alpha(n)) per operation (nearly O(1))
Space: O(n)
"""


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n
        self.components = n

    def find(self, x: int) -> int:
        """Find with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """Union by rank. Returns True if merged, False if already connected."""
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        self.size[px] += self.size[py]

        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1

        self.components -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def component_size(self, x: int) -> int:
        return self.size[self.find(x)]

    def num_components(self) -> int:
        return self.components


if __name__ == "__main__":
    uf = UnionFind(10)
    connections = [(0, 1), (1, 2), (3, 4), (5, 6), (6, 7), (0, 5)]
    for u, v in connections:
        uf.union(u, v)
        print(f"Union({u},{v}) -> {uf.num_components()} components")

    print(f"\n0 connected to 7? {uf.connected(0, 7)}")
    print(f"0 connected to 3? {uf.connected(0, 3)}")
    print(f"Component size of 0: {uf.component_size(0)}")

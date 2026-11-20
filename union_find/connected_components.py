"""
🟡 Number of Connected Components
Find the number of connected components in an undirected graph.

Time:  O(V + E * alpha(V))
Space: O(V)
"""


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        self.count -= 1


def count_components(n: int, edges: list[list[int]]) -> int:
    uf = UnionFind(n)
    for u, v in edges:
        uf.union(u, v)
    return uf.count


def count_components_dfs(n: int, edges: list[list[int]]) -> int:
    """DFS approach for comparison."""
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    count = 0

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    for i in range(n):
        if i not in visited:
            dfs(i)
            count += 1

    return count


if __name__ == "__main__":
    print(count_components(5, [[0,1],[1,2],[3,4]]))          # 2
    print(count_components(5, [[0,1],[1,2],[2,3],[3,4]]))    # 1
    print(count_components_dfs(5, [[0,1],[1,2],[3,4]]))      # 2

"""
🟡 Topological Sort (Kahn's Algorithm)
Topological ordering of a directed acyclic graph (DAG).

Time:  O(V + E)
Space: O(V)
"""
from collections import deque, defaultdict


def topological_sort(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    graph = defaultdict(list)
    in_degree = [0] * num_courses
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return order if len(order) == num_courses else []


def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    return len(topological_sort(num_courses, prerequisites)) == num_courses


if __name__ == "__main__":
    print(topological_sort(4, [[1,0],[2,0],[3,1],[3,2]]))
    print(can_finish(2, [[1,0]]))       # True
    print(can_finish(2, [[1,0],[0,1]])) # False (cycle)

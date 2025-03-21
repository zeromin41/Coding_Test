import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

queue = deque([i for i in range(1, n + 1) if indegree[i] == 0])
result = []

while queue:
    node = queue.popleft()
    result.append(node)
    for neighbor in graph[node]:
        indegree[neighbor] -= 1
        if indegree[neighbor] == 0:
            queue.append(neighbor)

print(*result)
from sys import stdin
from collections import deque

f_input = lambda : stdin.readline().rstrip()
N, M, V = map(int, f_input().split())

graph = dict()
for i in range(N):
    graph[i + 1] = []

for _ in range(M):
    start, end = map(int, f_input().split())

    # 간선은 양방향
    graph[start].append(end)
    graph[end].append(start)

for val in graph.values():
    val.sort()

# DFS
stack = deque([V])
visited = list()
while len(stack) > 0:
    node = stack.pop()
    if node not in visited:
        visited.append(node)
    for candidate in graph[node][::-1]:
        if candidate not in visited:
            stack.append(candidate)
print(" ".join(map(str, visited)))

# BFS
queue = deque([V])
visited.clear()
while len(queue) > 0:
    node = queue.popleft()
    if node not in visited:
        visited.append(node)
    for candidate in graph[node]:
        if candidate not in visited:
            queue.append(candidate)
print(" ".join(map(str, visited)))

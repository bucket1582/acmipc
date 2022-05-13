from sys import stdin
from collections import deque

f_input = lambda : stdin.readline().rstrip()

n, m = map(int, f_input().split())
graph = {}

for _ in range(m):
    a, b = map(int, f_input().split())
    from_a_to = graph.setdefault(a, [])
    from_a_to.append(b)
    from_b_to = graph.setdefault(b, [])
    from_b_to.append(a)

cnt = 0
visited = [False for _ in range(n)]
stack = deque()
while not all(visited):
    idx = 0
    while visited[idx]:
        idx += 1
    stack.append(idx + 1)
    while len(stack) > 0:
        node = stack.pop()
        if visited[node - 1]:
            continue
        visited[node - 1] = True
        for next_node in graph.get(node, []):
            stack.append(next_node)
    cnt += 1
    stack.clear()
print(cnt)

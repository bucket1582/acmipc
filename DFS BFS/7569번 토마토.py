from sys import stdin
from collections import deque

f_input = lambda : stdin.readline().rstrip()

n, m = map(int, f_input().split())

table = []
visited = []
q = deque()
for row_idx in range(m):
    row = list(map(int, f_input().split()))
    for col_idx in range(n):
        if row[col_idx] == 1:
            q.append((row_idx, col_idx))
    table.append(row)
    visited.append([False for _ in range(n)])

depth = 0
while True:
    for _ in range(len(q)):
        node = q.popleft()
        if visited[node[0]][node[1]]:
            continue
        visited[node[0]][node[1]] = True
        if table[node[0]][node[1]] == -1:
            continue
        table[node[0]][node[1]] = 1
        if node[0] > 0:
            q.append((node[0] - 1, node[1]))
        if node[1] > 0:
            q.append((node[0], node[1] - 1))
        if node[0] < m - 1:
            q.append((node[0] + 1, node[1]))
        if node[1] < n - 1:
            q.append((node[0], node[1] + 1))
    if len(q) == 0:
        break
    depth += 1

ripe_flag = True
for row in table:
    for ele in row:
        if ele == 0:
            ripe_flag = False
if ripe_flag:
    print(depth - 1)
else:
    print(-1)

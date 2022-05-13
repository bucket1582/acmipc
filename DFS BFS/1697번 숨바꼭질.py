from sys import stdin
from collections import deque

f_input = lambda : stdin.readline().rstrip()

n, k = map(int, f_input().split())

q = deque([n])
visited = [False for _ in range(100001)]
depth = 0
greater_min = -1
while True:
    for _ in range(len(q)):
        loc = q.popleft()
        if loc < 0:
            continue
        if loc > k:
            if greater_min < 0:
                greater_min = depth + loc - k
            else:
                greater_min = min(greater_min, depth + loc - k)
            continue
        if visited[loc]:
            continue
        visited[loc] = True
        if loc < n:
            q.append(loc - 1)
            q.append(2 * loc)
            continue
        if loc == k:
            break
        q.append(loc - 1)
        q.append(loc + 1)
        q.append(2 * loc)
    if loc == k:
        break
    if len(q) == 0:
        break
    depth += 1
if loc == k:
    if greater_min < 0:
        print(depth)
    else:
        print(min(depth, greater_min))
else:
    print(greater_min)

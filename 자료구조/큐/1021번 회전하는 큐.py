from collections import deque
from sys import stdin

f_input = lambda : stdin.readline().rstrip()
n, m = map(int, f_input().split())
q = deque(t for t in range(1, n + 1))

want_to_remove = deque(map(int, f_input().split()))

num_of_rot = 0
while len(want_to_remove) > 0:
    target = want_to_remove.popleft()
    idx = q.index(target)
    q_len = len(q)

    if idx <= (q_len // 2):
        for _ in range(idx + 1):
            e = q.popleft()
            if e == target:
                break
            q.append(e)
            num_of_rot += 1
    else:
        for _ in range(idx + 1):
            e = q.pop()
            q.appendleft(e)
            num_of_rot += 1
            if e == target:
                q.popleft()
                break
print(num_of_rot)

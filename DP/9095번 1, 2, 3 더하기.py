from sys import stdin

f_input = lambda : stdin.readline().rstrip()

t = int(f_input())
p = [1, 2, 4]
for _ in range(t):
    n = int(f_input())

    for i in range(len(p) + 1, n + 1):
        p.append(p[-3] + p[-2] + p[-1])
    print(p[n - 1])

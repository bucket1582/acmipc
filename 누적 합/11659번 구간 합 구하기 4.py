from sys import stdin

f_input = lambda : stdin.readline().rstrip()

n, m = map(int, f_input().split())
lst = list(map(int, f_input().split()))
for i in range(1, n):
    lst[i] += lst[i - 1]
for _ in range(m):
    i, j = map(int, f_input().split())
    if i > 1:
        print(lst[j - 1] - lst[i - 2])
    else:
        print(lst[j - 1])

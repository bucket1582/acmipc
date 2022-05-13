from sys import stdin

m, n = map(int, stdin.readline().rstrip().split())
str_set = set()
for _ in range(m):
    str_set.add(stdin.readline().rstrip())
cnt = 0
for _ in range(n):
    inq = stdin.readline().rstrip()
    if inq in str_set:
        cnt += 1
print(cnt)

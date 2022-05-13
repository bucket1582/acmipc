from sys import stdin

f_input = lambda: stdin.readline().rstrip()

f_input()
a = set(map(int, f_input().split()))
b = set(map(int, f_input().split()))

union = a.union(b)
intersect = a.intersection(b)

print(len(union) - len(intersect))

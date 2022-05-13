def can_be_in_a_box(w, h, x):
    return x**2 <= w**2 + h**2

from sys import stdin

n, w, h = map(int, stdin.readline().rstrip().split())
for _ in range(n):
    print("DA" if can_be_in_a_box(w, h, int(stdin.readline().rstrip())) else "NE")

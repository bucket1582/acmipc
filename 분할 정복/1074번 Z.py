def visit(r, c, n):
    # base case
    if n == 1:
        if r == 0:
            if c == 0:
                return 0
            return 1
        if c == 0:
            return 2
        return 3

    group_num = None
    if r < pow(2, n - 1):
        if c < pow(2, n - 1):
            group_num = 0
        else:
            group_num = 1
            c -= pow(2, n - 1)
    else:
        if c < pow(2, n - 1):
            group_num = 2
            r -= pow(2, n - 1)
        else:
            group_num = 3
            r -= pow(2, n - 1)
            c -= pow(2, n - 1)
    return group_num * pow(2, 2 * n - 2) + visit(r, c, n - 1)

from sys import stdin

f_input = lambda : stdin.readline().rstrip()

n, r, c = map(int, f_input().split())
print(visit(r, c, n))

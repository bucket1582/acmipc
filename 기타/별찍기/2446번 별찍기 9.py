n = int(input())
max_star = 2 * n - 1
for i in range(n, 0, -1):
    blk = " " * (n - i)
    star = "*" * (2 * i - 1)
    print(blk + star)
for i in range(2, n + 1):
    blk = " " * (n - i)
    star = "*" * (2 * i - 1)
    print(blk + star)

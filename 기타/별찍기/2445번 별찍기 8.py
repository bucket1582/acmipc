n = int(input())

for i in range(1, n):
    star = "*" * i
    blk = " " * (2 * n - 2 * i)
    print(star + blk + star)
for i in range(n, 0, -1):
    star = "*" * i
    blk = " " * (2 * n - 2 * i)
    print(star + blk + star)

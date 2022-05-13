def count_below_x(x, n):
    i = 1
    cnt = 0
    while pow(i, 2) <= x:
        cnt += min(n - i, x // i - i) * 2 + 1
        i += 1
    return cnt


from sys import stdin

f_input = lambda : stdin.readline().rstrip()
n = int(f_input())
k = int(f_input())

min_val = 1
max_val = k
while max_val > min_val:
    mid_val = (max_val + min_val) // 2
    cnt = count_below_x(mid_val, n)
    if cnt < k:
        # k보다 적은 것이므로, 더 많아져야 한다.
        min_val = mid_val + 1
    else:
        # k보다 크거나 같은 것이므로 더 적어져야 한다.
        max_val = mid_val

print(min_val)
        

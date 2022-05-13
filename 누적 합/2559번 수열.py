from sys import stdin

f_input = lambda : stdin.readline().rstrip()

n, k = map(int, f_input().split())
seq = list(map(int, f_input().split()))

moving_sum = [sum(seq[:k])]
max_val = moving_sum[0]
for i in range(k, n):
    sum_val = moving_sum[-1] - seq[i - k] + seq[i]
    moving_sum.append(sum_val)
    if sum_val > max_val:
        max_val = sum_val
print(max_val)

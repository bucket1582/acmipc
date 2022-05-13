import sys

f_input = lambda : sys.stdin.readline().rstrip()
N = int(f_input())
data = list(map(lambda x : int(x), f_input().split()))

con_sum = [0, 0]
for i in range(N):
    val = data[i]
    # 1. 앞에 있는 것을 더하지 않은 것
    con_sum.append(val)
    # 2. 앞에 있는 것을 더한 것
    con_sum.append(max(con_sum[2 * i] + val, con_sum[2 * i + 1] + val))
print(max(con_sum[2:]))

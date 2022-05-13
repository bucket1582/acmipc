def choose_2(n):
    return n * (n - 1) // 2


from sys import stdin

f_input = lambda : stdin.readline().rstrip()

n, m = map(int, f_input().split())

seq = list(map(int, f_input().split()))
coset = dict()  # 잉여류 - 개수 매핑
latest_coset = seq[0] % m
coset[latest_coset] = 1
for i in range(1, n):
    latest_coset = latest_coset + seq[i] % m
    latest_coset %= m
    if latest_coset in coset:
        coset[latest_coset] += 1
    else:
        coset[latest_coset] = 1

# 정답 구하기
cnt = 0
for key, val in coset.items():
    if key == 0:
        # 잉여류가 0이면, 그 자체도 m으로 나누어떨어진다.
        # 즉, 1개 뽑는 경우의 수 + 2개 뽑는 경우의 수
        cnt += val
    cnt += choose_2(val)
print(cnt)

from sys import stdin

f_input = lambda : stdin.readline().rstrip()

n = int(f_input())

if n < 10:
    ans = [1 for _ in range(n + 1)] + [0 for _ in range(n + 1, 10)]
else:
    ans = [1 for _ in range(10)]
    pow_10_idx = 1
    while 10 ** (pow_10_idx + 1) < n:
        for digit in range(10):
           # 새로운 자리가 추가될 때마다 1 ~ 9 에 대해 같은 구조 반복
           # 새로 추가된 자리도 카운팅
           ans[digit] += 9 * ans[digit] + 10 ** pow_10_idx - 1
        pow_10_idx += 1
    
ans[0] -= 1 # base case에서 제거
print(" ".join(map(str, ans)))

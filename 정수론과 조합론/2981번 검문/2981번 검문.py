from sys import stdin
import math

f_input = lambda: stdin.readline()

def factorize_and_map_to_string(n):
    factors = []
    for i in range(2, n + 1):
        if n % i == 0:
            factors.append(str(i))
    return factors

N = int(f_input())

delta = list() # 차이를 저장할 리스트
latest = 0 # 가장 최근 값
for _ in range(N):
    new = int(f_input()) # 입력 받기
    if latest != 0:
        delta.append(new - latest)
    latest = new

gcd = math.gcd(*delta)
factors = factorize_and_map_to_string(gcd)
print(' '.join(factors))

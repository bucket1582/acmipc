import sys

MEMOI = dict()
def count_stairs(N, starting_with):
    # 길이가 N이고
    # starting_with로 시작하는 계단 수 개수
    
    # N이 1이면
    if N == 1:
        # Starting with, 즉 시작 수가 있으므로 1로 고정
        return 1

    # 메모이제이션
    if (N, starting_with) in MEMOI:
        return MEMOI[(N, starting_with)]

    # 0 핸들링
    if starting_with == 0:
        # 길이가 N - 1이고 1로 시작하는 계단 수의 개수와 같다.
        val = count_stairs(N - 1, 1)
        MEMOI[(N, starting_with)] = val
        return val
    # 9 핸들링
    elif starting_with == 9:
        # 길이가 N - 1이고 8로 시작하는 계단 수의 개수와 같다.
        val = count_stairs(N - 1, 8)
        MEMOI[(N, starting_with)] = val
        return val
    # 나머지는 공통적
    else:
        # 길이 N - 1
        # starting_with + 1과 starting_with - 1 검사
        # 2개 개수 합
        val = count_stairs(N - 1, starting_with - 1) + count_stairs(N - 1, starting_with + 1)
        MEMOI[(N, starting_with)] = val
        return val
    
f_input = lambda : sys.stdin.readline().rstrip()

N = int(f_input())

summation = 0
# 첫 수가 0이 될 수는 없다.
for i in range(1, 10):
    summation += count_stairs(N, i) % 1000000000
print(summation % 1000000000)

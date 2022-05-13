import sys

MEMOI = dict()
def lis(n = 0, prev = 0):
    global sequence

    # 초과 시에는 0
    if n >= length:
        return 0

    if (n, prev) in MEMOI:
        return MEMOI[(n, prev)]

    num = sequence[n]
    # num이 prev보다 클 때
    if num > prev:
        # 선택하냐 안 하냐 그것이 문제로다
        val_choose = 1 + lis(n + 1, num)
        val_not_choose = lis(n + 1, prev)
        val = max(val_choose, val_not_choose)
        MEMOI[(n, prev)] = val
        return val
    else:
        # 선택 기회조차 없다
        val = lis(n + 1, prev)
        MEMOI[(n, prev)] = val
        return val
        

# 빠른 입력
f_input = lambda : sys.stdin.readline().rstrip()

# 데이터 파싱
length = int(f_input())
sequence = list(map(lambda x : int(x), f_input().split()))
c = lis()
print(c)

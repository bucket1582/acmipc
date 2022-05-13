import sys

MEMOI = dict()
def make_one(N):
    # N이 1과 같으면 완성!
    if N == 1:
        return 0

    # 메모이제이션
    if N in MEMOI:
        return MEMOI[N]

    # 4가지 경우
    # 1. % 6 == 0
    # 2. % 3 == 0
    # 3. % 2 == 0
    # 4. 6과 서로소
    
    # % 6 == 0
    if N % 6 == 0:
        # 3으로 나눠본다.
        div_3 = 1 + make_one(N // 3)

        # 2로 나눠본다.
        div_2 = 1 + make_one(N // 2)

        # 1을 빼 본다.
        sub_1 = 1 + make_one(N - 1)

        # 최소 시행을 찾고 기억한다.
        val = min(div_3, div_2, sub_1)
        MEMOI[N] = val
        return val
    # % 3 == 0
    elif N % 3 == 0:
        # 3으로 나눠본다.
        div_3 = 1 + make_one(N // 3)

        # 1을 빼 본다.
        sub_1 = 1 + make_one(N - 1)

        # 최소 시행을 찾고 기억한다.
        val = min(div_3, sub_1)
        MEMOI[N] = val
        return val
    # % 2 == 0
    elif N % 2 == 0:
        # 2로 나눠본다.
        div_2 = 1 + make_one(N // 2)

        # 1을 빼 본다.
        sub_1 = 1 + make_one(N - 1)

        # 최소 시행을 찾고 기억한다.
        val = min(div_2, sub_1)
        MEMOI[N] = val
        return val
    else:
        # 1을 빼 본다.
        sub_1 = 1 + make_one(N - 1)

        # 최소 시행을 찾고 기억한다.
        val = sub_1
        MEMOI[N] = val
        return val

f_input = lambda : sys.stdin.readline().rstrip()
N = int(f_input())
print(make_one(N))

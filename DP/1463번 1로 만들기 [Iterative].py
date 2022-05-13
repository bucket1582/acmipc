import sys

f_input = lambda : sys.stdin.readline().rstrip()

MEMOI = {1:1, 2:1, 3:1}
N = int(f_input())

for i in range(1, N + 1):
    # 이미 이번 수를 만드는 방법은 알려져있다
    num_compute = MEMOI[i]

    # 1을 더해본다
    add_1 = i + 1
    # 그게 있으면
    if add_1 in MEMOI:
        # 뭐가 더 최소인지 보고 바꾼다.
        MEMOI[add_1] = min(MEMOI[add_1], num_compute + 1)
    else:
        MEMOI[add_1] = num_compute + 1

    # 2를 곱해본다
    mul_2 = i * 2
    # 그게 있으면
    if mul_2 in MEMOI:
        # 뭐가 더 최소인지 보고 바꾼다.
        MEMOI[mul_2] = min(MEMOI[mul_2], num_compute + 1)
    else:
        MEMOI[mul_2] = num_compute + 1

    # 3을 곱해본다.
    mul_3 = i * 3
    # 그게 있으면
    if mul_3 in MEMOI:
        # 뭐가 더 최소인지 보고 바꾼다.
        MEMOI[mul_3] = min(MEMOI[mul_3], num_compute + 1)
    else:
        MEMOI[mul_3] = num_compute + 1
print(MEMOI[N])

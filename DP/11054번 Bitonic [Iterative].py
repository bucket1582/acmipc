import sys

# 빠른 입력
f_input = lambda : sys.stdin.readline().rstrip()

# 데이터 파싱
length = int(f_input())
sequence = list(map(lambda x : int(x), f_input().split()))

lis = []
for i in range(length):
    # 초기화
    # 이번 수로 시작하는 증가수열
    lis.append(1)
    # 이번 수로 시작하는 감소 수열
    lis.append(1)
    for j in range(2 * i):
        # j가 2로 나누어떨어지면, 증가를 유지하고 있는 수열
        if j % 2 == 0:
            # 증가 유지 가능?
            if sequence[j // 2] < sequence[i]:
                # 증가 수열 길이 업데이트
                lis[2 * i] = max(lis[j] + 1, lis[2 * i])
            elif sequence[j // 2] > sequence[i]:
                # 감소 수열 길이 업데이트
                lis[2 * i + 1] = max(lis[j] + 1, lis[2 * i + 1])
        # 이미 감소하고 있는 수열
        else:
            if sequence[j // 2] > sequence[i]:
                lis[2 * i + 1] = max(lis[j] + 1, lis[2 * i + 1])
print(max(lis))

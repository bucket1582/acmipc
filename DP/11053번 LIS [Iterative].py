import sys

# 빠른 입력
f_input = lambda : sys.stdin.readline().rstrip()

# 데이터 파싱
length = int(f_input())
sequence = list(map(lambda x : int(x), f_input().split()))

lis = []
for i in range(length):
    # 초기화
    lis.append(1)
    for j in range(i):
        if sequence[j] < sequence[i]:
            # sequence[j]로 끝나는 증가 수열에 이 수를 붙인 수열의 길이와
            # 현재 이 수로 끝나는 증가 수열의 길이를 비교,
            # 더 큰 것을 증가 수열의 길이로 한다.
            lis[i] = max(lis[i], lis[j] + 1)
print(max(lis))

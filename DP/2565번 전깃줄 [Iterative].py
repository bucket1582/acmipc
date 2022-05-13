import sys

# 빠른 입력
f_input = lambda : sys.stdin.readline().rstrip()

# 데이터 파싱
num_lines = int(f_input())
lines = dict()
keys = []
for _ in range(num_lines):
    x, y = map(lambda x : int(x), f_input().split())
    lines[x] = y
    keys.append(x)

# O(n log n)
keys.sort()

# A에 있는 전깃줄의 넘버를 순차적으로 불러왔을 때, -> 이 때문에 sorting이 필요
# B에 있는 전깃줄 넘버가 증가하면 된다.

lis = []
for i in range(num_lines):
    # 초기화
    # 이번 수로 시작하는 증가수열 (정확히는 이 수 하나밖에 없는 수열의 길이)
    lis.append(1)
    for j in range(i):
        # 이전 전깃줄 넘버
        prev_key = keys[j]

        # 현재 전깃줄 넘버
        cur_key = keys[i]
        
        # 증가하고 있으면 뒤에 붙일 수 있다
        if lines[prev_key] < lines[cur_key]:
            lis[i] = max(lis[j] + 1, lis[i])
# 자르는 개수
print(num_lines - max(lis))

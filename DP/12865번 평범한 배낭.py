import sys

f_input = lambda : sys.stdin.readline().rstrip()
n, k = map(lambda x : int(x), f_input().split())

# 데이터 파싱
obj = []
for _ in range(n):
    obj.append(tuple(map(lambda x : int(x), f_input().split())))

# Buttom - Up DP
sack = [0 for _ in range(k + 1)]
for i in range(n):
    weight, value = obj[i]

    # 이번 물품을 고려한 가방 싸기
    new_sack = []
    for w in range(k + 1):
        # 1. 가방 한도 초과; 넣을 수 없다면
        # 이전 최적해를 그대로 답습한다
        if w < weight:
            new_sack.append(sack[w])
            continue

        # 2. 가방 한도 초과 아님; 넣을 수 있다
        # 최적해를 새로 계산한다
        # 최적해는 이 물품을 넣을 수 있도록 물품을 뺀 후 이 물품을 넣은 것의 가치와
        # 안 넣은 해 둘 중 가치가 더 큰 것이 된다
        val_instead = sack[w - weight] + value
        val_original = sack[w]
        new_sack.append(max(val_instead, val_original))
    # 최적해 업데이트
    sack = new_sack
print(max(sack))

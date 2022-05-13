import sys

# 빠른 입력
f_input = lambda : sys.stdin.readline().rstrip()

# 데이터 파싱
cups = int(f_input())
wine = []
for _ in range(cups):
    wine.append(int(f_input()))

# Iterative Method for DP
MEMOI = dict()

for cup in range(cups):
    # 이번 컵에 들어있는 와인의 양
    drink = wine[cup]

    # 최초 리셋
    MEMOI[(cup, 0)] = 0
    MEMOI[(cup, 1)] = drink
    
    # (컵, 연속으로 마신 잔 수)
    # 0L 들어있는 잔 때문에 연속 0잔 마셨을 수도 있다.
    if (cup - 1, 0) in MEMOI:
        MEMOI[(cup, 0)] = max(MEMOI[(cup, 0)], MEMOI[(cup - 1, 0)])
        MEMOI[(cup, 1)] = MEMOI[(cup - 1, 0)] + drink
    if (cup - 1, 1) in MEMOI:
        MEMOI[(cup, 0)] = max(MEMOI[(cup, 0)], MEMOI[(cup - 1, 1)])
        MEMOI[(cup, 2)] = MEMOI[(cup - 1, 1)] + drink
    if (cup - 2, 0) in MEMOI:
        MEMOI[(cup, 0)] = max(MEMOI[(cup, 0)], MEMOI[(cup - 2, 0)])
        MEMOI[(cup, 1)] = max(MEMOI[(cup - 2, 0)] + drink, MEMOI[(cup, 1)])
    if (cup - 2, 1) in MEMOI:
        MEMOI[(cup, 0)] = max(MEMOI[(cup, 0)], MEMOI[(cup - 2, 1)])
        MEMOI[(cup, 1)] = max(MEMOI[(cup - 2, 1)] + drink, MEMOI[(cup, 1)])
    if (cup - 2, 2) in MEMOI:
        MEMOI[(cup, 0)] = max(MEMOI[(cup, 0)], MEMOI[(cup - 2, 2)])
        MEMOI[(cup, 1)] = max(MEMOI[(cup - 2, 2)] + drink, MEMOI[(cup, 1)])

# 최댓값 찾기
search_for = [
    (cups - 1, 0),
    (cups - 1, 1),
    (cups - 1, 2),
    (cups - 2, 0),
    (cups - 2, 1),
    (cups - 2, 2)
]
maxima = 0
for search in search_for:
    if search in MEMOI and maxima < MEMOI[search]:
        maxima = MEMOI[search]
print(maxima)

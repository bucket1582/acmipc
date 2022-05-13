from sys import stdin

f_input = lambda: stdin.readline().rstrip()

weight_cnt = int(f_input())
weights = list(map(int, f_input().split()))

marble_cnt = int(f_input())
marbles = list(map(int, f_input().split()))

BIAS = 40000
avail = [False for _ in range(-40000, 40001)] # 추로 해당 무게를 만드는 것이 가능한가?
avail[0 + BIAS] = True

max_avail = 0
min_avail = 0
for weight in weights:
    new_avail = avail[:] # avail이 업데이트 되면서 꼬이는 것 방지
    for avail_idx in range(min_avail, max_avail + 1):
        # 해당 무게가 만들어질 수 없는 것이었다면, 논하지 않는다.
        if not avail[BIAS + avail_idx]:
            continue

        # print(f"Current Searching: {avail_idx}, weight: {weight}")
        # 만들어질 수 있었다면 (이전까지) 그러면, weight를 합한 것도 만들 수 있다.
        new_avail[BIAS + avail_idx + weight] = True
        if avail_idx + weight > max_avail:
            max_avail = avail_idx + weight # 탐색 영역 확장

        new_avail[BIAS + avail_idx - weight] = True
        if avail_idx - weight < min_avail:
            min_avail = avail_idx - weight
    avail = new_avail[:]

print(" ".join(map(lambda x: "Y" if avail[BIAS + x] else "N", marbles)))

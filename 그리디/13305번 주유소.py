# Handling Input
input()

road_length = input().split()
road_length = [int(l) for l in road_length]

oil_price = input().split()
oil_price = [int(p) for p in oil_price]

cost = 0
least_price = oil_price[0]

# 그대로 가다가 더 싸질 때만 바꾼다.
for idx in range(len(road_length)):
    cost += least_price * road_length[idx]

    # 최저가 갱신
    if oil_price[idx + 1] < least_price:
        least_price = oil_price[idx + 1]
print(cost)

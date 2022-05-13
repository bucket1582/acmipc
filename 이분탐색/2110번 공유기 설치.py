def is_able_to_install(house_loc, distance, count):
    # 첫 집에는 무조건 설치한다.
    x_prev = house_loc[0]
    count -= 1
    for house_x in house_loc[1:]:
        dist = house_x - x_prev
        # print(f"{x_prev} -> {house_x}, distance = {dist}; install : {dist >= distance}")
        if dist < distance:
            continue
        x_prev = house_x
        count -= 1
        if count <= 0:
            break
    return count <= 0

from sys import stdin

f_input = lambda : stdin.readline().rstrip()

n, c = map(int, f_input().split())
max_x = 0
min_x = -1
house = []
for _ in range(n):
    x = int(f_input())
    if min_x == -1 or min_x > x:
        min_x = x
    if max_x < x:
        max_x = x
    house.append(x)
house.sort()

max_search = (max_x - min_x + 1) // (c - 1)
min_search = 1
# print(f"Search through {min_search} to {max_search}")

while min_search < max_search:
    search_distance = (min_search + max_search) // 2
    # print(f"Inquires {search_distance}")
    is_able = is_able_to_install(house, search_distance, c)
    if not is_able:
        max_search = search_distance
    else:
        min_search = search_distance + 1

final_able = is_able_to_install(house, min_search, c)
if final_able:
    print(min_search)
else:
    print(min_search - 1)

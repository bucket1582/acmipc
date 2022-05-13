MAX_HEIGHT = 256
BREAK_TIME = 2
FILLING_TIME = 1


def is_possible(inventory, std_height, block_file):
    remainders = inventory
    for block_height in block_file:
        # 블록 사용
        if block_height < std_height:
            remainders -= std_height - block_height
        # 블록 저장
        else:
            remainders += block_height - std_height
    # 블록이 남아야 가능한 경우임
    return remainders >= 0

    

def compute_time(block_file, std_height):
    total_time = 0
    for block_height in block_file:
        # 더 낮으면 채우기
        if block_height < std_height:
            total_time += (std_height - block_height) * FILLING_TIME
        # 더 높으면 덜어내기
        else:
            total_time += (block_height - std_height) * BREAK_TIME
    return total_time
    

n, _, inventory = map(int, input().split())

block_file = []
for _ in range(n):
    block_file += map(int, input().split())

answer = tuple()
for height in range(MAX_HEIGHT + 1):
    if not is_possible(inventory, height, block_file):
        continue
    time = compute_time(block_file, height)

    if (len(answer) == 0) or (time <= answer[0]):
        answer = (time, height)

print(f"{answer[0]} {answer[1]}")

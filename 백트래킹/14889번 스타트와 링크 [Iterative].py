from time import time
def addOne(start, already):
    global is_chosen
    # 겹치지 않는 값이 될 때까지 +1
    start += 1
    while start in already:
        start += 1
    return start

def addOneIdx(lst, idx):
    # 리스트 인덱스에 대해 addOne
    lst[idx] = addOne(lst[idx], lst[:idx] + lst[idx + 1:])

def resetIdx(lst, idx):
    # 리스트 인덱스 리셋
    lst[idx] = addOne(lst[idx-1], lst[:idx] + lst[idx + 1:])
    
# 데이터 파싱
N = int(input())

s = time()
# 능력치 데이터 가져오기
table = []
for _ in range(N):
    raw = input().split()
    table.append([int(x) for x in raw])

# 능력치의 차의 최솟값을 저장;
min_diff = -1

# link 팀에 속하는지
is_chosen = [False for _ in range(N)]

# 링크 팀 초기화
link = [t for t in range(N // 2)]
for x in link:
    is_chosen[x] = True
    
while True:
    # 능력치 차 계산
    abilityA = 0
    abilityB = 0
    for playerA in range(N):
        if is_chosen[playerA]:
            for playerB in range(playerA + 1, N):
                if is_chosen[playerB]:
                    abilityA += table[playerA][playerB] + table[playerB][playerA]    
        else:
            for playerB in range(playerA + 1, N):
                if not is_chosen[playerB]:
                    abilityB += table[playerA][playerB] + table[playerB][playerA]

    # 최소 능력치차 업데이트
    if min_diff == -1:
        min_diff = abs(abilityA - abilityB)
    else:
        diff = abs(abilityA - abilityB)
        if diff < min_diff:
            min_diff = diff
            
    # 백트래킹
    # 뒤부터 업데이트
    for i in range(N // 2 - 1, -1, -1):
        is_chosen[link[i]] = False # 원래 있었던 선수 퇴출
        addOneIdx(link, i)
        if link[i] <= N // 2 + i:
            is_chosen[link[i]] = True # 새 선수 영입
            break

    # 끝날 조건
    if link[0] > N // 2:
        break

    # 업데이트 된 대상들 초기화
    for j in range(i + 1, N // 2):
        resetIdx(link, j)
        is_chosen[link[j]] = True # 새 선수 영입
print(min_diff)
print(time() - s)


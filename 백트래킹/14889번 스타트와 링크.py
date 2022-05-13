from time import time
def computeAbilityDiff(team):
    global table, is_chosen, N
    abilityA = 0
    abilityB = 0
    for i in range(N):
        if is_chosen[i]:
            for j in range(i + 1, N):
                if not is_chosen[j]:
                    continue
                abilityA += table[i][j] + table[j][i]
        else:
            for j in range(i + 1, N):
                if is_chosen[j]:
                    continue
                abilityB += table[i][j] + table[j][i]
            
    return abs(abilityA - abilityB)

def backtrack(team):
    global is_chosen
    # 빈 팀이면 그대로 반환
    if len(team) == 0:
        return team
    
    # 마지막으로 뽑은 사람 퇴출
    last_person = team.pop(-1)
    is_chosen[last_person] = False
    return team

def teaming(team = []):
    global min_diff, is_chosen, N
    if len(team) >= N // 2:
        if min_diff == -1:
            min_diff = computeAbilityDiff(team)
        else:
            diff = computeAbilityDiff(team)
            if diff < min_diff:
                min_diff = diff
        return backtrack(team)

    for i in range(len(team), N):
        # 이미 뽑혔으면 스킵
        if is_chosen[i]:
            continue

        # 안 뽑혔으면 일단 팀 짜 봐~
        team.append(i)
        is_chosen[i] = True
        team = teaming(team)

    # 모든 팀 짜 봤어? 그럼 백트래킹
    return backtrack(team)
    

# 데이터 파싱
N = int(input())

# 능력치 데이터 가져오기
table = []
for _ in range(N):
    raw = input().split()
    table.append([int(x) for x in raw])

is_chosen = [False for _ in range(N)]

# 능력치의 차의 최솟값을 저장;
min_diff = -1

s = time()
teaming()
print(time() - s)
print(min_diff))


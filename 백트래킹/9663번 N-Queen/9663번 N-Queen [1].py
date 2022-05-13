from time import time
def putQueen1(loc, n, atk):
    # 기준
    stdLine = loc // n # 행
    stdColumn = loc % n # 열

    # 직선 공격
    for i in range(n * n):
        # i의 위치; 행과 열
        line = i // n
        column = i % n

        # 행이나 열이 기준과 같으면 공격받는 위치
        if (line == stdLine) or (column == stdColumn):
            atk.add(i)

    # 대각선 공격
    # 좌상
    idx = loc
    while not ((idx // n == 0) or (idx % n == 0)):
        idx -= n + 1
        atk.add(idx)

    # 우상
    idx = loc
    while not ((idx // n == 0) or (idx % n == n - 1)):
        idx -= n - 1
        atk.add(idx)

    # 좌하
    idx = loc
    while not ((idx // n == n - 1) or (idx % n == 0)):
        idx += n - 1
        atk.add(idx)

    # 우하
    idx = loc
    while not ((idx // n == n - 1) or (idx % n == n - 1)):
        idx += n + 1
        atk.add(idx)

    return atk


def putQueen2(loc, n, atk):
    # 기준
    stdLine = loc // n # 행
    stdColumn = loc % n # 열
    
    for i in range(n * n):
        # i의 위치; 행과 열
        line = i // n
        column = i % n

        # 행이나 열, 대각선이 기준과 같으면 공격받는 위치
        if (line == stdLine) or (column == stdColumn) or \
           (line - stdLine == column - stdColumn) or (line - stdLine == stdColumn - column):
            atk.add(i)
            
    return atk


def putQueen(loc, n, atk):
    return putQueen1(loc, n, atk)

n = int(input())

count = 0
queens = []
loc = -1

place_time = 0
search_time = 0
judge_time = 0
place_new_time = 0
back_time = 0
while True:
    # 초기화
    atk = set()

    tmp = time()
    # 현재 놓여있는 퀸 모두 배치 계산
    for queen in queens:
        atk = putQueen(queen, n, atk)
    place_time += time() - tmp

    # 백트래킹
    # 더 이상 놓는게 불가능해질 때까지 무지성 퀸 놓기
    # 마지막으로 탐색한 위치 이후만 본다
    tmp = time()
    if n * n - len(atk) >= n - len(queens):
        judge_time += time() - tmp
        for i in range(loc + 1, n * n):
            tmp = time()
            # 그 위치가 불가능할 위치일 경우 고려하지 않는다
            if i in atk:
                search_time += time() - tmp
                continue
            search_time += time() - tmp

            tmp = time()
            # 새로운 퀸 배치
            newQueen = i
            atk = putQueen(newQueen, n, atk)
            queens.append(newQueen)
            place_new_time += time() - tmp

            # 이번 행에 퀸 하나를 배치하면, 이번 행은 탐색이 끝나므로, 다음행 바로 직전으로 옮긴다
            line = i // n
            i = (line + 1) * n - 1

            tmp = time()
            # 더 이상 놓을 수 없을 경우, 놓지 않고 Iteration을 끝낸다
            if n * n - len(atk) < n - len(queens):
                judge_time += time() - tmp
                break
            judge_time += time() - tmp

            # 퀸을 배치했더니 n개 메이드 -> count 1 더하고, Iteration 종료
            if len(queens) == n:
                count += 1
                break

    # 끝나는 조건; 아무 퀸도 추가할 수 없을 때 또는, 첫번째 퀸이 1번 줄을 벗어날 때
    if  len(queens) == 0 or queens[0] > n - 1:
        break
    
    tmp = time()
    # 마지막 항목 제거 (불가능하므로)
    loc = queens.pop(-1)
    back_time += time() - tmp

print(count)
print(f"* Time\n* queen 배치 시간 : {format(place_time, '.3f')}\n* i 탐색 시간 : {format(search_time, '.3f')}\n" +
      f"* 종료 판단 시간 : {format(judge_time, '.3f')}\n* 새 queen 배치 시간 : {format(place_new_time, '.3f')}\n" +
      f"* 마지막 항목 제거 시간 : {format(back_time, '.3f')}\n" +
      f"* 총 시간 (대략) : {format(place_time + search_time + judge_time + place_new_time + back_time, '.3f')}")
        

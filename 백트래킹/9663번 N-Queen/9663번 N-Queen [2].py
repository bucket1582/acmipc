from time import time
def putQueen(loc, n, atk):
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
            atk.append(i)
            
    return atk


def removeQueen(loc, n, atk):
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
            if i in atk:
                atk.remove(i)
            
    return atk


n = int(input())

count = 0
queens = []
atk = []
loc = -1

place_time = 0
search_time = 0
judge_time = 0
place_new_time = 0
back_time = 0
while True:
    # 백트래킹
    # 더 이상 놓는게 불가능해질 때까지 무지성 퀸 놓기
    # 마지막으로 탐색한 위치 이후만 본다
    for i in range(loc + 1, n * n):
        tmp = time()
        # 그 위치가 불가능할 위치일 경우 고려하지 않는다
        if i in atk:
            search_time += time() - tmp
            continue
        search_time += time() - tmp

        tmp = time()
        # 더 이상 놓을 수 없을 경우, 놓지 않고 Iteration을 끝낸다
        if n * n - len(set(atk)) < n - len(queens):
            judge_time += time() - tmp
            break
        judge_time += time() - tmp

        tmp = time()
        # 새로운 퀸 배치
        newQueen = i
        atk = putQueen(newQueen, n, atk)
        queens.append(newQueen)
        place_new_time += time() - tmp

        # 퀸을 배치했더니 n개 메이드 -> count 1 더하고, Iteration 종료
        if len(queens) == n:
            count += 1
            break
        
    # 끝나는 조건; 아무 퀸도 추가할 수 없을 때
    if len(queens) == 0:
        break

    tmp = time()
    # 마지막 항목 제거 (불가능하므로)
    loc = queens.pop(-1)
    atk = removeQueen(loc, n, atk)
    back_time += time() - tmp

print(count)
print(f"* Time\n* queen 배치 시간 : {format(place_time, '.3f')}\n* i 탐색 시간 : {format(search_time, '.3f')}\n" +
      f"* 종료 판단 시간 : {format(judge_time, '.3f')}\n* 새 queen 배치 시간 : {format(place_new_time, '.3f')}\n" +
      f"* 마지막 항목 제거 시간 : {format(back_time, '.3f')}\n" +
      f"* 총 시간 (대략) : {format(place_time + search_time + judge_time + place_new_time + back_time, '.3f')}")
        

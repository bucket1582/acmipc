from time import time
def isUnderDiagAttack(queens, line, col):
    # 대각 판단
    for i in range(len(queens)):
        # 합 혹은 차가 같으면 대각
        if (i + queens[i] == line + col) or \
           (i - queens[i] == line - col):
            return True
    return False

def putQueen(queens = []):
    global count, n
    # 지금까지 놓은 퀸의 개수가 곧 행
    line = len(queens)

    # n개 이상 놓았으면, 성공
    if line >= n:
        count += 1
        return queens[:-1]

    # Iteration : 열
    for i in range(n):
        # 놓을 수 있는지 판단 
        # 이전 퀸이 이미 차지한 열이면 건너뛰기
        if i in queens:
            continue
        # 이전 퀸이 이미 차지한 대각이면 건너뛰기
        if isUnderDiagAttack(queens, line, i):
            continue
        
        # 가능한 위치; 퀸 놓고 다음행으로 진행
        queens.append(i)
        queens = putQueen(queens)
        
    # 해당 행의 모든 칸에 퀸을 놓아보았음; 이전 행으로 돌아감.
    return queens[:-1]

n = int(input())
s = time()
count = 0
putQueen()
print(count)
print(time() - s)

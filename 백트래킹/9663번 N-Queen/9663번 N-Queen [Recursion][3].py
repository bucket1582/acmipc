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
    global count, dataset, n
    # 지금까지 놓은 퀸의 개수가 곧 행
    line = len(queens)

    # n개 이상 놓았으면, 성공
    if line >= n:
        count += 1
        dataset.pop(-1)
        return queens[:-1]

    # Iteration : 열
    for i in dataset[-1]:
        # 놓을 수 있는지 판단 
        # 이전 퀸이 이미 차지한 열이면 건너뛰기
        col = [t for t in range(n)]
        if i in queens:
            col.remove(i)
            continue
        # 이전 퀸이 이미 차지한 대각이면 건너뛰기
        if isUnderDiagAttack(queens, line, i):
            continue
        
        # 가능한 위치; 퀸 놓고 다음행으로 진행
        queens.append(i)
        if i == 0:
            try:
                col.remove(0)
                col.remove(1)
            except:
                ...
        elif i == n - 1:
            try:
                col.remove(n - 1)
                col.remove(n - 2)
            except:
                ...
        else:
            try:
                col.remove(i)
                col.remove(i + 1)
                col.remove(i - 1)
            except:
                ...
        dataset.append(col)
        queens = putQueen(queens)
        
    # 해당 행의 모든 칸에 퀸을 놓아보았음; 이전 행으로 돌아감.
    dataset.pop(-1)
    return queens[:-1]

n = int(input())
s = time()
count = 0
dataset = [[t for t in range(n)]]
putQueen()
print(count)
print(time() - s)

def isUnderAttack(col, ldiag, rdiag):
    # 공격받는 칸인지 판단
    global columnChecker, leftDiagChecker, rightDiagChecker
    # 셋 중 하나라도 True면 놓을 수 없음
    return columnChecker[col] or leftDiagChecker[ldiag] or rightDiagChecker[rdiag]

def blockRegion(col, ldiag, rdiag):
    # 위치 막기
    global columnChecker, leftDiagChecker, rightDiagChecker
    columnChecker[col] = True
    leftDiagChecker[ldiag] = True
    rightDiagChecker[rdiag] = True

def openRegion(col, ldiag, rdiag):
    # 위치 열기
    global columnChecker, leftDiagChecker, rightDiagChecker
    columnChecker[col] = False
    leftDiagChecker[ldiag] = False
    rightDiagChecker[rdiag] = False

def backtrack(queens):
    # 빈 리스트면 바로 리턴
    if len(queens) == 0:
        return []
    
    # 마지막 퀸의 좌표 찾기
    col = queens.pop(-1)
    line = len(queens)

    # 위치 열기
    openRegion(col, line + col, line - col + n - 1)

    # 리턴
    return queens

def putQueen(queens = []):
    global count, n
    # 지금까지 놓은 퀸의 개수가 곧 행
    line = len(queens)

    # n개 이상 놓았으면, 성공
    if line >= n:
        count += 1
        return backtrack(queens)

    # Iteration : 열
    for i in range(n):
        # 놓을 수 있는지 판단
        # 열: i
        # 좌하향 대각선: 행과 열의 합; line + i
        # 우하향 대각선: 행과 열의 차 + n - 1; line - i + n - 1
        if isUnderAttack(i, line + i, line - i + n - 1):
            continue
        
        # 가능한 위치
        queens.append(i) # 퀸 놓기

        # 열, 좌하향 대각선, 우하향 대각선 막기
        blockRegion(i, line + i, line - i + n - 1)

        # 다음행 진행
        queens = putQueen(queens)
        
    # 해당 행의 모든 칸에 퀸을 놓아보았음; 이전 행으로 돌아감.
    return backtrack(queens)

n = int(input())
count = 0

# True면 해당 위치에 Queen이 있음
# 열 체크 : n개
columnChecker = [False for _ in range(n)]
# 좌하향 대각선 체크 : 2n - 1개; 합이 보존 됨; 합 0 ~ 2n - 2
leftDiagChecker = [False for _ in range(2 * n - 1)]
# 우하향 대각선 체크 : 2n - 1개; 차가 보존 됨; 차 -n + 1 ~ n - 1
rightDiagChecker = [False for _ in range(2 * n - 1)]

putQueen()
print(count)

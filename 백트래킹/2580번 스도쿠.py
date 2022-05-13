def marking(line, col, val):
    # 마킹
    global lines, columns, boxes
    # 행과 열 처리
    lines[line][val - 1] = True
    columns[col][val - 1] = True

    # 박스 처리
    boxes[line // 3 * 3 + col // 3][val - 1] = True

def unmarking(line, col, val):
    # 마킹 풀기
    global lines, columns, boxes
    # 행과 열 처리
    lines[line][val - 1] = False
    columns[col][val - 1] = False

    # 박스 처리
    boxes[line // 3 * 3 + col // 3][val - 1] = False

def isBlocked(line, col, val):
    # 마킹 되어 있는지 확인
    global lines, columns
    return lines[line][val - 1] or columns[col][val - 1] or boxes[line // 3 * 3 + col // 3][val - 1]

def sudokuSolve(solution = []):
    global sol2coords
    # 차자따!
    if len(solution) >= len(sol2coords):
        return solution

    # 좌표 불러오기
    line, col = sol2coords[len(solution)]
    for i in range(1, 10):
        # 해당 숫자를 기입할 수 없으면, 스킵
        if isBlocked(line, col, i):
            continue

        # 기입 가능한 숫자; 숫자 기입
        solution.append(i)

        # 숫자 블로킹
        marking(line, col, i)

        # 해답에 추가
        sudoku = sudokuSolve(solution)
        # 차자따!
        if len(solution) >= len(sol2coords):
            return solution
    # 못 차자따 ㅠㅠ
    if len(solution) == 0:
        return []
    val = solution.pop(-1)
    line, col = sol2coords[len(solution)]
    unmarking(line, col, val)
    return solution
        
def buildSudoku(solution, problem):
    global sol2coords
    lineStrings = problem.split('\n')
    sudoku = []
    for lineString in lineStrings:
        line = lineString.split()
        sudoku.append(line)

    for i in range(len(solution)):
        line, col = sol2coords[i]
        sudoku[line][col] = str(solution[i])
    sudoku = sudoku[:-1]
    return '\n'.join(' '.join(line) for line in sudoku)


# 데이터 파싱        
# 수 존재 마킹
lines = [[False for _ in range(9)] for _ in range(9)]
columns = [[False for _ in range(9)] for _ in range(9)]
boxes = [[False for _ in range(9)] for _ in range(9)]
'''
박스 인덱스
0 1 2
3 4 5
6 7 8
'''

sol2coords = [] # solution idx -> 좌표 (i, j) 매핑
problem = "" # 문제 상황 기억
for i in range(9):
    raw = input()
    problem += raw + '\n'
    raw = raw.split()
    line = [int(x) for x in raw]
    for j in range(9):
        if line[j] != 0:
            # 0이 아니면, 해당 수의 존재 마킹
            marking(i, j, line[j])
        else:
            # 0이면, 그 위치를 기억해 둔다
            sol2coords.append((i, j))

# 문제 해결
solution = sudokuSolve()
answer = buildSudoku(solution, problem)
print(answer)

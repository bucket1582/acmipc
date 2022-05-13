def parseOperators(operators):
    global a
    calculation = a[0]
    for i in range(len(operators)):
        # 덧셈
        if operators[i] == 0:
            calculation += a[i + 1]
        # 뺄셈
        elif operators[i] == 1:
            calculation -= a[i + 1]
        # 곱셈
        elif operators[i] == 2:
            calculation *= a[i + 1]
        # 나눗셈
        else:
            # C++과 파이썬의 나눗셈 규칙이 다르다!
            # 음수 나눗셈
            if calculation * a[i + 1] < 0:
                absolute = abs(calculation) // abs(a[i + 1])
                calculation = -absolute
            else:
                calculation //= a[i + 1]
    return calculation

def backtrack(operators):
    global oper
    # 만약에 비어있으면, 빈 리스트 그대로
    if len(operators) == 0:
        return operators
    
    # 마지막으로 사용했던 연산자를 다시 원위치로
    last_operator = operators.pop(-1)
    oper[last_operator] += 1

    # 나머지 리턴
    return operators
 
def calculate(operators = []):
    global a, oper, max_depth, results
    if len(operators) >= max_depth:
        calculation = parseOperators(operators)
        results.append(calculation)
        return backtrack(operators)

    for i in range(4):
        # 해당 연산자를 모두 소진했을 경우
        if oper[i] <= 0:
            continue

        # 아니면 무지성 사용
        operators.append(i)
        oper[i] -= 1
        operators = calculate(operators)
        
    # 다 사용했으면?
    return backtrack(operators)

# 데이터 파싱
# N -> 필요 없음
input()

# 숫자 집합
raw = input().split()
a = [int(x) for x in raw]

# 연산자 개수
raw = input().split()
oper = [int(x) for x in raw]

# 최대 깊이
max_depth = len(a) - 1

# 모든 연산 결과 저장
results = []

# 계산하기
calculate()

print(max(results))
print(min(results))

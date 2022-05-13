import sys
MEMOI = dict()
def climbing_stairs(n = 0, gap = 1):
    global stairs, T

    if (n, gap) in MEMOI:
        return MEMOI[(n, gap)]
    
    # 최종 계단 2칸 전에는 무조건 2칸을 뛰어야 한다.
    if n == T - 3:
        return stairs[n] + stairs[n + 2]
    # 최종 계단 1칸 전에는 무조건 1칸을 뛰어야 한다.
    if n == T - 2:
        return stairs[n] + stairs[n + 1]
    # 최종 계단에서는 끝난다; 그러나 논리적으로 이 부분은 호출되지 않는다.
    if n == T - 1:
        return stairs[n]

    if gap == 1:
        common = stairs[n]
        val = climbing_stairs(n + 1, 2)
        MEMOI[(n, gap)] = common + val
        return common + val
    else:
        common = stairs[n]
        val1 = climbing_stairs(n + 2, 1)
        val2 = climbing_stairs(n + 2, 2)
        res = max(common + val1, common + val2)
        MEMOI[(n, gap)] = res
        return res


# 빠른 입력
f_input = lambda : sys.stdin.readline().rstrip()

# 계단 개수
T = int(f_input())

# 데이터 파싱
stairs = []
for _ in range(T):
    stairs.append(int(f_input()))

# 1개 있을 때 특수
if T == 1:
    print(stairs[0])
# 2개 있을 때 역시 특수
elif T == 2:
    print(stairs[0] + stairs[1])
# 3개 있을 때까지 특수
elif T == 3:
    print(max(stairs[0] + stairs[2], stairs[1] + stairs[2]))
else:
    # 처음에는 2번 연속 1칸 올라가는 것이 가능하다.
    step_first_one = climbing_stairs(n = 0, gap = 1)
    step_first_two = climbing_stairs(n = 0, gap = 2)
    skip_first_one = climbing_stairs(n = 1, gap = 1)
    skip_first_two = climbing_stairs(n = 1, gap = 2)
    print(max(step_first_one, step_first_two, skip_first_one, skip_first_two))

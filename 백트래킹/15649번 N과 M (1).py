def addOne(start, already):
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
    lst[idx] = addOne(0, lst[:idx] + lst[idx + 1:])
    
    
raw = input().split()
n, m = int(raw[0]), int(raw[1])

permut = [t + 1 for t in range(m)]
while True:
    print(' '.join(str(x) for x in permut))

    # 백트래킹
    # 뒤부터 업데이트
    for i in range(m - 1, -1, -1):
        addOneIdx(permut, i)
        if permut[i] <= n:
            break

    # 끝날 조건
    if permut[0] > n:
        break

    # 업데이트 된 대상들 초기화
    for j in range(i + 1, m):
        resetIdx(permut, j)

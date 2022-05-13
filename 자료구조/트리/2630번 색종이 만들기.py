from sys import stdin

def check_all_0_or_1(table):
    all_0 = True
    all_1 = True
    for row in table:
        for cell in row:
            if cell != 0:
                all_0 = False
            if cell != 1:
                all_1 = False
    if all_0:
        return 0
    if all_1:
        return 1
    return -1


def cut_paper(table, n):
    checker = check_all_0_or_1(table)
    if checker == 0:
        return (1, 0)
    if checker == 1:
        return (0, 1)

    lu = [row[:n // 2] for row in table[:n // 2]]
    ru = [row[n // 2:] for row in table[:n // 2]]
    ld = [row[:n // 2] for row in table[n // 2:]]
    rd = [row[n // 2:] for row in table[n // 2:]]

    lu_ans = cut_paper(lu, n // 2)
    ru_ans = cut_paper(ru, n // 2)
    ld_ans = cut_paper(ld, n // 2)
    rd_ans = cut_paper(rd, n // 2)
    ans = (lu_ans[0] + ru_ans[0] + ld_ans[0] + rd_ans[0], \
           lu_ans[1] + ru_ans[1] + ld_ans[1] + rd_ans[1])
    return ans
    

f_input = lambda : stdin.readline().rstrip()

N = int(f_input())
table = []
for _ in range(N):
    table.append(list(map(int, f_input().split())))
ans = cut_paper(table, N)
print(ans[0])
print(ans[1])

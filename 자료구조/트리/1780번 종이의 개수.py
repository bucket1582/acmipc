from sys import stdin

def check_all_0_or_1_or_m_1(table):
    all_0 = True
    all_1 = True
    all_m_1 = True
    for row in table:
        for cell in row:
            if cell != 0:
                all_0 = False
            if cell != 1:
                all_1 = False
            if cell != -1:
                all_m_1 = False
    if all_0:
        return 0
    if all_1:
        return 1
    if all_m_1:
        return -1
    return -2


def cut_paper(table, n):
    checker = check_all_0_or_1_or_m_1(table)
    if checker == 0:
        return (0, 1, 0)
    if checker == 1:
        return (0, 0, 1)
    if checker == -1:
        return (1, 0, 0)

    third = n // 3
    two_third = 2 * third

    lu = [row[:third] for row in table[:third]]
    mu = [row[third:two_third] for row in table[:third]]
    ru = [row[two_third:] for row in table[:third]]
    lc = [row[:third] for row in table[third:two_third]]
    mc = [row[third:two_third] for row in table[third:two_third]]
    rc = [row[two_third:] for row in table[third:two_third]] 
    ld = [row[:third] for row in table[two_third:]]
    md = [row[third:two_third] for row in table[two_third:]]
    rd = [row[two_third:] for row in table[two_third:]]

    ans = [0, 0, 0]
    for part in [lu, mu, ru, lc, mc, rc, ld, md, rd]:
        part_ans = cut_paper(part, n // 3)
        ans[0] += part_ans[0]
        ans[1] += part_ans[1]
        ans[2] += part_ans[2]

    return ans
    

f_input = lambda : stdin.readline().rstrip()

N = int(f_input())
table = []
for _ in range(N):
    table.append(list(map(int, f_input().split())))
ans = cut_paper(table, N)
print(ans[0])
print(ans[1])
print(ans[2])

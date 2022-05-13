def check_all_1(table):
    for row in table:
        for ele in row:
            if ele == 0:
                return False
    return True

def ripe(table, n, m):
    not_ripe_flag = True
    std = deepcopy(table)
    for row_idx in range(m):
        for col_idx in range(n):
            if std[row_idx][col_idx] == 1:
                if row_idx > 0:
                    if std[row_idx - 1][col_idx] == 0:
                        table[row_idx - 1][col_idx] = 1
                        not_ripe_flag = False
                if row_idx < m - 1:
                    if std[row_idx + 1][col_idx] == 0:
                        table[row_idx + 1][col_idx] = 1
                        not_ripe_flag = False
                if col_idx > 0:
                    if std[row_idx][col_idx - 1] == 0:
                        table[row_idx][col_idx - 1] = 1
                        not_ripe_flag = False
                if col_idx < n - 1:
                    if std[row_idx][col_idx + 1] == 0:
                        table[row_idx][col_idx + 1] = 1
                        not_ripe_flag = False
    return not_ripe_flag

def deepcopy(table):
    new_table = []
    for row in table:
        new_table.append([ele for ele in row])
    return new_table

from sys import stdin

f_input = lambda : stdin.readline().rstrip()

n, m = map(int, f_input().split())

table = []
for _ in range(m):
    row = list(map(int, f_input().split()))
    table.append(row)

days = 0
while not check_all_1(table):
    not_ripe = ripe(table, n, m)
    if not_ripe:
        days = -1
        break
    days += 1
print(days)

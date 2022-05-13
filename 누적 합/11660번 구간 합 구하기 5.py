from sys import stdin

f_input = lambda : stdin.readline().rstrip()

n, m = map(int, f_input().split())

sum_matrix = []
for i in range(n):
    sum_row = []
    row_sum = 0
    row = list(map(int, f_input().split()))
    for j in range(n):
        row_sum += row[j]
        if i == 0:
            sum_row.append(row_sum)
        else:
            sum_row.append(row_sum + sum_matrix[-1][j])
    sum_matrix.append(sum_row)

for _ in range(m):
    x1, y1, x2, y2 = map(lambda x : int(x) - 1, f_input().split())
    if x1 == 0 and y1 == 0:
        print(sum_matrix[x2][y2])
    elif x1 == 0:
        print(sum_matrix[x2][y2] - sum_matrix[x2][y1 - 1])
    elif y1 == 0:
        print(sum_matrix[x2][y2] - sum_matrix[x1 - 1][y2])
    else:
        print(sum_matrix[x2][y2] - sum_matrix[x2][y1 - 1] -\
              sum_matrix[x1 - 1][y2] + sum_matrix[x1 - 1][y1 - 1])
        

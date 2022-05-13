def compute_cell(matrix_a, matrix_b, row_idx, col_idx, m):
    cell = 0
    for i in range(m):
        cell += matrix_a[row_idx][i] * matrix_b[i][col_idx]
    return cell


from sys import stdin

f_input = lambda : stdin.readline().rstrip()

n, m = map(int, f_input().split())

matrix_a = []
for _ in range(n):
    row = list(map(int, f_input().split()))
    matrix_a.append(row)

m, k = map(int, f_input().split())
matrix_b = []
for _ in range(m):
    row = list(map(int, f_input().split()))
    matrix_b.append(row)

matrix_mul = []
for i in range(n):
    row = []
    for j in range(k):
        row.append(compute_cell(matrix_a, matrix_b, i, j, m))
    matrix_mul.append(row)
    
for row in matrix_mul:
    print(" ".join(map(str, row)))
    

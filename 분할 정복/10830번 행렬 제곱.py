def compute_cell(matrix_a, matrix_b, row_idx, col_idx, m, remainder):
    cell = 0
    for i in range(m):
        cell += matrix_a[row_idx][i] % remainder * matrix_b[i][col_idx] % remainder % remainder
    return cell

def matrix_mul(matrix_a, matrix_b, n, m, k, remainder):
    matrix_mul = []
    for i in range(n):
        row = []
        for j in range(k):
            row.append(compute_cell(matrix_a, matrix_b, i, j, m, remainder) % remainder)
        matrix_mul.append(row)
    return matrix_mul

def fast_matrix_pow(matrix, power, n, remainder):
    if power == 0:
        identity = []
        for i in range(n):
            row = [0 for _ in range(n)]
            row[i] = 1
            identity.append(row)
        return identity
    if power == 1:
        return matrix
    if power % 2 == 0:
        sqrt_matrix = fast_matrix_pow(matrix, power // 2, n, remainder)
        return matrix_mul(sqrt_matrix, sqrt_matrix, n, n, n, remainder)
    sqrt_matrix = fast_matrix_pow(matrix, (power - 1) // 2, n, remainder)
    return matrix_mul(matrix_mul(sqrt_matrix, sqrt_matrix, n, n, n, remainder), matrix, n, n, n, remainder)
            
def refine(matrix, remainder):
    ans_matrix = []
    for row in matrix:
        ans_row = []
        for cell in row:
            ans_row.append(cell % remainder)
        ans_matrix.append(ans_row)
    return ans_matrix



from sys import stdin

f_input = lambda : stdin.readline().rstrip()

n, b = map(int, f_input().split())

matrix = []
for _ in range(n):
    row = list(map(int, f_input().split()))
    matrix.append(row)

matrix = fast_matrix_pow(matrix, b, n, 1000)
matrix = refine(matrix, 1000)
for row in matrix:
    print(" ".join(map(str, row)))

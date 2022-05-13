from sys import stdin

f_input = lambda: stdin.readline().rstrip()

n = int(f_input())
matrix_size = []
for _ in range(n):
    matrix_size.append(tuple(map(int, f_input().split())))

matrix_mul_time = [[-1 for _ in range(n)] for _ in range(n)]
# matrix_mul_time[A][B]: time needed for A to B
for size in range(1, n + 1):
    for start in range(n - size + 1):
        min_time = 0
        for split in range(start, start + size - 1):
            left_mul_time = matrix_mul_time[start][split]
            left_mat_size = (matrix_size[start][0], matrix_size[split][1])
            right_mul_time = matrix_mul_time[split + 1][start + size - 1]
            right_mat_size = (matrix_size[split + 1][0], matrix_size[start + size - 1][1])
            
            time_spent = left_mul_time + \
                         left_mat_size[0] * right_mat_size[0] * right_mat_size[1] + \
                         right_mul_time
            if min_time <= 0 or time_spent < min_time:
                min_time = time_spent
        matrix_mul_time[start][start + size - 1] = min_time
print(matrix_mul_time[0][n - 1])
            
            

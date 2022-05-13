from sys import stdin

f_input = lambda : stdin.readline().rstrip()

t = int(f_input())
for _ in range(t):
    n = int(f_input())
    files = list(map(int, f_input().split()))
    
    sum_files = [files[0]]
    for file in files[1:]:
        sum_files.append(sum_files[-1] + file)

    min_time = [[-1 for _ in range(n)] for _ in range(n)]
    # print(sum_files)
    # file_append[from][to] from에서 to까지 합치는 데 걸리는 최소 시간 -> 세그먼트 트리는 안 되나?
    # i: 개수, j: 시작점, k: 분절점
    for i in range(1, n + 1):
        for j in range(n - i + 1):
            min_val = 0
            # min val은 0이 될 수 없다. 다만, 파일이 1개일 때에는 min val이 0일 수도 있다.
            for k in range(j, j + i - 1):
                time_spent = min_time[j][k] + min_time[k + 1][j + i - 1]
                if min_val == 0 or time_spent < min_val:
                    min_val = time_spent
            sum_interval = sum_files[j + i - 1] - sum_files[j - 1] if j > 0 else sum_files[j + i - 1]
            sum_interval = 0 if i == 1 else sum_interval
            min_time[j][j + i - 1] = min_val + sum_interval
        # print(f"Length {i}, DP: {min_time}")
    print(min_time[0][n - 1])
                

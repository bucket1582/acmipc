def count_routes(x, y, m, n):
    global route_count, height_table
    if x == m - 1 and y == n - 1:
        route_count[x][y] = 1
        return route_count[x][y]
    if route_count[x][y] is not None:
        return route_count[x][y]

    route_count[x][y] = 0
    for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        dx, dy = direction
        x_next, y_next = x + dx, y + dy
        if 0 <= x_next < m and 0 <= y_next < n:
            if height_table[x_next][y_next] < height_table[x][y]:    
                route_count[x][y] += count_routes(x_next, y_next, m, n)
    return route_count[x][y]
            

from sys import stdin

f_input = lambda: stdin.readline().rstrip()

m, n = map(int, f_input().split())
height_table = []
route_count = [[None for _ in range(n)] for _ in range(m)]
for _ in range(m):
    height_table.append(list(map(int, f_input().split())))

print(count_routes(0, 0, m, n))

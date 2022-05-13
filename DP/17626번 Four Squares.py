from sys import stdin

f_input = lambda : stdin.readline().rstrip()

n = int(f_input())

quad_list = [1]
minimum_cnt = [0, 1]

for i in range(2, n + 1):
    val = 4
    quad_list.append(i ** 2)
    for quad in quad_list:
        if quad > i:
            break
        val = min(minimum_cnt[-quad] + 1, val)
    minimum_cnt.append(val)
print(minimum_cnt[-1]) 

from sys import stdin

f_input = lambda : stdin.readline().rstrip()

n = int(f_input())
f = int(f_input())

get_over_100 = n // 100

for i in range(100):
    candidate = get_over_100 * 100 + i
    if candidate % f == 0:
        break

print(format(i, "02d"))

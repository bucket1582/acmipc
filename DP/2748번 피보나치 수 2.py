from sys import stdin

f_input = lambda : stdin.readline().rstrip()

n = int(f_input())

f_n_2, f_n_1 = 0, 1
fn = 1
for _ in range(2, n + 1):
    fn = f_n_2 + f_n_1
    f_n_2 = f_n_1
    f_n_1 = fn
print(fn)

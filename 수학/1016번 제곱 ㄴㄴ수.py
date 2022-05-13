from sys import stdin

f_input = lambda : stdin.readline().rstrip()

min_val, max_val = map(int, f_input().split())

candidate_lst = [1 for _ in range(min_val, max_val + 1)]
for raw_val in range(2, int(pow(max_val, 0.5)) + 1):
    sqr_val = raw_val * raw_val
    idx = None 
    if min_val % sqr_val == 0:
        idx = 0
    else:
        idx = (min_val // sqr_val + 1) * sqr_val - min_val
    while idx < len(candidate_lst):
        candidate_lst[idx] = 0
        idx += sqr_val

print(sum(candidate_lst))

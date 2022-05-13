from sys import stdin

f_input = lambda: stdin.readline().rstrip()

f_input()
num_set = set(map(int, f_input().split()))
f_input()
ans_lst = list(map(lambda x: "1" if int(x) in num_set else "0", f_input().split()))
print(" ".join(ans_lst))

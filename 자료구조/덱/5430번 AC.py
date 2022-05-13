from sys import stdin
from collections import deque

f_input = lambda : stdin.readline().rstrip()

test_case = int(f_input())

for _ in range(test_case):
    operation = f_input()
    n = int(f_input())
    if n > 0:
        lst = deque(f_input()[1:-1].split(","))
    else:
        f_input()
        lst = deque()

    err_flag = False
    left_or_right = True # True for Left
    for op in operation:
        if op == "R":
            left_or_right = not left_or_right
        elif op == "D":
            if n <= 0:
                err_flag = True
                break
            if left_or_right:
                lst.popleft()
            else:
                lst.pop()
            n -= 1
    if err_flag:
        print("error")
    else:
        if not left_or_right:
            lst.reverse()
        print("[" + ",".join(lst) + "]")
            

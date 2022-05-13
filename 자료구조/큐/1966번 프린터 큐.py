from sys import stdin
from collections import deque

f_input = lambda : stdin.readline().rstrip()
test_cases = int(f_input())

for _ in range(test_cases):
    doc_num, q_loc = map(int, f_input().split())
    print_q = deque(map(int, f_input().split()))

    val = print_q[q_loc]
    break_flag = False
    rank = 1
    while True:
        max_val = max(print_q)

        # print(print_q, q_loc)
        cur = print_q.popleft()
        q_loc = (q_loc - 1) % doc_num
        while cur != max_val:
            print_q.append(cur)
            # print(print_q, q_loc)
            cur = print_q.popleft()
            q_loc = (q_loc - 1) % doc_num
            
        # print("Escape " + str(q_loc))
        if q_loc == doc_num - 1:
            break
        doc_num -= 1
        rank += 1
    print(rank)
    
        
            

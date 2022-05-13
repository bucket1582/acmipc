from collections import deque

# 스택 2개를 사용한다.
# 스택 A: 입력 값을 모아둔다.
# 스택 B: 스택 A에서 뽑은 수를 저장한다; 이때, 오름차순이 되도록 한다.
# 스택 B에서 pop한 원소는 다시 불러오지 않는다.

stack_a = deque()
stack_b = deque()

sequence_len = int(input())
sequence = map(int, input().split())
stack_a.extend(sequence)

answer_stack = deque()

while len(stack_a) > 0:
    a_top = stack_a.pop()
    nge_number = -1
    while len(stack_b) > 0:
        b_top = stack_b.pop()
        if b_top > a_top:
            nge_number = b_top
            stack_b.append(b_top)
            break
    stack_b.append(a_top)
    answer_stack.appendleft(str(nge_number))

print(" ".join(answer_stack))

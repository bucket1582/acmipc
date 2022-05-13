n = int(input())

sequence = list()
for i in range(n):
    sequence.append(int(input()))

i = 1
stack = list()
action_sequence = list()

impossible_flag = False
for index in range(n):
    if sequence[index] in stack[:-1]:
        impossible_flag = True
        break
    while (len(stack) == 0) or (stack[-1] != sequence[index]):
        action_sequence.append("+")
        stack.append(i)
        i += 1
    action_sequence.append("-")
    stack.pop()

if impossible_flag:
    print("NO")
else:
    for action in action_sequence:
        print(action)
        
        

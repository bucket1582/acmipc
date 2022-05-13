from sys import stdin
from collections import deque

f_input = lambda : stdin.readline().rstrip()

computer_num = int(f_input())
# graph_table[A][B] = A to B
node_num = int(f_input())

graph_dict = {}
for _ in range(node_num):
    com_a, com_b = map(int, f_input().split())
    to_lst = graph_dict.setdefault(com_a, [])
    to_lst.append(com_b)
    to_lst = graph_dict.setdefault(com_b, [])
    to_lst.append(com_a)

visited = [False for _ in range(100)]
visit_len = 0
q = deque([1])
while len(q) > 0:
    infected = q.popleft()
    if visited[infected - 1]:
        continue
    visited[infected - 1] = True
    visit_len += 1
    for newcomer in graph_dict.get(infected, []):
        q.append(newcomer)
print(visit_len - 1)


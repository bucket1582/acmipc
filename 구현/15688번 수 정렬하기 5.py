from sys import stdin

f_input = lambda : stdin.readline().rstrip()
n = int(f_input())
lst = []
for _ in range(n):
    lst.append(int(f_input()))
    
lst.sort() # Tim sort
for i in range(n):
    print(lst[i])

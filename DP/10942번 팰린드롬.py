from sys import stdin

f_input = lambda: stdin.readline().rstrip()
n = int(f_input())
seq = list(map(int, f_input().split()))
m = int(f_input())

palindrome = [[None for _ in range(n)] for _ in range(n)]
# palindrome[A][B]; A to B가 palindrome인지 아닌지 여부
for seq_len in range(1, n + 1):
    for start_idx in range(n - seq_len + 1):
        if seq_len == 1:
            palindrome[start_idx][start_idx + seq_len - 1] = True
            continue

        if seq_len == 2:
            if seq[start_idx] == seq[start_idx + seq_len - 1]:
                palindrome[start_idx][start_idx + seq_len - 1] = True
            else:
                palindrome[start_idx][start_idx + seq_len - 1] = False
            continue
        
        if seq[start_idx] == seq[start_idx + seq_len - 1] and \
           palindrome[start_idx + 1][start_idx + seq_len - 2]:
            palindrome[start_idx][start_idx + seq_len - 1] = True
        else:
            palindrome[start_idx][start_idx + seq_len - 1] = False

for _ in range(m):
    s, e = map(int, f_input().split())
    print(int(palindrome[s - 1][e - 1]))

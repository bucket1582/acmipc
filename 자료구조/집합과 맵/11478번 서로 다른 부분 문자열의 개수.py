from sys import stdin

string = stdin.readline().rstrip()

substrings = set()
for str_len in range(1, len(string) + 1):
    for start_idx in range(len(string) - str_len + 1):
        substrings.add(string[start_idx : start_idx + str_len])
print(len(substrings))

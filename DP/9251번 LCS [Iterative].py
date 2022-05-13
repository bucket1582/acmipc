import sys

# 빠른 입력
f_input = lambda : sys.stdin.readline().rstrip()

# 데이터 파싱
seq1 = f_input()
seq2 = f_input()

lcs = [0 for _ in range(len(seq1) + 1)]

for char_std in seq2:
    new_lcs = [0]
    for char_idx in range(len(seq1)):
        char_comp = seq1[char_idx]
        # 같으면, 이전까지의 문자열에 붙인다
        if char_comp == char_std:
            new_lcs.append(lcs[char_idx] + 1)
        # 다르면, 이전까지의 문자열의 길이와 현재까지의 문자열의 길이 비교
        else:
            new_lcs.append(max(new_lcs[-1], lcs[char_idx + 1]))
    lcs = new_lcs
print(max(lcs))

def binary_search(element, lst):
    left_idx = 0
    right_idx = len(lst) - 1
    while left_idx < right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if lst[mid_idx] > element:
            right_idx = mid_idx
        elif lst[mid_idx] < element:
            left_idx = mid_idx + 1
        else:
            right_idx = mid_idx
            left_idx = mid_idx
    return right_idx


from sys import stdin

f_input = lambda : stdin.readline().rstrip()

string = f_input()
q = int(f_input())

char_dict = dict()
for char in range(ord('a'), ord('z') + 1):
    char_dict[chr(char)] = []

for char_idx in range(len(string)):
    char_dict[string[char_idx]].append(char_idx)

for _ in range(q):
    char, l, r = f_input().split()
    l = int(l)
    r = int(r)
    search_lst = char_dict[char]
    if len(search_lst) == 0:
        print(0)
        continue
    left = binary_search(l, search_lst)
    right = binary_search(r, search_lst)

    adj = 0
    if search_lst[right] <= r:
        adj += 1
    if search_lst[left] < l:
        adj -= 1
    cnt = right - left + adj
    print(cnt)

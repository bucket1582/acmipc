def find_loc(lis, element):
    low = 0
    high = len(lis) - 1
    while high > low:
        mid = (low + high) // 2
        if lis[mid] < element:
            low = mid + 1
        else:
            high = mid
    return low


from sys import stdin

f_input = lambda : stdin.readline().rstrip()
f_input()
seq = list(map(int, f_input().split()))
increasing_seq = [seq[0]]

for i in range(1, len(seq)):
    last_element = increasing_seq[-1]
    if last_element < seq[i]:
        increasing_seq.append(seq[i])
        continue
    loc = find_loc(increasing_seq, seq[i])
    increasing_seq[loc] = seq[i]
print(len(increasing_seq))

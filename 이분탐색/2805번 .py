from sys import stdin

def is_valid_height(tree_height, cut_height, target):
    log_length = 0
    for height in tree_height:
        log_length += max(height - cut_height, 0)
    return log_length >= target

f_input = lambda : stdin.readline().rstrip()

_, target = map(int, f_input().split())
tree_height = list(map(int, f_input().split()))

minimum = 0
maximum = max(tree_height)
mid = maximum // 2

while minimum < mid < maximum:
    valid = is_valid_height(tree_height, mid, target)

    if not valid:
        maximum = mid - 1
    else:
        minimum = mid + 1
    mid = (minimum + maximum) // 2

if is_valid_height(tree_height, mid + 1, target):
    mid += 1
elif not is_valid_height(tree_height, mid, target):
    mid -= 1
print(mid)
    

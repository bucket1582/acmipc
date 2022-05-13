from sys import stdin

f_input = lambda : stdin.readline().rstrip()

n, a_0 = map(int, f_input().split())

if n == 0:
    print(0.0)
else:
    min_of_max = None
    max_of_min = None
    seq = list(map(int, f_input().split()))

    for i in range(len(seq)):
        min_val = (seq[i] - a_0) / (i + 1)
        max_val = (seq[i] - a_0 + 1) / (i + 1)

        if min_of_max is None or min_of_max > max_val:
            min_of_max = max_val
        if max_of_min is None or max_of_min < min_val:
            max_of_min = min_val

    if min_of_max <= max_of_min:
        print(-1)
    else:
        if max_of_min < 0:
            print(-1)
        else:
            print(max_of_min)

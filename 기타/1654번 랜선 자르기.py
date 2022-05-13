def count_lan_lines(old_lan_length, new_lan_length):
    return old_lan_length // new_lan_length

def sum_lan_count(new_lan_length, lan_length_list):
    return sum(map(lambda x: count_lan_lines(x, new_lan_length), lan_length_list))

k, n = map(int, input().split())

length_list = list()
for i in range(k):
    length_list.append(int(input()))

start = 1
end = max(length_list)
while start <= end:
    mid = (start + end) // 2
    max_lan_count = sum_lan_count(mid, length_list)
    if max_lan_count < n:
        end = mid - 1
    else:
        start = mid + 1
print(start - 1)

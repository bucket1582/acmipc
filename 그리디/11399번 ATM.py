input()
p_list = input().split()
p_list = [int(p) for p in p_list]
p_list.sort()

summation = 0
fake_sum = 0
for p in p_list:
    fake_sum += p
    summation += fake_sum
print(summation)

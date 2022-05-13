def count_factor_in_integer(integer, factor):
    count = 0
    while integer % factor == 0:
        integer //= factor
        count += 1
    return count

n = int(input())

count_two = 0
count_five = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        count_two += count_factor_in_integer(i, 2)
    if i % 5 == 0:
        count_five += count_factor_in_integer(i, 5)

print(min(count_two, count_five))

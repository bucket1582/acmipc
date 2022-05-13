def count_factor_in_integer(integer, factor):
    count = 0
    while integer >= factor:
        # 1부터 integer까지 factor의 배수 개수는 int(integer/factor)
        # 이를 겹으로 쌓아서 factor**2의 배수, factor**3의 배수... 개수 카운팅!
        count += integer // factor
        integer //= factor
    return count

n, m = map(int, input().split())
count_two = count_factor_in_integer(n, 2) -\
            count_factor_in_integer(m, 2) -\
            count_factor_in_integer(n - m, 2)
count_five = count_factor_in_integer(n, 5) -\
             count_factor_in_integer(m, 5) -\
             count_factor_in_integer(n - m, 5)

print(min(count_two, count_five))

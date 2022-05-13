from sys import stdin

f_input = lambda : stdin.readline().rstrip()

n = int(f_input())

# p_n = p_{n-1} + 2 * p_{n-2}
# p_1 = 1, p_2 = 3

num = [1, 3]

for _ in range(n + 1):
    num.append(pow(2 * num[-2] + num[-1], 1, 10007))
print(num[n - 1])

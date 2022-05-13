from sys import stdin

f_input = lambda : stdin.readline().rstrip()

n = int(f_input())

# p_n = p_{n-1} + p_{n-2}
# p_1 = 1, p_2 = 2
# Lucas Number

num = [1, 2]

for _ in range(n + 1):
    num.append(pow(num[-2] + num[-1], 1, 10007))
print(num[n - 1])

from sys import stdin

f_input = lambda: stdin.readline().rstrip()

coin_num, target = map(int, f_input().split())

coins = []
max_coin = -1
for _ in range(coin_num):
    coin = int(f_input())
    coins.append(coin)
    if coin > max_coin:
        max_coin = coin
    del coin

num_combinations = [1]
for _ in range(1, target + 1):
    possible_combinations = 0
    for coin in coins:
        if coin > len(num_combinations):
            continue
        possible_combinations += num_combinations[-coin]
    num_combinations.append(possible_combinations)
    if len(num_combinations) > max_coin:
        num_combinations.pop(0)
    print(num_combinations, num_combinations[-1])
print(num_combinations[-1])

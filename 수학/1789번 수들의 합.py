from sys import stdin

s = int(stdin.readline().rstrip())

# 1부터 k까지의 자연수의 합과 남은 수 k' 합으로 s를 나타내면 가장 많다
cnt = 0
max_i = 1
while True:
    if s - max_i <= max_i:
        break
    cnt += 1
    s -= max_i
    max_i += 1
cnt += 1
print(cnt)
